import unittest
from sklearn.pipeline import Pipeline
from pprint import pprint
import pandas as pd
import traceback
from os import environ

from ibm_watson_machine_learning import APIClient

from ibm_watson_machine_learning.experiment import AutoAI
from ibm_watson_machine_learning.deployment import WebService, Batch
from ibm_watson_machine_learning.workspace import WorkSpace

from ibm_watson_machine_learning.helpers.connections import S3Connection, S3Location, DataConnection, FSLocation

from ibm_watson_machine_learning.experiment.autoai.optimizers import RemoteAutoPipelines

from ibm_watson_machine_learning.utils.autoai.errors import NotExistingCOSResource

from ibm_watson_machine_learning.tests.utils import (get_wml_credentials, get_cos_credentials, bucket_exists,
                                                        create_bucket, get_space_id, is_cp4d)
from ibm_watson_machine_learning.tests.utils.cleanup import space_cleanup, delete_model_deployment

from ibm_watson_machine_learning.utils.autoai.enums import PositiveLabelClass, TShirtSize, Transformers



@unittest.skipIf(not is_cp4d(), "Not supported on cloud")
class TestAutoAIRemote(unittest.TestCase):
    """
    The test can be run on CLOUD, WMLS and CPD (not tested)
    The test covers:
    - COS set-up (if run on Cloud): checking if bucket exists for the cos instance, if not new bucket is create
    - Saving data `/bank.cdv` to COS/data assets
    - downloading training data from cos/data assets
    - downloading all generated pipelines to lale pipeline
    - deployment with lale pipeline
    - deployment deletion
    """
    wml_client: 'APIClient' = None
    experiment: 'AutoAI' = None
    remote_auto_pipelines: 'RemoteAutoPipelines' = None
    wml_credentials = None
    cos_credentials = None
    pipeline_opt: 'RemoteAutoPipelines' = None
    service: 'WebService' = None
    service_batch: 'Batch' = None

    data_location = './autoai/data/breast_cancer.csv'


    positive_label = 'M'
    prediction_column = 'diagnosis'

    trained_pipeline_details = None
    run_id = None

    data_connection = None
    results_connection = None

    train_data = None

    bucket_name = environ.get('BUCKET_NAME', "wml-autoaitests-qa")
    pod_version = environ.get('KB_VERSION', None)
    space_name = environ.get('SPACE_NAME', 'regression_tests_sdk_space')

    cos_endpoint = "https://s3.us-south.cloud-object-storage.appdomain.cloud"
    data_cos_path = 'data/breast_cancer.csv'
    cos_resource_instance_id = None

    results_cos_path = 'results_wml_autoai'

    pipeline: 'Pipeline' = None
    lale_pipeline = None
    deployed_pipeline = None
    hyperopt_pipelines = None
    new_pipeline = None
    new_sklearn_pipeline = None
    X_values = None
    y_values = None

    OPTIMIZER_NAME = 'BREAST CANCER csv wml_autoai binary test'
    DEPLOYMENT_NAME = "BREAST CANCER AutoAI Deployment tests"

    project_id = None
    space_id = None

    asset_id = None

    @classmethod
    def setUpClass(cls) -> None:
        """
        Load WML credentials from config.ini file based on ENV variable.
        """
        cls.wml_credentials = get_wml_credentials()
        try:
            del cls.wml_credentials['password']
        except:
            pass
        try:
            del cls.wml_credentials['bedrock_url']
        except:
            pass

        assert(cls.wml_credentials.get('username') is not None)
        assert(cls.wml_credentials.get('password') is None)
        assert (cls.wml_credentials.get('bedrock_url') is None)
        assert(cls.wml_credentials.get('apikey') is not None)
        cls.wml_client = APIClient(wml_credentials=cls.wml_credentials.copy())

        if not cls.wml_client.ICP:
            cls.cos_credentials = get_cos_credentials()
            cls.cos_endpoint = cls.cos_credentials.get('endpoint_url')
            cls.cos_resource_instance_id = cls.cos_credentials.get('resource_instance_id')

        cls.project_id = cls.wml_credentials.get('project_id')


    def test_00a_space_cleanup(self):
        space_cleanup(self.wml_client,
                      get_space_id(self.wml_client, self.space_name,
                                   cos_resource_instance_id=self.cos_resource_instance_id),
                      days_old=7)
        TestAutoAIRemote.space_id = get_space_id(self.wml_client, self.space_name,
                                     cos_resource_instance_id=self.cos_resource_instance_id)
        if self.wml_client.ICP:
            self.wml_client.set.default_project(self.project_id)
        else:
            self.wml_client.set.default_space(self.space_id)

    def test_00b_prepare_COS_instance(self):
        if self.wml_client.ICP:
            self.skipTest("Prepare COS is available only for Cloud")
        import ibm_boto3
        cos_resource = ibm_boto3.resource(
            service_name="s3",
            endpoint_url=self.cos_endpoint,
            aws_access_key_id=self.cos_credentials['cos_hmac_keys']['access_key_id'],
            aws_secret_access_key=self.cos_credentials['cos_hmac_keys']['secret_access_key']
        )
        # Prepare bucket
        if not bucket_exists(cos_resource, self.bucket_name):
            TestAutoAIRemote.bucket_name = create_bucket(cos_resource, self.bucket_name)

            self.assertIsNotNone(TestAutoAIRemote.bucket_name)
            self.assertTrue(bucket_exists(cos_resource, TestAutoAIRemote.bucket_name))

        print(f"Using COS bucket: {TestAutoAIRemote.bucket_name}")

    def test_01_initialize_AutoAI_experiment__pass_credentials__object_initialized(self):
        TestAutoAIRemote.experiment = AutoAI(wml_credentials=self.wml_credentials.copy(),
                                             project_id=self.project_id,
                                             space_id=self.space_id)

        self.assertIsInstance(self.experiment, AutoAI, msg="Experiment is not of type AutoAI.")

    def test_02_save_remote_data_and_DataConnection_setup(self):
        if self.wml_client.ICP:
            TestAutoAIRemote.data_connection = DataConnection(
                            location=FSLocation(path=self.data_location))
            TestAutoAIRemote.results_connection = None

        else: #for cloud and COS
            TestAutoAIRemote.data_connection = DataConnection(
                connection=S3Connection(endpoint_url=self.cos_endpoint,
                                        access_key_id=self.cos_credentials['cos_hmac_keys']['access_key_id'],
                                        secret_access_key=self.cos_credentials['cos_hmac_keys']['secret_access_key']),
                location=S3Location(bucket=self.bucket_name,
                                    path=self.data_cos_path)
            )
            TestAutoAIRemote.results_connection = DataConnection(
                connection=S3Connection(endpoint_url=self.cos_endpoint,
                                        access_key_id=self.cos_credentials['cos_hmac_keys']['access_key_id'],
                                        secret_access_key=self.cos_credentials['cos_hmac_keys']['secret_access_key']),
                location=S3Location(bucket=self.bucket_name,
                                    path=self.results_cos_path)
            )
            TestAutoAIRemote.data_connection.write(data=self.data_location, remote_name=self.data_cos_path)

        self.assertIsNotNone(obj=TestAutoAIRemote.data_connection)

    def test_02a_read_saved_remote_data_before_fit(self):
        data = self.data_connection.read()
        print(f"Data sample")
        print(data.head())
        self.assertGreater(len(data), 0)

    def test_03_initialize_optimizer(self):
        TestAutoAIRemote.remote_auto_pipelines = self.experiment.optimizer(
            name=self.OPTIMIZER_NAME,
            desc='test description',
            prediction_type=self.experiment.PredictionType.BINARY,
            prediction_column=self.prediction_column,
            positive_label=self.positive_label,
            scoring=PositiveLabelClass.PRECISION_SCORE_MICRO,
            # cognito_transform_names=[Transformers.DIFF,Transformers.SUM,Transformers.MAX,
            #                          Transformers.SIN,Transformers.SUM],
            include_only_estimators=[self.experiment.ClassificationAlgorithms.LR,
                                     self.experiment.ClassificationAlgorithms.LGBM],
            test_size=0.1,
            max_number_of_estimators=2,
            t_shirt_size=TShirtSize.S if self.wml_client.ICP else TShirtSize.L
        )

        self.assertIsInstance(self.remote_auto_pipelines, RemoteAutoPipelines,
                              msg="experiment.optimizer did not return RemoteAutoPipelines object")

    def test_04_get_configuration_parameters_of_remote_auto_pipeline(self):
        parameters = self.remote_auto_pipelines.get_params()
        print(parameters)
        self.assertIsInstance(parameters, dict, msg='Config parameters are not a dictionary instance.')

    def test_05_fit_run_training_of_auto_ai_in_wml(self):
        TestAutoAIRemote.trained_pipeline_details = self.remote_auto_pipelines.fit(
            training_data_reference=[self.data_connection],
            training_results_reference=self.results_connection,
            background_mode=False)

        TestAutoAIRemote.run_id = self.trained_pipeline_details['metadata']['id']

        self.assertIsNotNone(self.data_connection.auto_pipeline_params,
                             msg='DataConnection auto_pipeline_params was not updated.')
        # TestAutoAIRemote.run_id = '2360fdc3-f06d-4053-9485-23ee9736f8e4'
        # TestAutoAIRemote.remote_auto_pipelines = self.experiment.runs.get_optimizer(TestAutoAIRemote.run_id)

    def test_05a_fit_error_when_cos_file_not_exists(self):
        if self.wml_client.ICP:
            self.skipTest("Prepare COS is available only for Cloud")

        with self.assertRaises(NotExistingCOSResource, msg="Training should raise error when non existing COS bucket given"):
            self.remote_auto_pipelines.fit(
                training_data_reference=[
                    DataConnection(
                    connection=S3Connection(endpoint_url=self.cos_endpoint,
                                            access_key_id=self.cos_credentials['cos_hmac_keys']['access_key_id'],
                                            secret_access_key=self.cos_credentials['cos_hmac_keys']['secret_access_key']),
                    location=S3Location(bucket="not_existing",
                                        path=self.data_cos_path)
                )],
                training_results_reference=self.results_connection,
                background_mode=False)

        with self.assertRaises(NotExistingCOSResource, msg="Training should raise error when non existing COS file given"):
            self.remote_auto_pipelines.fit(
                training_data_reference=[
                    DataConnection(
                        connection=S3Connection(endpoint_url=self.cos_endpoint,
                                                access_key_id=self.cos_credentials['cos_hmac_keys']['access_key_id'],
                                                secret_access_key=self.cos_credentials['cos_hmac_keys'][
                                                    'secret_access_key']),
                        location=S3Location(bucket=self.bucket_name,
                                            path="not_existing")
                    )],
                training_results_reference=self.results_connection,
                background_mode=False)

    def test_06_get_train_data(self):
        TestAutoAIRemote.train_data = self.remote_auto_pipelines.get_data_connections()[0].read()

        print("train data sample:")
        print(self.train_data.head())
        self.assertGreater(len(self.train_data), 0)

        TestAutoAIRemote.X_values = self.train_data.drop([self.prediction_column], axis=1)[:10].values
        TestAutoAIRemote.y_values = self.train_data[self.prediction_column][:10]

    def test_07_get_run_status(self):
        status = self.remote_auto_pipelines.get_run_status()
        self.assertEqual(status, "completed", msg="AutoAI run didn't finished successfully. Status: {}".format(status))

    def test_08_get_run_details(self):
        parameters = self.remote_auto_pipelines.get_run_details()
        print(parameters)
        print("\n\n")
        print(parameters.get('entity').get('status'))
        self.assertIsNotNone(parameters)

    def test_08b_get_metrics(self):
        self.wml_client.training.get_metrics(self.run_id)

    def test_09_predict_using_fitted_pipeline(self):
        predictions = self.remote_auto_pipelines.predict(X=self.X_values[:5])
        print(predictions)
        self.assertGreater(len(predictions), 0)

    def test_10_summary_listing_all_pipelines_from_wml(self):
        pipelines_details = self.remote_auto_pipelines.summary()
        print(pipelines_details)

    def test_11__get_data_connections__return_a_list_with_data_connections_with_optimizer_params(self):
        data_connections = self.remote_auto_pipelines.get_data_connections()
        self.assertIsInstance(data_connections, list, msg="There should be a list container returned")
        self.assertIsInstance(data_connections[0], DataConnection,
                              msg="There should be a DataConnection object returned")

    def test_12_get_pipeline_params_specific_pipeline_parameters(self):
        pipeline_params = self.remote_auto_pipelines.get_pipeline_details(pipeline_name='Pipeline_1')
        print(pipeline_params)

    def test_13__get_pipeline_params__fetch_best_pipeline_parameters__parameters_fetched_as_dict(self):
        best_pipeline_params = self.remote_auto_pipelines.get_pipeline_details()
        print(best_pipeline_params)

    ####
    # LALE #
    ########

    def test_14__get_pipeline__load_lale_pipeline__pipeline_loaded(self):
        TestAutoAIRemote.pipeline = self.remote_auto_pipelines.get_pipeline(pipeline_name='Pipeline_4')
        print(f"Fetched pipeline type: {type(self.pipeline)}")

        # self.assertIsInstance(self.pipeline, TrainablePipeline,
        #                       msg="Fetched pipeline is not of TrainablePipeline instance.")
        predictions = self.pipeline.predict(
            X=self.X_values[:5])  # works with autoai_libs from branch `development` (date: 9th March 20)
        print(predictions)

    def test_15_get_all_pipelines_as_lale(self):
        summary = self.remote_auto_pipelines.summary()
        print(summary)
        failed_pipelines = []
        for pipeline_name in summary.reset_index()['Pipeline Name']:
            print(f"Getting pipeline: {pipeline_name}")
            lale_pipeline = None
            try:
                lale_pipeline = self.remote_auto_pipelines.get_pipeline(pipeline_name=pipeline_name)
                # self.assertIsInstance(lale_pipeline, TrainablePipeline)
                predictions = lale_pipeline.predict(
                    X=self.X_values[:1])
                print(predictions)
                self.assertGreater(len(predictions), 0, msg=f"Returned prediction for {pipeline_name} are empty")
            except:
                print(f"Failure: {pipeline_name}")
                failed_pipelines.append(pipeline_name)
                traceback.print_exc()

            if not TestAutoAIRemote.lale_pipeline:
                TestAutoAIRemote.lale_pipeline = lale_pipeline
                print(f"{pipeline_name} loaded for next test cases")

        self.assertEqual(len(failed_pipelines), 0, msg=f"Some pipelines failed. Full list: {failed_pipelines}")

    #################################
    #      DEPLOYMENT SECTION       #
    #################################

    def test_21_deployment_setup_and_preparation(self):
        TestAutoAIRemote.service = WebService(source_wml_credentials=self.wml_credentials.copy(),
                                              source_project_id=self.project_id,
                                              source_space_id=self.space_id)
        self.wml_client.set.default_space(self.space_id)
        delete_model_deployment(self.wml_client, deployment_name=self.DEPLOYMENT_NAME)
        self.wml_client.set.default_project(self.project_id) if self.project_id else None

        self.assertIsInstance(self.service, WebService, msg="Deployment is not of WebService type.")
        self.assertIsInstance(self.service._source_workspace, WorkSpace, msg="Workspace set incorrectly.")
        self.assertEqual(self.service.id, None, msg="Deployment ID initialized incorrectly")
        self.assertEqual(self.service.name, None, msg="Deployment name initialized incorrectly")

    def test_22__deploy__deploy_best_computed_pipeline_from_autoai_on_wml(self):
        self.service.create(
            experiment_run_id=self.remote_auto_pipelines._engine._current_run_id,
            model="Pipeline_1",
            deployment_name=self.DEPLOYMENT_NAME)

        self.assertIsNotNone(self.service.id, msg="Online Deployment creation - missing id")
        self.assertIsNotNone(self.service.name, msg="Online Deployment creation - name not set")
        self.assertIsNotNone(self.service.scoring_url,
                             msg="Online Deployment creation - mscoring url  missing")

    def test_23_score_deployed_model(self):
        nb_records = 5
        predictions = self.service.score(payload=self.train_data.drop([self.prediction_column], axis=1)[:nb_records])
        print(predictions)
        self.assertIsNotNone(predictions)
        self.assertEqual(len(predictions['predictions'][0]['values']), nb_records)

    def test_24_list_deployments(self):
        self.service.list()
        params = self.service.get_params()
        print(params)
        self.assertIsNotNone(params)

    def test_25_delete_deployment(self):
        print("Delete current deployment: {}".format(self.service.deployment_id))
        self.service.delete()
        self.wml_client.set.default_space(self.space_id) if not self.wml_client.default_space_id else None
        self.wml_client.repository.delete(self.service.asset_id)
        self.wml_client.set.default_project(self.project_id) if is_cp4d() else None
        self.assertEqual(self.service.id, None, msg="Deployment ID deleted incorrectly")
        self.assertEqual(self.service.name, None, msg="Deployment name deleted incorrectly")
        self.assertEqual(self.service.scoring_url, None,
                         msg="Deployment scoring_url deleted incorrectly")

    #########################
    #  Batch deployment
    #########################

    def test_30_batch_deployment_setup_and_preparation(self):
        if self.wml_client.ICP:
            TestAutoAIRemote.service_batch = Batch(source_wml_credentials=self.wml_credentials.copy(),
                                                   source_project_id=self.project_id,
                                                   target_wml_credentials=self.wml_credentials,
                                                   target_space_id=self.space_id)
        else:
            TestAutoAIRemote.service_batch = Batch(self.wml_credentials,
                                                   source_space_id=self.space_id)

        self.assertIsInstance(self.service_batch, Batch, msg="Deployment is not of Batch type.")
        self.assertIsInstance(self.service_batch._source_workspace, WorkSpace, msg="Workspace set incorrectly.")
        self.assertEqual(self.service_batch.id, None, msg="Deployment ID initialized incorrectly")
        self.assertEqual(self.service_batch.name, None, msg="Deployment name initialized incorrectly")

    def test_32__deploy__batch_deploy_best_computed_pipeline_from_autoai_on_wml(self):
        self.service_batch.create(
            experiment_run_id=self.remote_auto_pipelines._engine._current_run_id,
            model="Pipeline_2",
            deployment_name=self.DEPLOYMENT_NAME + ' BATCH')

        self.assertIsNotNone(self.service_batch.id, msg="Batch Deployment creation - missing id")
        self.assertIsNotNone(self.service_batch.id, msg="Batch Deployment creation - name not set")
        self.assertIsNotNone(self.service_batch.asset_id,
                          msg="Batch Deployment creation - model (asset) id missing, incorrect model storing")

    def test_33_score_batch_deployed_model(self):
        scoring_params = self.service_batch.run_job(
            payload=self.train_data.drop(columns=[self.prediction_column]),
            background_mode=False)
        print(scoring_params)
        print(self.service_batch.get_job_result(scoring_params['metadata']['id']))
        self.assertIsNotNone(scoring_params)
        self.assertIn('predictions', str(scoring_params).lower())

    def test_34_list_batch_deployments(self):
        deployments = self.service_batch.list()
        print(deployments)
        self.assertIn('created_at', str(deployments).lower())
        self.assertIn('status', str(deployments).lower())

        params = self.service_batch.get_params()
        print(params)
        self.assertIsNotNone(params)

    def test_35_delete_deployment_batch(self):
        print("Delete current deployment: {}".format(self.service_batch.deployment_id))
        self.service_batch.delete()
        self.wml_client.set.default_space(self.space_id) if not self.wml_client.default_space_id else None
        self.wml_client.repository.delete(self.service_batch.asset_id)
        self.wml_client.set.default_project(self.project_id) if is_cp4d() else None
        self.assertEqual(self.service_batch.id, None, msg="Deployment ID deleted incorrectly")
        self.assertEqual(self.service_batch.name, None, msg="Deployment name deleted incorrectly")
        self.assertEqual(self.service_batch.scoring_url, None,
                         msg="Deployment scoring_url deleted incorrectly")
if __name__ == '__main__':
    unittest.main()
