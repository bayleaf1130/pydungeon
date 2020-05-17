''' Configuration file manipulator '''

# Standard Imports
import yaml

# Third Party Imports
# None

# Local Imports
from pydungeon import logger


class Config(object):
    def __init__(self, config_name):
        self._config_name = config_name

    def load(self):
        with open(self._config_name, 'r') as stream:
            try:
                return yaml.load(stream, Loader=yaml.FullLoader)
            except yaml.YAMLError as error:
                logger.error(f'Could Not Load YAML File {self._config_name}', exc_info=True)

    def save(self, data):
        with open(self._config_name, 'w') as stream:
            try:
                return yaml.dump(data, stream)
            except yaml.YAMLError as error:
                logger.error(f'Could Not Save YAML File {self._config_name}', exc_info=True)



