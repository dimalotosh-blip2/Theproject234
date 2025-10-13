import logging

logging.basicConfig(
    filename='system_log.txt',
    filemode='a',
    level=logging.DEBUG,
    format='>> %(levelname)s | %(asctime)s | %(message)s'
)

logging.info('Start working...')
logging.error('Some file is missing, maybe deleted')
logging.debug('Checking system status...')
logging.critical('Something really bad just happened!')

