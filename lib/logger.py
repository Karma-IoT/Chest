import logging

logging.basicConfig(level = logging.INFO,format='%(asctime)s %(message)s',datefmt='%Y-%m-%d %H:%M:%S')

def info(msg, *args, **kwargs):
    logging.info('-- [KBT] ' + msg, *args, **kwargs)

