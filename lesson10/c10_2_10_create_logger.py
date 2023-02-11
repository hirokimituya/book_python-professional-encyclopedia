import logging

formatter = '%(asctime)s: [%(levelname)s] - %(filename)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)

logging.info('info %s %s', 'test', 'test2')
