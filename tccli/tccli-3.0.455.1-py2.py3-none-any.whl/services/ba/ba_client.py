# -*- coding: utf-8 -*-
import os
import json
import tccli.options_define as OptionsDefine
import tccli.format_output as FormatOutput
from tccli import __version__
from tccli.utils import Utils
from tccli.exceptions import ConfigurationError
from tencentcloud.common import credential
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.ba.v20200720 import ba_client as ba_client_v20200720
from tencentcloud.ba.v20200720 import models as models_v20200720


def doSyncIcpOrderWebInfo(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BaClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SyncIcpOrderWebInfoRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.SyncIcpOrderWebInfo(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateWeappQRUrl(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BaClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateWeappQRUrlRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.CreateWeappQRUrl(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeGetAuthInfo(args, parsed_globals):
    g_param = parse_global_arg(parsed_globals)

    cred = credential.Credential(
        g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey], g_param[OptionsDefine.Token]
    )
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.BaClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeGetAuthInfoRequest()
    model.from_json_string(json.dumps(args))
    rsp = client.DescribeGetAuthInfo(model)
    result = rsp.to_json_string()
    try:
        json_obj = json.loads(result)
    except TypeError as e:
        json_obj = json.loads(result.decode('utf-8'))  # python3.3
    FormatOutput.output("action", json_obj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


CLIENT_MAP = {
    "v20200720": ba_client_v20200720,

}

MODELS_MAP = {
    "v20200720": models_v20200720,

}

ACTION_MAP = {
    "SyncIcpOrderWebInfo": doSyncIcpOrderWebInfo,
    "CreateWeappQRUrl": doCreateWeappQRUrl,
    "DescribeGetAuthInfo": doDescribeGetAuthInfo,

}

AVAILABLE_VERSION_LIST = [
    "v20200720",

]


def action_caller():
    return ACTION_MAP


def parse_global_arg(parsed_globals):
    g_param = parsed_globals

    is_exist_profile = True
    if not parsed_globals["profile"]:
        is_exist_profile = False
        g_param["profile"] = "default"

    configure_path = os.path.join(os.path.expanduser("~"), ".tccli")
    is_conf_exist, conf_path = Utils.file_existed(configure_path, g_param["profile"] + ".configure")
    is_cred_exist, cred_path = Utils.file_existed(configure_path, g_param["profile"] + ".credential")

    conf = {}
    cred = {}

    if is_conf_exist:
        conf = Utils.load_json_msg(conf_path)
    if is_cred_exist:
        cred = Utils.load_json_msg(cred_path)

    if not (isinstance(conf, dict) and isinstance(cred, dict)):
        raise ConfigurationError(
            "file: %s or %s is not json format"
            % (g_param["profile"] + ".configure", g_param["profile"] + ".credential"))

    if OptionsDefine.Token not in cred:
        cred[OptionsDefine.Token] = None

    if not is_exist_profile:
        if os.environ.get(OptionsDefine.ENV_SECRET_ID) and os.environ.get(OptionsDefine.ENV_SECRET_KEY):
            cred[OptionsDefine.SecretId] = os.environ.get(OptionsDefine.ENV_SECRET_ID)
            cred[OptionsDefine.SecretKey] = os.environ.get(OptionsDefine.ENV_SECRET_KEY)
            cred[OptionsDefine.Token] = os.environ.get(OptionsDefine.ENV_TOKEN)

        if os.environ.get(OptionsDefine.ENV_REGION):
            conf[OptionsDefine.Region] = os.environ.get(OptionsDefine.ENV_REGION)

    for param in g_param.keys():
        if g_param[param] is None:
            if param in [OptionsDefine.SecretKey, OptionsDefine.SecretId, OptionsDefine.Token]:
                if param in cred:
                    g_param[param] = cred[param]
                else:
                    raise ConfigurationError("%s is invalid" % param)
            elif param in [OptionsDefine.Region, OptionsDefine.Output]:
                if param in conf:
                    g_param[param] = conf[param]
                else:
                    raise ConfigurationError("%s is invalid" % param)

    try:
        if g_param[OptionsDefine.ServiceVersion]:
            g_param[OptionsDefine.Version] = "v" + g_param[OptionsDefine.ServiceVersion].replace('-', '')
        else:
            version = conf["ba"][OptionsDefine.Version]
            g_param[OptionsDefine.Version] = "v" + version.replace('-', '')

        if g_param[OptionsDefine.Endpoint] is None:
            g_param[OptionsDefine.Endpoint] = conf["ba"][OptionsDefine.Endpoint]
    except Exception as err:
        raise ConfigurationError("config file:%s error, %s" % (conf_path, str(err)))

    if g_param[OptionsDefine.Version] not in AVAILABLE_VERSION_LIST:
        raise Exception("available versions: %s" % " ".join(AVAILABLE_VERSION_LIST))

    return g_param

