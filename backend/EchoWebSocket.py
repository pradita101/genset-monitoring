#!/usr/bin/python3
# -*- coding: utf-8 -*-

import asyncio
import websockets
import configparser
import io
import sys, traceback

config = configparser.ConfigParser()
config.read('config.ini')
host = ''
port = str(config['WEBSOCKET']['ws_port'])

connected = set()


async def echo(websocket, path):
    # Register.
    connected.add(websocket)
    try:
        message = await websocket.recv()
        print(f"< {message}")
        await asyncio.wait([ws.send(message) for ws in connected])
        await asyncio.sleep(1)
    except Exception as e:
        print("Error from def echo : ",e)
    finally:
        connected.remove(websocket)


if __name__ == '__main__':
    try:
        print("__ S T A R T__")
        asyncio.set_event_loop(asyncio.new_event_loop())
        asyncio.get_event_loop().run_until_complete(
            websockets.serve(echo, host, port))
        asyncio.get_event_loop().run_forever()
    except Exception as e:
        print("Error : ", e)
        traceback.print_exc(file=sys.stdout)
        exit()
