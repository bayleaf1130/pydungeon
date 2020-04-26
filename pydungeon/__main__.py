import sys

from pydungeon import logger

def main(sysargs):
    print('In Main')
    logger.warning('ERROR')
    logger.error('HELP')


if __name__ == '__main__':
    sys.exit(main(None))