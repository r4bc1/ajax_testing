import asyncio
import websockets
import json


async def main():
    async with websockets.connect("ws://localhost:2707") as socket:
        REQ ={"request_id":"01",
              "data": r"Hub&&name&&qwe&&id&&123&&%%Device&&name&&wqe&&id&&234&&nick&&romashka"}
        await socket.send(json.dumps(REQ))
        print(await socket.recv())


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
