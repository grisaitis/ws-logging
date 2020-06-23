import asyncio
import logging

import websockets

logger = logging.getLogger(__name__)


class WebsocketsHandler(logging.StreamHandler):
    terminator = ""
    stream = None

    def __init__(self, ws_client: websockets.WebSocketClientProtocol):
        super().__init__()
        self.ws_client = ws_client

    @classmethod
    async def from_server_string(cls, host, port, path="ws"):
        uri = f"ws://{host}:{port}/{path}"
        logger.debug(f"call websockets.connect with {uri}")
        ws_client = await websockets.connect(uri)
        logger.debug(f"connection: {repr(ws_client)}")
        return cls(ws_client=ws_client)

    def emit(self, record: logging.LogRecord):
        msg = self.format(record)
        asyncio.create_task(self.ws_client.send(msg))

    async def stop(self):
        await self.ws_client.close()
