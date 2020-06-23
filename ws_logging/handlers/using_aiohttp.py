import asyncio
import logging

import aiohttp

logger = logging.getLogger(__name__)

"""
helpful links
- docs: https://docs.aiohttp.org/en/stable/client_quickstart.html#websockets

questions
- does aiohttp have a connection interface that isn't a context manager?

"""


class AiohttpHandler(logging.StreamHandler):
    def __init__(self, host, port, path="ws"):
        super().__init__()  # should i put stream=None?
        self.host = host
        self.port = port
        self.path = path  # is path the correct name here?
        self.url = f"ws://{host}:{port}/{path}"

    async def send_msg_async(self, msg: str):
        async with aiohttp.ClientSession() as session:
            async with session.ws_connect(self.url) as ws:
                await ws.send_str(msg)

    def emit(self, record):
        msg = self.format(record)
        asyncio.create_task(self.send_msg_async(msg))
