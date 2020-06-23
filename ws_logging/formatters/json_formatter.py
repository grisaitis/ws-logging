import logging
import json


class JsonFormatter(logging.Formatter):
    def __init__(self, datefmt=None, **json_dumps_kwargs):
        super().__init__(datefmt=datefmt)
        self.json_dumps_kwargs = json_dumps_kwargs

    def format(self, record: logging.LogRecord):
        return json.dumps(record.__dict__, **self.json_dumps_kwargs)
