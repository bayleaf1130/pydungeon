''' The main entry point '''

# Standard Imports
import sys

# Third Party Imports
# None

# Local Imports
from pydungeon import logger

def main(sysargs=None):
    print('In Main')
    logger.warning('ERROR')
    logger.error('HELP')


if __name__ == '__main__':
    sys.exit(main(None))