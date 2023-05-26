'''
    Just a reminder for logging message
'''
import logging

logging.basicConfig(filename="logfile.txt", level=logging.WARNING)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')