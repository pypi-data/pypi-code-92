import dataclasses
import datetime
import itertools
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List, Union, Any

import dateutil.parser
from stringcase import camelcase
from imecilabt_utils.utils import duration_string_to_seconds

from imecilabt.gpulab.model.job import urn_to_name, urn_to_auth, urn_to_user_mini_id, DOCKER_IMAGE_USERPASS_PATTERN
from imecilabt.gpulab.model.usage_statistics import GPULabUsageStatistics, GpuOverview
from dataclass_dict_convert import dataclass_dict_convert, create_wrap_in_list_from_convertor, \
    dataclass_auto_type_check, dataclass_copy_method, dataclass_multiline_repr
from imecilabt_utils.urn_util import URN, is_valid_urn, check_valid_urn_bytype
from imecilabt_utils.validation_utils import is_valid_uuid, is_valid_email, is_valid_ssh_key, ALLOWED_HOST_KEY_ALGOS


def is_valid_job_id(id: str) -> bool:
    return is_valid_uuid(id)  # we allow both version 1 and 4 UUIDs (version 4 is used for new jobs)
    #return is_valid_uuid4(id)


def _test_char_list(tested_list: Optional[List[str]], tested_list_name: str, *, dont_allow_any_single_char: bool = False) -> None:
    if isinstance(tested_list, list) and (len(tested_list) >= 5 or dont_allow_any_single_char):
        if len(tested_list) == 0:
            return
        has_single_char = any(len(el) == 1 for el in tested_list)
        all_single_char = all(len(el) == 1 for el in tested_list)
        if all_single_char:
            if dont_allow_any_single_char:
                # Almost certain: there is a programming error somewhere, and we have a list of chars made from a single string...
                raise ValueError('Bug: {} is list of single char str, instead a list of str'.format(tested_list_name))
            elif len(tested_list) >= 5:
                # Extremely low chance this is a real list of str
                # Most likely: there is a programming error somewhere, and we have a list of chars made from a single string...
                raise ValueError('Bug: {} is list of single char str, instead a list of str'.format(tested_list_name))
            else:
                # short list with single chars. We're not sure.
                pass
        if has_single_char and dont_allow_any_single_char:
            raise ValueError('{} contains a single char str. This is not correct.'.format(tested_list_name))


def _parse_opt_date(opt_date_str: Optional[str]) -> Optional[datetime.datetime]:
    return dateutil.parser.parse(opt_date_str) if opt_date_str else None


def _ensure_opt_date(opt_date_any: Optional[Union[str, datetime.datetime]]) -> Optional[datetime.datetime]:
    if opt_date_any is None:
        return None
    if isinstance(opt_date_any, datetime.datetime):
        return opt_date_any
    return dateutil.parser.parse(opt_date_any)


def _opt_date_str(opt_date: Optional[datetime.datetime]) -> Optional[str]:
    return opt_date.isoformat() if opt_date else None


def _int_or_none(val: Optional[Any]) -> Optional[int]:
    return int(val) if val is not None else None


class JobStatus(Enum):
    ONHOLD = 'On Hold'             # On hold, not planned to run at this time (not in queue)
    QUEUED = 'Queued'              # Available to run, waiting in queue
    ASSIGNED = 'Assigned'          # Assigned to a specific node by the scheduler, but not yet "picked up" by that node.
    STARTING = 'Starting'          # Received by worker, setup in progress, not yet running
    RUNNING = 'Running'            # Running on worker
    CANCELLED = 'Cancelled'        # Cancelled during run (due to user request)
    FINISHED = 'Finished'          # Run completed
    DELETED = 'Deleted'            # Marked as deleted. This causes it to be ignored in "queue" view
    FAILED = 'Failed'              # Failure due to job definition problem, system problems, or other.


# dataclasses_json.cfg.global_config.encoders[JobStatus] = lambda js: js.name if js is not None else None
# dataclasses_json.cfg.global_config.decoders[JobStatus] = JobStatus.__members__.get


@dataclass_dict_convert(dict_letter_case=camelcase)
@dataclass(frozen=True)
@dataclass_auto_type_check
@dataclass_copy_method
@dataclass_multiline_repr
class JobPortMapping:
    container_port: int = None
    host_port: Optional[int] = None
    host_ip: Optional[str] = None

    @classmethod
    def from_docker_dict(cls, d: dict, *, container_port: Optional[Union[int, str]] = None) -> 'JobPortMapping':
        """
        Make JobPortMapping from the port mapping dict that docker returns
        :param d: the dict that docker returns
        :param container_port: set the container_port directly instead of using the dict (optional)
        :return:
        """
        def _handle_port_val(val: Union[str, int]) -> Optional[int]:
            if val is None:
                return None
            if isinstance(val, int):
                return val
            val = str(val)
            val = val.replace("/tcp", "").replace("/udp", "")
            return int(val)

        return cls(
            container_port=_handle_port_val(container_port if container_port else d.get('ContainerPort', d.get('containerPort', d.get('container_port')))),
            host_port=_handle_port_val(d.get('HostPort', d.get('hostPort', d.get('host_port')))),
            host_ip=d.get('HostIp', d.get('hostIp', d.get('host_ip'))),
        )
    #
    # @staticmethod
    # def from_dict_list(pm_dict_lst: List[Dict]) -> List['JobPortMapping']:
    #     # Note: normally, you can do this with Job.schema().load(pm_dict_lst, many=True)
    #     #       that seems to ignore global decoders however
    #     #       (which is not a problem here, but we also avoid it here for consistency)
    #     return [JobPortMapping.from_dict(d) for d in pm_dict_lst]


def camelCaseOrAllCaps(input: str) -> str:
    if input.isupper():
        return input
    else:
        from stringcase import camelcase
        return camelcase(input)


# @dataclass_dict_convert(dict_letter_case=camelcase)
@dataclass_dict_convert(dict_letter_case=camelCaseOrAllCaps)
@dataclass(frozen=True)
@dataclass_auto_type_check
@dataclass_copy_method
@dataclass_multiline_repr
class JobEventTimes:
    created: datetime.datetime
    status_updated: datetime.datetime

    QUEUED: Optional[datetime.datetime] = None
    ASSIGNED: Optional[datetime.datetime] = None
    STARTING: Optional[datetime.datetime] = None
    RUNNING: Optional[datetime.datetime] = None
    FINISHED: Optional[datetime.datetime] = None
    FAILED: Optional[datetime.datetime] = None
    CANCELLED: Optional[datetime.datetime] = None
    DELETED: Optional[datetime.datetime] = None

    long_run_notify: Optional[datetime.datetime] = None # last time long run notify email was sent

    def end_date(self) -> Optional[datetime.datetime]:
        if self.FINISHED:
            return self.FINISHED
        if self.FAILED:
            return self.FAILED
        if self.CANCELLED:
            return self.CANCELLED
        if self.DELETED:
            return self.DELETED
        return None

    def get_duration(self) -> Optional[datetime.timedelta]:
        start = self.RUNNING
        end = self.FINISHED
        if start is None:
            return None
        if end is None:
            end = datetime.datetime.now(datetime.timezone.utc)
        assert end.tzinfo is not None, 'end is naive "{}"'.format(end)
        assert start.tzinfo is not None, 'start is naive "{}"'.format(start)
        return end - start

    def get_queue_duration(self) -> Optional[datetime.timedelta]:
        start = self.QUEUED
        end = self.STARTING or self.RUNNING or self.FAILED or self.CANCELLED or self.DELETED
        if start is None:
            return None
        if end is None:
            end = datetime.datetime.now(datetime.timezone.utc)
        assert end.tzinfo is not None, 'end is naive "{}"'.format(start)
        assert start.tzinfo is not None, 'start is naive "{}"'.format(self.queue_time)
        return end - start

    def sanitized_copy(self, logged_in=True, same_project=False) -> 'JobEventTimes':
        # all may be known
        # TODO maybe hide some more if not logged_in
        return dataclasses.replace(self, long_run_notify=None)


@dataclass_dict_convert(dict_letter_case=camelcase)
@dataclass(frozen=True)
@dataclass_auto_type_check
@dataclass_copy_method
@dataclass_multiline_repr
class JobStateResources:
    cluster_id: int
    gpu_ids: List[int]
    cpu_ids: List[int]
    cpu_memory_gb: int
    gpu_memory_gb: int  # if less than a GB, this is rounded DOWN (so it can be 0!)

    slave_name: str
    slave_host: str
    slave_instance_id: str
    slave_instance_pid: int
    worker_id: int

    ssh_host: Optional[str] = None
    ssh_port: Optional[int] = None
    ssh_username: Optional[str] = None
    ssh_proxy_host: Optional[str] = None
    ssh_proxy_port: Optional[int] = None
    ssh_proxy_username: Optional[str] = None

    port_mappings: List[JobPortMapping] = field(default_factory=list)
    gpu_details: Optional[GpuOverview] = None

    @property
    def cpu_memory_mb(self) -> int:
        # while GB is sometimes 1000^3 instead of 1024^3 (typically HD size etc), for memory, base 1024 is always used.
        # (and docker seems to use 1000 based, which is silly)
        return self.cpu_memory_gb * 1024

    @property
    def cpu_memory_byte(self) -> int:
        # while GB is sometimes 1000^3 instead of 1024^3 (typically HD size etc), for memory, base 1024 is always used.
        # (and docker seems to use 1000 based, which is silly)
        return self.cpu_memory_gb * 1024 * 1024 * 1024

    def sanitized_copy(self, logged_in=True, same_project=False) -> 'JobStateResources':
        # not entirely public, but all not that private
        res = dataclasses.replace(
            self,
            ssh_username='hidden',
            ssh_proxy_username='hidden',
            port_mappings=[],
            gpu_details=None
        )
        if not logged_in:
            res = dataclasses.replace(
                res,
                gpu_ids=[],
                cpu_ids=[],
                slave_host='hidden',
                slave_name='hidden',
                slave_instance_id='hidden',
                slave_instance_pid=-1,
                worker_id=-1,
                ssh_host='hidden',
                ssh_port=-1,
                ssh_proxy_host='hidden',
                ssh_proxy_port=-1,
            )
        return res


@dataclass_dict_convert(dict_letter_case=camelcase)
@dataclass(frozen=True)
@dataclass_auto_type_check
@dataclass_copy_method
class MaxSimultaneousJobs:
    bucket_name: str
    bucket_max: int


@dataclass_dict_convert(dict_letter_case=camelcase)
@dataclass(frozen=True, repr=False)
@dataclass_auto_type_check
@dataclass_copy_method
@dataclass_multiline_repr
class JobRequestExtra:
    ssh_pub_keys: List[str] = field(default_factory=list)
    email_on_queue: List[str] = field(default_factory=list)
    email_on_run: List[str] = field(default_factory=list)
    email_on_end: List[str] = field(default_factory=list)

    def __post_init__(self):
        for email in itertools.chain(self.email_on_queue, self.email_on_run, self.email_on_end):
            if not is_valid_email(email):
                raise ValueError('Invalid email "{}"'.format(email))
        for ssh_pub_key in self.ssh_pub_keys:
            if not is_valid_ssh_key(ssh_pub_key):
                raise ValueError('Invalid SSH public key "{}" (allowed host key algos: {})'
                                 .format(ssh_pub_key, ALLOWED_HOST_KEY_ALGOS))

    def sanitized_copy(self, logged_in=True, same_project=False) -> 'JobRequestExtra':
        # hide all
        return JobRequestExtra([], [], [], [])


@dataclass_dict_convert(dict_letter_case=camelcase)
@dataclass(frozen=True)
@dataclass_auto_type_check
@dataclass_copy_method
@dataclass_multiline_repr
class JobRequestScheduling:
    interactive: bool = False
    killable_after: Optional[str] = None  # duration str
    restartable: bool = False
    reservation_id: Optional[str] = None
    max_duration: Optional[str] = None  # duration str
    max_simultaneous_jobs: Optional[MaxSimultaneousJobs] = None
    not_before: Optional[datetime.datetime] = None
    not_after: Optional[datetime.datetime] = None

    def __post_init__(self):
        if self.killable_after is not None and not duration_string_to_seconds(self.killable_after):
            raise AttributeError('killable_after must be a number followed by a time unit, not "{}"'
                                 .format(self.killable_after))
        if self.max_duration is not None:
            max_dur_s = duration_string_to_seconds(self.max_duration)
            if max_dur_s is None:
                raise AttributeError('max_duration must be a number followed by a time unit, not "{}"'
                                     .format(self.max_duration))
            if max_dur_s < 60:
                raise AttributeError('max_duration must be at least 1 minute, not "{}"'
                                     .format(self.max_duration))

    @property
    def max_duration_s(self) -> Optional[int]:
        return duration_string_to_seconds(self.max_duration) if self.max_duration is not None else None

    @property
    def killable_after_s(self) -> Optional[int]:
        return duration_string_to_seconds(self.killable_after) if self.killable_after is not None else None

    def sanitized_copy(self, logged_in=True, same_project=False) -> 'JobRequestScheduling':
        # hide only reservation ID
        return dataclasses.replace(self, reservation_id='hidden' if self.reservation_id else None)


@dataclass_dict_convert(dict_letter_case=camelcase)
@dataclass(frozen=True)
@dataclass_auto_type_check
@dataclass_copy_method
@dataclass_multiline_repr
class JobStateScheduling:
    assigned_cluster_id: Optional[int] = None
    assigned_instance_id: Optional[str] = None
    assigned_slave_name: Optional[str] = None
    # assigned_time: Optional[datetime.datetime] = None  # Not needed, stored in JobEventTimes
    queued_explanations: List[str] = field(default_factory=list)
    within_max_simultaneous_jobs: Optional[bool] = None  # deprecated now! Scheduling determines this internally on the fly instead
    tally_increment: Optional[float] = None  # The tally increment each 5 minutes caused by the resource use of this job

    def sanitized_copy(self, logged_in=True, same_project=False) -> 'JobStateScheduling':
        # Nothing to hide
        # TODO maybe hide some more if not logged_in
        return self.make_copy()

    def make_compatible_with(self, gpulab_api_version: str) -> 'JobStateScheduling':
        """
        Return a version of this that is backwards compatible with version 3.X.
        :param gpulab_api_version: version to be compatible with.
        :return:
        """
        if gpulab_api_version == '3.1':
            return self
        else:
            assert gpulab_api_version == '3.0'
            return JobStateScheduling(
                assigned_cluster_id=self.assigned_cluster_id,
                assigned_instance_id=self.assigned_instance_id,
                assigned_slave_name=self.assigned_slave_name,
                queued_explanations=list(self.queued_explanations),
                within_max_simultaneous_jobs=self.within_max_simultaneous_jobs,
                tally_increment=None,  # tally_increment is not compatible with 3.0
            )


@dataclass_dict_convert(
    dict_letter_case=camelcase,
    custom_from_dict_convertors={
        'gpu_model': create_wrap_in_list_from_convertor(str),
    }
)
@dataclass(frozen=True)
@dataclass_auto_type_check
@dataclass_copy_method
@dataclass_multiline_repr
class JobRequestResources:
    cpus: int
    gpus: int
    cpu_memory_gb: int
    gpu_memory_gb: Optional[int] = None

    features: List[str] = field(default_factory=list)
    gpu_model: List[str] = field(default_factory=list)  # We used to allow None, a str or a list of str. We don't allow a naked str anymore.
    min_cuda_version: Optional[int] = None
    cluster_id: Optional[int] = None
    slave_name: Optional[str] = None
    slave_instance_id: Optional[str] = None

    def __post_init__(self):
        _test_char_list(self.gpu_model, 'Job.request.resources.gpu_model', dont_allow_any_single_char=True)
        _test_char_list(self.features, 'Job.request.resources.features', dont_allow_any_single_char=True)

    def sanitized_copy(self, logged_in=True, same_project=False) -> 'JobRequestResources':
        """copy with removed confidential data
        :param logged_in: sanitized copy for logged in user, or for anonymous user?
        :param same_project: sanitized copy for user in same project, or for someone else?
        """
        return self.make_copy()  # nothing to sanitize

    @property
    def cluster_id_list(self) -> List[int]:
        return [self.cluster_id] if self.cluster_id else []

    @property
    def cpu_memory_mb(self) -> int:
        # while GB is sometimes 1000^3 instead of 1024^3 (typically HD size etc), for memory, base 1024 is always used.
        # (and docker seems to use 1000 based, which is silly)
        return self.cpu_memory_gb * 1024

    @property
    def cpu_memory_byte(self) -> int:
        # while GB is sometimes 1000^3 instead of 1024^3 (typically HD size etc), for memory, base 1024 is always used.
        # (and docker seems to use 1000 based, which is silly)
        return self.cpu_memory_gb * 1024 * 1024 * 1024

    def matches_gpu_model(self, tested_model: str) -> bool:
        return any(my_model.lower() in tested_model.lower() for my_model in self.gpu_model)


@dataclass_dict_convert(dict_letter_case=camelcase)
@dataclass(frozen=True)
@dataclass_auto_type_check
@dataclass_copy_method
@dataclass_multiline_repr
class JobStorage:
    container_path: Optional[str] = None  # default: host_path
    host_path: Optional[str] = None  # default: container_path

    def __post_init__(self):
        if not self.container_path and not self.host_path:
            raise AttributeError('need at least one of host_path and container_path')
        if not self.container_path:
            object.__setattr__(self, 'container_path', self.host_path)
        if not self.host_path:
            object.__setattr__(self, 'host_path', self.container_path)

    @classmethod
    def from_string(cls, s: str) -> 'JobStorage':
        return cls(container_path=s, host_path=s)


def _convert_portmappings(pm_list: List):
    if not pm_list:
        return pm_list
    res = []
    for pm in pm_list:
        if isinstance(pm, int):
            res.append(JobPortMapping(container_port=pm, host_port=None))
        else:
            assert isinstance(pm, dict)
            res.append(JobPortMapping.from_dict(pm))
    return res


def _convert_storage(storage_list: List):
    if not storage_list:
        return storage_list
    res = []
    for s in storage_list:
        if isinstance(s, str):
            res.append(JobStorage(container_path=s, host_path=s))
        else:
            assert isinstance(s, dict)
            res.append(JobStorage.from_dict(s))
    return res

# def _pre_process_portmappings(pm_list: List):
#     if not pm_list:
#         return pm_list
#     res = []
#     for pm in pm_list:
#         if isinstance(pm, int):
#             res.append(JobPortMapping(container_port=pm, host_port=None))
#         else:
#             assert isinstance(pm, dict)
#             res.append(pm)
#     return res
#
#
# def _pre_process_storage(storage_list: List):
#     if not storage_list:
#         return storage_list
#     res = []
#     for s in storage_list:
#         if isinstance(s, str):
#             res.append(JobStorage(container_path=s, host_path=s))
#         else:
#             assert isinstance(s, dict)
#             res.append(s)
#     return res


# @dataclass_json_pre_modify_dict_field(modifier_by_fieldname={'port_mappings': _pre_process_portmappings, 'storage': _pre_process_storage})
@dataclass_dict_convert(dict_letter_case=camelcase,
    direct_fields=['command', 'environment'],
    custom_from_dict_convertors={
        'group_add': create_wrap_in_list_from_convertor(str),
        'port_mappings': _convert_portmappings,
        'storage': _convert_storage,
    },)
@dataclass(frozen=True)
@dataclass_auto_type_check
@dataclass_copy_method
@dataclass_multiline_repr
class JobRequestDocker:
    image: str
    # A single command not in a list has a different meaning than a single command in a list (!):
    #   In the 1st case, the command can includes spaces and is processed like a shell
    #   In the 2nd case, the first element is the executable and the other the literal arguments
    # Note that dockerpy container.run directly accepts the same 2 types of arguments in the same way
    command: Union[str, List[str]] = field(default_factory=list)
    environment: dict = field(default_factory=dict)
    storage: List[JobStorage] = field(default_factory=list)
    port_mappings: List[JobPortMapping] = field(default_factory=list)
    project_gid_variable_name: Optional[str] = None
    # user_uid_variable_name: Optional[str] = None  # deprecated
    working_dir: Optional[str] = None
    group_add: List[str] = field(default_factory=list)
    user: Optional[str] = None

    def __post_init__(self):
        _test_char_list(self.command, 'Job.request.docker.command', dont_allow_any_single_char=False)
        _test_char_list(self.group_add, 'Job.request.docker.group_add', dont_allow_any_single_char=False)

    @property
    def image_nopass(self) -> str:
        res = self.image
        match = DOCKER_IMAGE_USERPASS_PATTERN.match(res)
        if match:
            return "{}:XXXX@{}".format(match.group(1), match.group(3))
        else:
            return res

    @property
    def command_as_str(self) -> Optional[str]:
        if not self.command:
            return None
        if isinstance(self.command, str):
            return self.command
        return ' '.join(self.command)

    def sanitized_copy(self, logged_in=True, same_project=False) -> 'JobRequestDocker':
        if logged_in and same_project:
            return JobRequestDocker(
                image=self.image_nopass,  # password is stipped from docker image if shown to project members
                command=self.command,
                environment=self.environment,
                storage=self.storage,
                port_mappings=self.port_mappings,
                project_gid_variable_name=self.project_gid_variable_name,
                working_dir=self.working_dir,
                group_add=self.group_add,
                user=self.user,
            )
        else:
            return JobRequestDocker(
                image='hidden',
                command=[],
                environment={},
                storage=[],
                port_mappings=[],
                project_gid_variable_name=None,
                working_dir=None,
                group_add=[],
                user=None,
            )


# @dataclass_json_hack_nested_from_dict  # needed for JobRequestResources and JobRequestDocker
@dataclass_dict_convert(dict_letter_case=camelcase)
@dataclass(frozen=True)
@dataclass_auto_type_check
@dataclass_copy_method
@dataclass_multiline_repr
class JobRequest:
    resources: JobRequestResources
    docker: JobRequestDocker
    scheduling: JobRequestScheduling = field(default_factory=JobRequestScheduling)
    extra: JobRequestExtra = field(default_factory=JobRequestExtra)

    def sanitized_copy(self, logged_in=True, same_project=False) -> 'JobRequest':
        """copy with removed confidential data
        :param logged_in: sanitized copy for logged in user, or for anonymous user?
        :param same_project: sanitized copy for user in same project, or for someone else?
        """
        copy = JobRequest(
            resources=self.resources.sanitized_copy(logged_in, same_project),
            docker=self.docker.sanitized_copy(logged_in, same_project),
            scheduling=self.scheduling.sanitized_copy(logged_in, same_project),
            extra=self.extra.sanitized_copy(logged_in, same_project),
        )
        return copy


@dataclass_dict_convert(dict_letter_case=camelcase)
@dataclass(frozen=True)
@dataclass_auto_type_check
@dataclass_copy_method
@dataclass_multiline_repr
class JobOwner:
    user_urn: str
    user_email: str
    project_urn: str

    def __post_init__(self):
        if not is_valid_email(self.user_email):
            raise ValueError('Invalid user_email "{}"'.format(self.user_email))
        if not check_valid_urn_bytype(self.user_urn, 'user'):
            raise ValueError('Invalid user_urn "{}"'.format(self.user_urn))
        if not check_valid_urn_bytype(self.project_urn, 'project'):
            raise ValueError('Invalid project_urn "{}"'.format(self.project_urn))

    @property
    def userurn_auth(self):
        return urn_to_auth(self.user_urn)

    @property
    def userurn_name(self):
        return urn_to_name(self.user_urn)

    @property
    def user_mini_id(self):
        return urn_to_user_mini_id(self.user_urn)

    @property
    def project_name(self):
        if self.project_urn and self.project_urn.startswith('urn:'):
            return URN(urn=self.project_urn).name
        else:
            return None

    def is_partially_sanitized(self) -> bool:
        return self.project_urn == 'urn:publicid:IDN+hidden+project+hidden' or self.user_email == 'hidden@hidden.hidden'

    def sanitized_copy(self, logged_in=True, same_project=False) -> 'JobOwner':
        # hide the email address and project
        return dataclasses.replace(
            self,
            user_email='hidden@hidden.hidden',
            project_urn=self.project_urn if logged_in and same_project else 'urn:publicid:IDN+hidden+project+hidden'
        )

#
# State vs Status
#
#   -> in the english language: very related, and often synonyms
#   -> typically in technical language, state is used in a more broad sense, and status is more "one-dimensional"
#       -> thus you can have a state containing multiple statuses
#
#  Here:
#   -> in JobState we describe the entire variable state of the Job.
#      "status" holds the ID of the current discrete step in the Job's lifecycle ("the workflow of job execution")
#      so "lifecycle_step" or "workflow_position" would be a synonym for our "status", but both feels too convoluted
#
@dataclass_dict_convert(dict_letter_case=camelcase)
@dataclass(frozen=True)
@dataclass_auto_type_check
@dataclass_copy_method
@dataclass_multiline_repr
class JobState:
    status: JobStatus  # The ID of the current step in the Job's lifecycle
    scheduling: JobStateScheduling  # mandatory, but content can all be None
    event_times: JobEventTimes  # mandatory, but content can be empty
    resources: Optional[JobStateResources] = None  # only filled in once job is at least STARTING
    final_usage_statistics: Optional[GPULabUsageStatistics] = None

    # updatable fields: FIELDNAME_PORT_MAPPINGS, FIELDNAME_GPU_INFO, FIELDNAME_END_DATE, FIELDNAME_SUMMARY_STATISTICS

    def sanitized_copy(self, logged_in=True, same_project=False) -> 'JobState':
        # most is public here
        return JobState(
            status=self.status,
            resources=self.resources.sanitized_copy(logged_in, same_project) if self.resources else None,
            scheduling=self.scheduling.sanitized_copy(logged_in, same_project),
            event_times=self.event_times.sanitized_copy(logged_in, same_project),
            final_usage_statistics=self.final_usage_statistics.make_copy() if self.final_usage_statistics and logged_in else None,
        )

    def make_compatible_with(self, gpulab_api_version: str) -> 'JobState':
        """
        Return a version of this that is backwards compatible with version 3.X.
        :param gpulab_api_version: version to be compatible with.
        :return:
        """
        if gpulab_api_version == '3.1':
            return self
        else:
            assert gpulab_api_version == '3.0'
            return JobState(
                status=self.status,
                resources=self.resources,
                scheduling=self.scheduling.make_compatible_with(gpulab_api_version),
                event_times=self.event_times,
                final_usage_statistics=self.final_usage_statistics,
            )


# @dataclass_json_hack_nested_from_dict  # needed for JobRequest.JobRequestResources and JobRequest.JobRequestDocker
@dataclass_dict_convert(dict_letter_case=camelcase)
@dataclass(frozen=True)
@dataclass_auto_type_check
@dataclass_copy_method
@dataclass_multiline_repr
class Job:
    # Note: Job ID is a 36 char UUID4 (thus including the hyphens)
    name: str
    deployment_environment: str
    request: JobRequest
    uuid: Optional[str] = None
    description: Optional[str] = None
    # Note: Owner is mandatory, except for the Job specified by the user.
    #       The client will add the owner info based on the PEM and specified project,
    #       before sending the Job to GPULab master.
    #       GPULab will check the JobOwner user against the authorized URN
    owner: Optional[JobOwner] = None
    state: Optional[JobState] = None

    def __post_init__(self):
        if self.uuid and not is_valid_job_id(self.uuid):
            raise ValueError('Invalid Job UUID "{}"'.format(self.uuid))

    # backward compatible check if job is "stable" aka "production"
    @property
    def is_production(self) -> bool:
        return self.deployment_environment in ['stable', 'prod', 'production']

    def replace_event_times_attrs(self, **kwargs):
        assert self.state
        new_event_times = dataclasses.replace(self.state.event_times, **kwargs)
        new_state = dataclasses.replace(self.state, event_times=new_event_times)
        return dataclasses.replace(self, state=new_state)

    def replace_request_extra_attrs(self, **kwargs):
        assert self.request and self.request.extra
        new_extra = dataclasses.replace(self.request.extra, **kwargs)
        new_request = dataclasses.replace(self.request, extra=new_extra)
        return dataclasses.replace(self, request=new_request)

    def replace_owner_attrs(self, **kwargs):
        if self.owner:
            new_owner = dataclasses.replace(self.owner, **kwargs)
            return dataclasses.replace(self, owner=new_owner)
        else:
            return dataclasses.replace(self, owner=JobOwner(**kwargs))

    def replace_state_scheduling(self, new_scheduling: JobStateScheduling):
        assert self.state
        new_state = dataclasses.replace(self.state, scheduling=new_scheduling)
        return dataclasses.replace(self, state=new_state)

    def replace_state_scheduling_attrs(self, **kwargs):
        assert self.state
        new_scheduling = dataclasses.replace(self.state.scheduling, **kwargs)
        new_state = dataclasses.replace(self.state, scheduling=new_scheduling)
        return dataclasses.replace(self, state=new_state)

    def replace_state_final_usage_statistics(self, final_usage_statistics: GPULabUsageStatistics):
        assert self.state
        new_state = dataclasses.replace(self.state, final_usage_statistics=final_usage_statistics)
        return dataclasses.replace(self, state=new_state)

    def replace_state_resources(self, new_resources: JobStateResources):
        assert self.state
        new_state = dataclasses.replace(self.state, resources=new_resources)
        return dataclasses.replace(self, state=new_state)

    def replace_state_resources_fields(self, **kwargs):
        assert self.state
        new_resources = dataclasses.replace(self.state.resources, **kwargs)
        new_state = dataclasses.replace(self.state, resources=new_resources)
        return dataclasses.replace(self, state=new_state)

    def sanitized_copy(self, logged_in=True, same_project=False) -> 'Job':
        """copy with removed confidential data
        :param logged_in: sanitized copy for logged in user, or for anonymous user?
        :param same_project: sanitized copy for user in same project, or for someone else?
        """
        copy = Job(
            uuid=self.uuid,
            name=self.name if same_project or self.name == 'JupyterHub-singleuser' else ('job-'+self.uuid[:6] if self.uuid else 'job'),
            deployment_environment=self.deployment_environment,
            request=self.request.sanitized_copy(logged_in, same_project),
            description=self.description if logged_in and same_project else None,
            owner=self.owner.sanitized_copy(logged_in, same_project),
            state=self.state.sanitized_copy(logged_in, same_project)
        )
        return copy

    def make_compatible_with(self, gpulab_api_version: Optional[str]) -> 'Job':
        """
        Return a version of this job that is backwards compatible with version 3.X.
        :param gpulab_api_version: version to be compatible with. If None, 3.0 is assumed.
        :return:
        """
        if gpulab_api_version == '3.1':
            return self
        else:
            return Job(
                uuid=self.uuid,
                name=self.name,
                deployment_environment=self.deployment_environment,
                request=self.request,
                description=self.description,
                owner=self.owner,
                state=self.state.make_compatible_with('3.0')
            )

    def is_fully_sanitized(self) -> bool:
        return self == self.sanitized_copy()

    def is_partially_sanitized(self) -> bool:
        """
        :return: True if this job is at least partially sanitized
        """
        return self.is_fully_sanitized() or \
               self.owner.is_partially_sanitized() or \
               self.request.docker.image == 'hidden'

    def get_backward_compat_version(self):
        if self.deployment_environment == 'staging':
            return 'dev'
        if self.deployment_environment in ['production', 'prod']:
            return 'stable'
        return self.deployment_environment

    @property
    def short_uuid(self) -> Optional[str]:
        if not self.uuid:
            return None
        if '-' in self.uuid:
            return self.uuid[:self.uuid.index('-')]
        return self.uuid
