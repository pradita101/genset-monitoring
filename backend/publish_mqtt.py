#!/usr/bin/python3
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt  # import the client1
import sys, traceback
import time
import datetime
import configparser
import random 
import json
import pymysql

config = configparser.ConfigParser()
config.read('config_local.ini')
broker_address = config['MQTT']['mqtt_broker']
port = int(config['MQTT']['mqtt_port'])
topic = config['MQTT']['topic']
user = config['MQTT']['username']
password = config['MQTT']['password']

# db_server = config['DB']['db_server']+":"+config['DB']['db_port']
db_server = config['DB']['db_server']
db_user = config['DB']['db_username']
db_password = config['DB']['db_pswrd']
db_name = config['DB']['db_name']

con = pymysql.connect(db_server, db_user, 
    db_password, db_name)

engine = ['ASI001','ASI002','ASI003','ASI004','ASI005','ASI006']

longitude = -5
latitude = 120

def create_message():
    msg = {}
    db_result = None
    # data_test = {"A":"DFXX","B":"1576563163","C":["-6.288","106.817","0.490","35.330"],"D":"1576563131","E":"1576563053","F":"131085","G":"-127.00","H":"0","I":"1","J":["4.84","5.19","4.26"],"K":["0.00","0.00","0.00"],"L":["0.00","0.00","0.00"],"M":"0.00","N":"0.00","O":"0.00","P":"0.00","Q":"0.00","R":"SAJ-alpha","S":["1","23,99","8","1","0","0","0","3593"]}
    # A: string, //Device ID 
    # B: string, //Unix Time in Second
    # C: Array<string>, //GPS Parameter Lat, Long, Heading, Speed
    # D: string, //Time when Genset On in Second
    # E: string, //Time when Genset Off in Second
    # F: string, //Engine Hour
    # G: string, //Room Temperature 
    # H: string, //Battery Voltage
    # I: string, //Engine Status Bool(1/0, On/Off)
    # J: Array<string>, //Current RST IR,IS,IT
    # K: Array<string>, //Voltage RST VR,VS,VT
    # L: Array<string>, //kVA RST kVAR,kVAS,kVAT
    # M: string, //Tank Level on Litre
    # N: string, //Fuel Consumption on Litre
    # O: string, //Pressure Engine
    # P: string, //RPM Engine
    # Q: string, //Coolant Temperature 
    # R: string, //Firmware Version
    # S:Array<string> //Device Status Pin Status, Signal Quality, Network Mode, SDCard Status, Err1, Err2, Err3, Free Memory
    with con:
        cur = con.cursor()
        cur.execute("SELECT lat, lng FROM indonesia ORDER BY RAND() LIMIT 1")
        db_result = cur.fetchone()
    
    msg['A'] = random.choice(engine)
    msg['B'] = time.time()
    msg['C'] = [str(db_result[0]),str(db_result[1]),"0.490", random.randint(1,160)]    
    msg['F'] = random.randint(1,86400)
    msg['G'] = random.uniform(1,95)
    msg['H'] = "12.5"
    msg['I'] = "1"
    msg['J'] = [str(random.uniform(30,120)),str(random.uniform(30,120)),str(random.uniform(30,120))]
    msg['K'] = [str(random.uniform(30,120)),str(random.uniform(30,120)),str(random.uniform(30,120))]
    msg['L'] = [str(random.uniform(30,120)),str(random.uniform(30,120)),str(random.uniform(30,120))]
    msg['N'] = random.uniform(1,30)
    msg['O'] = random.uniform(30,120)
    msg['P'] = random.randint(10,4800)
    msg['Q'] = random.uniform(1,95)
    msg['R'] = "1.0.1"    
    msg['T'] = random.uniform(30,120) 
    msg['U'] = random.uniform(30,120) 
    msg['V'] = "1"    
    msg['info'] = 'data dummy dari ws Bandung'
    result = json.dumps(msg)
    return result

def go_mqtt():
    try:
        client = mqtt.Client("Publisher_1", transport="tcp")  # create new instance
        
        client.username_pw_set(user, password=password)
        # connect to broker
        client.connect(broker_address, port=port)
        client.loop_start()  # start the loop
        
        client.subscribe(topic)
        message = create_message()
        print(message)
        client.publish(topic,str(message))
        time.sleep(1)  # wait
        client.loop_stop()  # stop the loop
        client.disconnect()
        
    except Exception as e:
        print("E R R O R : ", e)
        traceback.print_exc(file=sys.stdout)
        exit()
        
        
if __name__ == "__main__":
    
    loop = True
    print('_____START_____')
    while(loop):
        try:
            go_mqtt()
            time.sleep(1)
        except Exception as e:
            print("E R R O R : ", e)
            traceback.print_exc(file=sys.stdout)
            loop = False
            exit()
