''' Configuration file manipulator '''

# Standard Imports
import yaml

# Third Party Imports
# None

# Local Imports
from pydungeon import logger

# Decorator for adding dict config to classes
def dictionary_transform(cls):
    # Modify the class attributes
    def asdict(self):
        result_dict = {}
        for key,value in self.__dict__.items():
            if not callable(key):
                result_dict[key] = value

        return result_dict

    def fromdict(self, data_dict):
        self.__dict__.update(data_dict)

    setattr(cls, 'asdict', asdict)
    setattr(cls, 'fromdict', fromdict)

    return cls


class Config(object):
    def __init__(self, config_name):
        self._config_name = config_name

    def load(self):
        with open(self._config_name, 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as error:
                logger.error(f'Could Not Load YAML File {self._config_name}', exc_info=True)

    def save(self, data):
        with open(self._config_name, 'w') as stream:
            try:
                return yaml.dump(data, stream)
            except yaml.YAMLError as error:
                logger.error(f'Could Not Save YAML File {self._config_name}', exc_info=True)


        
