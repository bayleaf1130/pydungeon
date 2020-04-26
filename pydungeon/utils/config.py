""" Configuration file manipulator """
import yaml


class CharacterConfig(object):
    def __init__(self, config_name):
        self._config_name = config_name

    def load(self):
        with open(self._config_name, 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as error:
                raise RuntimeError('Could not load yaml')
        