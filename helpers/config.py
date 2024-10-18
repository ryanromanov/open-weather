import configparser


def get_ai_attitude_from_file() -> str:
    """
     reads the config.ini file and grabs the ai_attitude property

    :return: the ai_attitude as a string
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config.get('ai', 'ai_attitude')
