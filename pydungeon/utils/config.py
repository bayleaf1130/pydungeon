''' Configuration file manipulator '''

# Standard Imports
import yaml

# Third Party Imports
# None

# Local Imports
from pydungeon import logger

class CharacterConfig(object):
    def __init__(self, config_name):
        self._config_name = config_name

    def load(self):
        with open(self._config_name, 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as error:
                logger.error(f'Could Not Load YAML File {self._config_name}', exc_info=True)

    def save(self, character):
        with open(self._config_name, 'w') as stream:
            try:
                return yaml.dump(character, stream)
            except yaml.YAMLError as error:
                logger.error(f'Could Not Save YAML File {self._config_name}', exc_info=True)


        