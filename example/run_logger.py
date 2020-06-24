import asyncio
import logging
import time

import aiohttp

from ws_logging.handlers.using_websockets_lib import WebsocketsHandler
from ws_logging.handlers.using_aiohttp import AiohttpHandler


# logging.getLogger().setLevel("DEBUG")

logging_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(
#     logging.Formatter("stream_handler - " + logging_format)
# )
# logger.addHandler(stream_handler)


def log_stuff(n_times=1):
    for i in range(n_times):
        logger.debug(f"wow {i}")
        logger.info(f"wheeee {i}")
        logger.warning(f"whoa!! {i}")
        logger.error(f"ooo {i}")
        logger.critical(f"yeah {i}")


async def log_with_ws_handler():
    logger.debug("make WebsocketsHandler")
    t = time.perf_counter()
    handler = await WebsocketsHandler.from_info("127.0.0.1", 8080, "ws")
    print("make handler", time.perf_counter() - t)
    handler.setFormatter(
        logging.Formatter("WebsocketsHandler - " + logging_format)
    )
    logger.addHandler(handler)
    t = time.perf_counter()
    log_stuff(1000)
    print("log_stuff()", time.perf_counter() - t)
    t = time.perf_counter()
    await handler.stop()
    print("handler.stop()", time.perf_counter() - t)


async def log_with_aiohttp_handler():
    t = time.perf_counter()
    handler = await AiohttpHandler.from_info("127.0.0.1", 8080, "ws")
    print("make handler", time.perf_counter() - t)
    handler.setFormatter(
        logging.Formatter("AiohttpHandler - " + logging_format)
    )
    logger.addHandler(handler)
    t = time.perf_counter()
    log_stuff(1000)
    print("log_stuff()", time.perf_counter() - t)
    t = time.perf_counter()
    await handler.stop()
    print("handler.stop()", time.perf_counter() - t)


async def test_aiohttp_client():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect("ws://127.0.0.1:8080/ws") as ws:
            await ws.send_str("hello, world!")


loop = asyncio.get_event_loop()
# loop.run_until_complete(test_aiohttp_client())
# loop.run_until_complete(log_with_aiohttp_handler())

t = time.time()
print("start")
# loop.run_until_complete(test_aiohttp_client())
loop.run_until_complete(log_with_ws_handler())
# loop.run_until_complete(log_with_aiohttp_handler())
print("total time:", time.time() - t)
print(len(asyncio.all_tasks(loop)))
