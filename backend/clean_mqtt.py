#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import paho.mqtt.client as mqtt  # import the client1
import asyncio
import websockets
import configparser
import traceback
import models
import json
import sys, traceback
import mongo_models

config = configparser.ConfigParser()
config.read('config.ini')
db = models.Models()
cnv = models.Convert()
MM = mongo_models.Mongo_Models()

############
class mqtt_data():

    async def hello(self, uri, msg):
        async with websockets.connect(uri) as websocket:
            await websocket.send(msg)
            reply = await websocket.recv()
            print(f">", reply)

    def on_connect(self, client):
        print("CONNECTION ESTABLISHED")

    def on_message(self, client, userdata, message):

        self.ws_host = config['WEBSOCKET']['ws_host']
        self.ws_port = config['WEBSOCKET']['ws_port']

        message = str(message.payload.decode("utf-8"))
        server = "ws://"+str(self.ws_host)+':'+str(self.ws_port)
        if message:
            try: 
                print(message)               
                # asyncio.set_event_loop(asyncio.new_event_loop())
                # ulang = asyncio.get_event_loop()
                # ulang.run_until_complete(self.hello(server, message))
                # ulang.close()
                # db.insert_raw(message)
                # MM.insert_raw(json.loads(message))                
                # data = cnv.format_data_stream(message)                
                # if data:
                #     db.insert_stream(data)
                # self.cek_genset(data)
            except Exception as e:
                global loop
                loop = False
                print("ERROR : ", e)
                traceback.print_exc(file=sys.stdout)
                pass
                
    
    def cek_genset(self, data):
        
        
        info = []
        datas = {}
        
        try:
            
            info = db.get_genset_data(data['Id'])                        
            if info is None:                
                datas['Id'] = data['Id']
                datas['name'] = None
                datas['detail'] = None
                datas['tank_capacity'] = None
                datas['displacement'] = None
                datas['starting_system'] = None
                datas['design_features'] = None
                datas['full_load_consumption'] = None
                datas['three_quarter_load_consumption'] = None
                datas['half_load_consumption'] = None
                datas['quarter_load_consumption'] = None
                datas['bore_stroke'] = None
                datas['continuous_rated_output'] = None
                datas['voltage_allowance'] = None
                db.insert_genset(datas)

        except Exception as e :
            print(e)
            traceback.print_exc(file=sys.stdout)
            pass

    def __init__(self):
        self.broker_address = config['MQTT']['mqtt_broker']
        self.port = int(config['MQTT']['mqtt_port'])
        self.topic = config['MQTT']['topic']
        self.user = config['MQTT']['username']
        self.password = config['MQTT']['password']

        try:
            client = mqtt.Client("Pusher_2", transport="tcp")  # create new instance
            client.on_connect = self.on_connect
            client.on_message = self.on_message  # attach function to callback

            client.username_pw_set(self.user, password=self.password)
            # connect to broker
            client.connect(self.broker_address, port=self.port)
            client.loop_start()  # start the loop

            client.subscribe(self.topic)
            time.sleep(1)  # wait
            client.loop_stop()  # stop the loop
            client.disconnect()
        except Exception as e:
            print("E R R O R : ", e)
            traceback.print_exc(file=sys.stdout)
            pass
            #exit()


########################################

loop = True

if __name__ == "__main__":
    try:
        print("__ S T A R T __")
        while loop:
            mqtt_data()

    except KeyboardInterrupt:
        loop = False
        print("Keyboard Interrupt exiting")
        exit()
