import aiohttp


async def websocket_request_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                # await ws.send_str(msg.data + '/answer')
                print(msg.data)
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    print('websocket connection closed')

    return ws


if __name__ == "__main__":
    from aiohttp import web

    app = web.Application()
    app.add_routes([web.get('/ws', websocket_request_handler)])

    web.run_app(app)
