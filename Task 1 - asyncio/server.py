import asyncio
import websockets
import json
import random


def make_response(data):
    data_dict = json.loads(data)
    big_ugly_data_string = data_dict["data"].split(r"%%")
    request_id = data_dict["request_id"]
    RESP = {"request_id": request_id, "data": dict()}

    for entity_block in big_ugly_data_string:
        elements = entity_block.split("&&")
        device = elements[0]
        RESP["data"][device] = dict()
        zock = 0
        for i in range(1, len(elements)):
            if zock % 2 != 0 and elements[i]:
                RESP["data"][device][elements[i - 1]] = elements[i]
            zock += 1
    return json.dumps(RESP)


async def response(websocket, path):
    data = await websocket.recv()
    RESP = make_response(data)
    sleep_time = round(random.choice(range(100, 600)) / 100, 2)
    await asyncio.sleep(sleep_time)
    word = random.choice(["this", "another", "that"])
    print("Timeout", sleep_time,"seconds for {} one.".format(word))
    await websocket.send(RESP)


if __name__ == '__main__':
    start_server = websockets.serve(response, 'localhost', 2707)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
