import configparser


def get_ai_attitude_from_file(config_file_name) -> str:
    """
     reads the config.ini file and grabs the ai_attitude property

    :return: the ai_attitude as a string
    """
    config = configparser.ConfigParser()
    config.read(config_file_name)
    return config.get('AI', 'ai_attitude')