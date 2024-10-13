import configparser


def get_ai_attitude_from_file():
    config = configparser.ConfigParser()
    config.read('config.ini')
    ai_attitude = config.get('ai','ai_attitude')
    return ai_attitude