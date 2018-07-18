import logging


def setLogger(self):
    self.logger = logging.getLogger('something')
    # myFormatter = logging.Formatter(
    #    'findNodes -- %(asctime)s - %(message)s')

    # Add the name
    myFormatter = logging.Formatter(
        self.logPrefix + ' - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(myFormatter)
    self.logger.addHandler(handler)
    self.logger.setLevel(logging.INFO)
    self.info = self.logger.info
