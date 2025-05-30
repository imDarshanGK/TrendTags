import json
import logging.config
import pathlib


def create_custom_logger(config_path: str) -> None:
    logging.getLogger(__name__)

    config_file = pathlib.Path(config_path)

    with open(config_file) as f_in:
        config = json.load(f_in)

    # Get the directory for logging as specified in the logging_config.json file to 
    # create the log directory if it does not exist. The filename in the config file 
    # must be only one folder deep from the root, such as "./logs/", however the 
    # directory name can be anything.
    log_directory = pathlib.Path(config["handlers"]["file"]["filename"].split("/")[0])
    if not log_directory.exists():
       log_directory.mkdir()

    logging.config.dictConfig(config)

    return None