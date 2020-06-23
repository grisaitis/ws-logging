import asyncio
import websockets


async def hello(websocket, path):
    while True:
        await websocket.recv()
        # print(f"< {name}")

        # greeting = f"Hello {name}!"
        greeting = "hello"

        await websocket.send(greeting)
        # print(f"> {greeting}")


start_server = websockets.serve(hello, "localhost", 8765, max_size=int(1e8))

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
