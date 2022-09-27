import logging


class Logger():


    def __init__(self, filename='/tmp/python.log'):
             logging.basicConfig(filename=filename, level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    def debug(self, text):
        return logging.debug(text)

    def info(self, text):
        return logging.info(text)

    def warning(self, text):
        return logging.warning(text)

    def error(self, text):
        return logging.error(text)

    def critical(self, text):
        return logging.critical(text)




