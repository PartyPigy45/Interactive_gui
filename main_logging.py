import logging 

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('main logger')

_handler = logging.FileHandler('main_logs.log')
_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s - %(asctime)s - %(message)s')

_handler.setFormatter(formatter)

logger.addHandler(_handler)