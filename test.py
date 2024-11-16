from exception import SensorException
from logger import logging
import sys

try:
    a = 10/4
    logging.info("This is for info")
    logging.warning("This is for warning")
except Exception as e:
    logging.info('exception is there')
    raise SensorException(e,sys) from e