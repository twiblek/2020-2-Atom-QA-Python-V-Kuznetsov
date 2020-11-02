import os
import pytest
import logging
import datetime

from models.models import Logs

class LogDBHandler(logging.Handler):
    def __init__(self, session):
        logging.Handler.__init__(self)
        self.session = session

    def emit(self, record):
        log = Logs(
            asctime = datetime.datetime.now(),
            levelname = record.levelname,
            levelno = record.levelno,
            message = record.msg,
            name = record.name
            )

        self.session.add(log)
        self.session.commit()

def logger(session):
    log = logging.getLogger('db_logger')
    log.setLevel(logging.DEBUG)
    log.addHandler(LogDBHandler(session))
    return log