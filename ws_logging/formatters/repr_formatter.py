import logging


class ReprLogRecordFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord):
        return repr(record)
