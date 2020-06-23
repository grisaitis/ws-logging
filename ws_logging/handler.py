import logging
import logging.handlers


class WebSocketHandler1(logging.Handler):
    def __init__(self, websocket_connection):
        super().__init__()
        self.websocket_connection = websocket_connection

    def emit(self, record):
        # await self.websocket_connection
        pass


class WebSocketHandler2(logging.handlers.StreamHandler):
    def __init__(self, websocket_connection):
        super().__init__()
        self.websocket_connection = websocket_connection
