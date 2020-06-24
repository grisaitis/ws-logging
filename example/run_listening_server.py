import logging

from aiohttp import web
import ws_logging
from ws_logging.listeners import aiohttp_ws_request_handler

handler = logging.StreamHandler()
handler.setFormatter(
    logging.Formatter(logging.BASIC_FORMAT)
    # ws_logging.formatters.JsonFormatter(indent=2, sort_keys=True)
)
logging.getLogger().addHandler(handler)
logging.getLogger().setLevel("DEBUG")
logging.getLogger("aiohttp").setLevel("WARNING")

logger = logging.getLogger(__name__)

app = web.Application()
app.add_routes([web.get("/ws", aiohttp_ws_request_handler)])

web.run_app(app)
