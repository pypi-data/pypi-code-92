import logging
import sys
import json

from electrumsv_sdk.app_state import AppState  # pylint: disable=E0401
from electrumsv_sdk.constants import NameSpace, read_config_json, LOG_LEVEL

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(name)-24s %(message)s',
    level=LOG_LEVEL, datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger("main")
logger_requests = logging.getLogger("urllib3")
logger_requests.setLevel(logging.WARNING)


def main() -> None:
    """
    Command-line interface for the ElectrumSV Software Development Kit

    The argparser module does not seem to naturally support the use of
    multiple subcommands simultaneously (which we need to support). This is handled
    manually by parsing sys.argv and feeding the correct options to the correct
    ArgumentParser instance (for the given subcommand). So in the end we get both
    a) the help menu interface via built-in argparser module
    b) the ability to string multiple subcommands + optional args together into a single cli
    command.
    """
    app_state = AppState(sys.argv)
    app_state.handle_first_ever_run()
    if app_state.config.sdk_home_dir:
        app_state.maybe_update_sdk_home_dir()

    # Call relevant entrypoint
    if app_state.config.namespace == NameSpace.INSTALL:
        # -> install() entrypoint of plugin
        app_state.controller.install(app_state.config)

    if app_state.config.namespace == NameSpace.START:
        # -> start() -> status_check() entrypoint of plugin
        app_state.controller.start(app_state.config)

    if app_state.config.namespace == NameSpace.STOP:
        # -> stop() entrypoint of plugin
        app_state.controller.stop(app_state.config)

    if app_state.config.namespace == NameSpace.RESET:
        # -> reset() entrypoint of plugin
        app_state.controller.reset(app_state.config)

    # Special built-in execution pathway (not part of plugin system)
    if app_state.config.namespace == NameSpace.NODE:
        app_state.controller.node(app_state.config)

    # Http 'GET' request to status_monitor (which itself is a plugin component of the SDK)
    if app_state.config.namespace == NameSpace.STATUS:
        app_state.controller.status(app_state.config)

    if app_state.config.namespace == NameSpace.CONFIG:
        print(f"config json:")
        print(json.dumps(read_config_json(), indent=4))


if __name__ == "__main__":
    main()
