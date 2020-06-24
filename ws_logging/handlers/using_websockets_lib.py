import asyncio
import logging

import websockets


class WebsocketsHandler(logging.StreamHandler):
    terminator = ""
    stream = None

    def __init__(self, ws_client: websockets.WebSocketClientProtocol):
        super().__init__()
        self.ws_client = ws_client
        self._unawaited_tasks = set()

    @classmethod
    async def from_info(cls, host: str, port: int, path: str = "ws"):
        uri = f"ws://{host}:{port}/{path}"
        ws_client = await websockets.connect(uri)
        return cls(ws_client=ws_client)

    def emit(self, record: logging.LogRecord):
        msg = self.format(record)
        task = asyncio.create_task(self.ws_client.send(msg))
        self._unawaited_tasks.add(task)

    async def stop(self):
        await asyncio.wait(self._unawaited_tasks)
        await self.ws_client.close()
