import asyncio
import logging
from pprint import pprint

from ws_logging.handlers.using_websockets_lib import WebsocketsHandler
from ws_logging.handlers.using_aiohttp import AiohttpHandler


root = logging.getLogger()
root.setLevel("DEBUG")
# logging.getLogger("ws_logging").setLevel("DEBUG")
# pprint(logging.root.manager.loggerDict)

# formatter = logging.Formatter(logging.BASIC_FORMAT)
logging_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")
print(logger.level)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(
    logging.Formatter("stream_handler - " + logging_format)
)
logger.addHandler(stream_handler)


def log_stuff():
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")


async def log_with_ws_handler():
    logger.debug("make WebsocketsHandler")
    handler = await WebsocketsHandler.from_server_string(
        "127.0.0.1", 8080, "ws"
    )
    handler.setFormatter(logging.Formatter("ws_handler - " + logging_format))
    logger.addHandler(handler)
    log_stuff()
    await handler.stop()


async def log_with_aiohttp_handler():
    handler = AiohttpHandler("127.0.0.1", 8080, "ws")
    handler.setFormatter(
        logging.Formatter("aiohttp_handler - " + logging_format)
    )
    logger.addHandler(handler)
    log_stuff()


# asyncio.run(log_with_ws_handler())
asyncio.run(log_with_aiohttp_handler(), debug=True)
