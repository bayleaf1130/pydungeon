import logging

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('pydungeon.log')
stream_handler = logging.StreamHandler()

stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

stream_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_handler.setFormatter(stream_format)
file_handler.setFormatter(file_format)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)