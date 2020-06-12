#!/usr/bin/python3
# -*- coding: utf-8 -*-

import string
import random
import datetime,time
import sys, traceback
from authlib.jose import jwt
import bcrypt
import hashlib 
import json
import base64
from getpass import getpass



class TokenMaker():
    def __init__(self):        
        self.header = {'typ': 'JWT','alg': 'HS256'}
        self.payload = {}
        self.secretKey = ''
        self.expired = ''

    def generate_secret_key(self,char = 256):
        key = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(char))
        return key
    
    def create_token(self, data):
        path = 'jwt-key.pub'
        days_file = open(path,'r')
        key = days_file.read()
        self.secretKey = key
        self.payload['exp'] = round(time.time() + 86400)
        # self.payload['nbf'] = time.time() + 2
        self.payload['iss'] = 'genset_monitoring'
        self.payload['iat'] = datetime.datetime.utcnow()
        self.payload['access'] = data['access']
        self.payload['uid'] = data['users_user_id']
        self.payload['uname'] =  data['users_username']
        self.payload['access'] =  data['access']
        token = jwt.encode(self.header,self.payload,self.secretKey)
        return token

    def generate_token(self, data):
        path = 'jwt-key.pub'
        data_user = data[0]
        days_file = open(path,'r')
        key = days_file.read()
        self.secretKey = key   
        self.payload['exp'] = round(time.time() + 86400)
        # self.payload['nbf'] = time.time() + 2
        self.payload['iss'] = 'genset_monitoring'
        self.payload['iat'] = datetime.datetime.utcnow()
        self.payload['uid'] = data_user['users_user_id']
        self.payload['uname'] =  data_user['users_username']
        self.payload['access'] =  data_user['access']
        token = jwt.encode(self.header,self.payload,self.secretKey)        
        return token

    def get_user_data(self, token):
        userdata = {}
        user_json = json.loads(base64.b64decode(token.split(".")[1]))
        userdata['user_id'] = user_json['uid']
        userdata['username'] = user_json['uname']
        userdata['access'] = user_json['access']
        return userdata
        pass

    def check_token(self, token):
        path = 'jwt-key.pub'
        days_file = open(path,'r')
        key = days_file.read()
        claims = jwt.decode(token, key)
        if claims.validate() is None:
            return True

    def create_password(self,raw_password):
        result = hashlib.md5(raw_password.encode())
        return result.hexdigest()



if __name__ == "__main__":    
    try:
        tm = TokenMaker()
        password = "akulaku"
        secretkey = tm.generate_secret_key()
        print(type(secretkey))
        hash = tm.create_password(password)
        print(hash)
    except Exception as e:
        print(e)
        traceback.print_exc(file=sys.stdout)
        pass
