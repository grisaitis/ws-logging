import asyncio
import logging

import aiohttp


class AiohttpHandler(logging.StreamHandler):
    terminator = ""
    stream = None

    def __init__(
        self,
        session: aiohttp.ClientSession,
        ws: aiohttp.ClientWebSocketResponse,
    ):
        super().__init__()
        self.session = session
        self.ws = ws
        self._unawaited_tasks = set()

    @classmethod
    async def from_info(cls, host: str, port: int, path: str):
        url = f"ws://{host}:{port}/{path}"
        session = aiohttp.ClientSession()
        ws = await session._ws_connect(url)
        return cls(session, ws)

    def emit(self, record: logging.LogRecord):
        msg = self.format(record)
        task = asyncio.create_task(self.ws.send_str(msg))
        self._unawaited_tasks.add(task)

    async def stop(self):
        await asyncio.wait(self._unawaited_tasks)
        await self.session.close()
