import asyncio
import statistics
import time
import websockets


async def hello():
    uri = "ws://localhost:8765"
    n = 1000
    durations_send = list(range(n))
    durations_send_await = list(range(n))
    durations_recv = list(range(n))
    async with websockets.connect(uri) as websocket:
        name = "william"  # input("What's your name? ")
        name = "w" * int(2e6)
        for i in durations_send:
            start = time.perf_counter()
            f = websocket.send(name)
            durations_send[i] = time.perf_counter() - start

            start = time.perf_counter()
            await f
            durations_send_await[i] = time.perf_counter() - start

            start = time.perf_counter()
            await websocket.recv()
            durations_recv[i] = time.perf_counter() - start

    def print_stuff(stuff):
        print(f"mean:   {statistics.mean(stuff):.8f}")
        print(f"median: {statistics.median(stuff):.8f}")

    print_stuff(durations_send)
    print_stuff(durations_send_await)
    print_stuff(durations_recv)


asyncio.get_event_loop().run_until_complete(hello())
