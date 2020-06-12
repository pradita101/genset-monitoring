#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import tornado.web
import tornado.ioloop
import json
import models
import sys, traceback
import datetime
import time
import token_maker

tm = token_maker.TokenMaker()
db = models.Models()
cnv = models.Convert()

class GensetAllData(RequestHandler):

    def set_default_headers(self):
        print ("GensetAllData")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.set_header('Content-Type', 'application/json')

    def get(self):
        token = self.request.headers.get('Authorization')        
        check = tm.check_token(token)
        if check : 
            result = db.get_all_genset_data()
            if result:
                data_log = tm.get_user_data(token)
                data_log['activity'] = "Get All Genset Data"
                data_log['ip_address'] = self.request.remote_ip            
                data_log['activity_time'] = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
                db.insert_log(data_log)

                self.write({'status':True, 'msg': 'Data Received', 'data':result})
            else:
                self.write({'status':False, 'msg': 'No Data', 'data': None})
        else:
            self.set_status(403)

    def options(self):
        # no body
        self.set_status(204)
        self.finish()

class GensetData(RequestHandler):

    def set_default_headers(self):
        print ("GensetData")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.set_header('Content-Type', 'application/json')

    def get(self, id):
        token = self.request.headers.get('Authorization')
        check = tm.check_token(token)
        if check :
            result_data = db.get_genset_data(id)
            status = False if result_data is None else True
            if (status):
                data_log = tm.get_user_data(token)
                data_log['activity'] = "Get Detail Genset Data"
                data_log['ip_address'] = self.request.remote_ip            
                data_log['activity_time'] = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
                db.insert_log(data_log)

                self.write({'status':True, 'msg': 'Data Received','data':result_data})
            else:
                self.write({'status':False, 'msg': 'No Data', 'data':None})
        else:
            self.set_status(403)
        
    def post(self, _):
        token = self.request.headers.get('Authorization')
        check = tm.check_token(token)
        data = json.loads(self.request.body)
        if check :            
            db.insert_genset(data)
            data_log = tm.get_user_data(token)
            data_log['activity'] = "Add New Genset Data"
            data_log['ip_address'] = self.request.remote_ip            
            data_log['activity_time'] = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
            db.insert_log(data_log)

            self.write({'status':True, 'message': 'new data genset added'})
        else:
            self.set_status(403)    

    def options(self, _):
        self.set_status(204)
        self.finish()

class UpdateGenset(RequestHandler):
    def set_default_headers(self):
        print ("UpdateGenset")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.set_header('Content-Type', 'application/json')

    def post(self, _):
        token = self.request.headers.get('Authorization')
        check = tm.check_token(token)
        if check :
            data = json.loads(self.request.body)            
            db.update_genset(data)
            data_log = tm.get_user_data(token)
            data_log['activity'] = "Update Genset Data"
            data_log['ip_address'] = self.request.remote_ip            
            data_log['activity_time'] = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
            db.insert_log(data_log)

            self.write({'status':True, 'message': 'data genset updated'})
        else:
            self.set_status(403)

    def options(self, _):
        self.set_status(204)
        self.finish()
    	
        
class StreamData(RequestHandler):

    def set_default_headers(self):
        print ("StreamData")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.set_header('Content-Type', 'application/json')

    def post(self, _):
        token = self.request.headers.get('Authorization')
        check = tm.check_token(token)
        if check:
            data = json.loads(self.request.body)
            genset_id = data['id']
            start_date = data['start_date']
            end_date = data['end_date']
            result_data = db.get_stream_range_data(genset_id, start_date, end_date)
            if (result_data):
                data_log = tm.get_user_data(token)
                data_log['activity'] = "Get Stream Data"
                data_log['ip_address'] = self.request.remote_ip            
                data_log['activity_time'] = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
                db.insert_log(data_log)

                self.write({'status':True, 'msg': 'Data Received', 'data':result_data})
            else:
                self.write({'status':False, 'msg': 'No Data', 'data': None})
        else:
            self.set_status(403)

    def options(self, _):
    	# no body
    	self.set_status(204)
    	self.finish()

class StreamAllData(RequestHandler):
    
    def set_default_headers(self):
        print ("StreamAllData")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.set_header('Content-Type', 'application/json')

    def get(self):
        token = self.request.headers.get('Authorization')
        check = tm.check_token(token)
        if check:
            result = db.get_all_stream_data()
            if result:
                self.write({'status':True, 'msg': 'Data Received', 'data':result})
            else:
                self.write({'status':False, 'msg': 'No Data', 'data': None})
        else:
            self.set_status(403)


    def options(self, _):
    	# no body
    	self.set_status(204)
    	self.finish()

class streamGensetData(RequestHandler):
    def set_default_headers(self):
        print ("streamGensetData")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.set_header('Content-Type', 'application/json')
        
    def options(self, _):
        	# no body
    	self.set_status(204)
    	self.finish()

    def get(self, id):
        token = self.request.headers.get('Authorization')
        check = tm.check_token(token)
        if check:
            results = db.get_genset_stream(id)
            if results:
                  data_log = tm.get_user_data(token)
                  data_log['activity'] = "Get Stream Genset Data"
                  data_log['ip_address'] = self.request.remote_ip            
                  data_log['activity_time'] = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
                  db.insert_log(data_log)
                  self.write({'status':True, 'msg': 'Data Received', 'data':results})
            else:
                  self.write({'status':False, 'msg': 'No Data', 'data': None})
        else:
            self.set_status(403)


class calculateAverage(RequestHandler):

    def set_default_headers(self):
        print ("calculateAverage")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.set_header('Content-Type', 'application/json')

    def options(self, _):
        	# no body
    	self.set_status(204)
    	self.finish()

    def get(self):
        results = db.get_avg_data()
        if results:
            loads = json.loads(results)
            for result in loads:
                db.insert_avg_temp(result)
                # print(type(result))
                # print(result)
                # pass
        else:
            print("no data to calculate")
        self.set_status(200)

class recoveryData(RequestHandler):
    def set_default_headers(self):
        print ("recoveryData")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.set_header('Content-Type', 'application/json')

    def options(self, _):        	
    	self.set_status(204)
    	self.finish()

    def get(self):
        results = db.get_raw_data()
        if results:
            loads = json.loads(results)
            for raw in loads:                
                data = cnv.format_data_stream(raw['raw_data_raw_data'])
                if data is not None :
                    if 'Id' in data.keys():
                        db.insert_stream(data)
        else:
            print("no data to calculate")
        self.set_status(200)


class calculateAverageAll(RequestHandler):
    
    def set_default_headers(self):
        print ("calculateAverageAll")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.set_header('Content-Type', 'application/json')

    def options(self, _):
        	# no body
    	self.set_status(204)
    	self.finish()

    def get(self):
        results = db.get_avg_data_all()
        if results:
            loads = json.loads(results)
            for result in loads:
                db.insert_avg_temp(result)
                # print(type(result))
                # print(result)
                # pass
        else:
            print("no data to calculate")
        self.set_status(200)

class getAverageData(RequestHandler):

    def set_default_headers(self):
        print ("getAverageData")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.set_header('Content-Type', 'application/json')

    def options(self, _):
        	# no body
    	self.set_status(204)
    	self.finish()

    def post(self, period):
        data = json.loads(self.request.body)
        token = self.request.headers.get('Authorization')
        check = tm.check_token(token)
        if check :
            result_data = db.get_period_avg_data(data['period'], data['genset_id'])
            status = False if result_data is None else True
            if (status):

                  data_log = tm.get_user_data(token)
                  data_log['activity'] = "get average data"
                  data_log['ip_address'] = self.request.remote_ip            
                  data_log['activity_time'] = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
                  db.insert_log(data_log)
                  self.write({'status':True, 'msg': 'Data Received','data':result_data})

            else:
                self.write({'status':False, 'msg': 'No Data', 'data':None})
        else:
            self.set_status(403)

class addUser(RequestHandler):
    
    def set_default_headers(self):
        print ("addUser")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.set_header('Content-Type', 'application/json')

    def options(self, _):
        	# no body
    	self.set_status(204)
    	self.finish()

    def post(self, _):
        data_log = {}
        token = self.request.headers.get('Authorization')
        check = tm.check_token(token)
        if check :
            post_data = json.loads(self.request.body)
            data = post_data
            data['secret'] = tm.generate_secret_key()
            pwd_hash = tm.create_password(data['password'])
            data['password'] = pwd_hash            
            if db.insert_user(data):
                data_log = tm.get_user_data(token)
                data_log['activity'] = 'Add User'
                data_log['ip_address'] = self.request.remote_ip                
                data_log['activity_time'] = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
                db.insert_log(data_log)

                self.write({'status':True, 'message': 'user inserted'})
            else:
                self.write({'status':False, 'message': 'user insert failed'})
        else:
            self.set_status(403)

class updateUser(RequestHandler):
    
    def set_default_headers(self):
        print ("updateUser")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.set_header('Content-Type', 'application/json')

    def options(self, _):
        	# no body
    	self.set_status(204)
    	self.finish()

    def post(self, _):
        token = self.request.headers.get('Authorization')
        check = tm.check_token(token)
        if check :
            data = json.loads(self.request.body)            
            old_pwd = tm.create_password(data['old_password'])
            data['old_password'] = old_pwd            
            new_pwd = tm.create_password(data['new_password'])
            data['new_password'] = new_pwd            
            if db.update_users(data):
                 data_log = tm.get_user_data(token)
                 data_log['activity'] = "Update User"
                 data_log['ip_address'] = self.request.remote_ip            
                 data_log['activity_time'] = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
                 db.insert_log(data_log) 
                 self.write({'status':True, 'message': 'user Updated'})

            else:
                self.write({'status':False, 'message': 'user Update Failed'})
        else:
            self.set_status(403)

class Login(RequestHandler):

    def set_default_headers(self):
        print ("Login")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.set_header('Content-Type', 'application/json')

    def options(self, _):
        	# no body
    	self.set_status(204)
    	self.finish()

    def post(self, _):
        data = json.loads(self.request.body)            
        pwd = tm.create_password(data['password'])        
        user_data = db.get_user(data['username'], pwd)
        if user_data:            
            token = tm.generate_token(json.loads(user_data))
            data_log = tm.get_user_data(token)
            data_log['activity'] = "login"
            data_log['ip_address'] = self.request.remote_ip            
            data_log['activity_time'] = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
            db.insert_log(data_log)

            self.write({'status':True, 'msg': 'Data Received','data':user_data,'token':token.decode("UTF-8")})
        else:
            self.write({'status':False, 'msg': 'No Data Received','data': None})
       


    

def make_app():
    urls = [
        (r"/api/genset/([^/]+)?", GensetData),
        (r"/api/stream/([^/]+)?", StreamData),
        (r"/api/login/([^/]+)?", Login),
        (r"/api/update_genset/([^/]+)?", UpdateGenset),
        (r"/api/stream_all/", StreamAllData),
        (r"/api/genset_all/", GensetAllData),
        (r"/api/cal_average/", calculateAverage),
        (r"/api/cal_average_all/", calculateAverageAll),
        (r"/api/avg_temp/([^/]+)?", getAverageData),
        (r"/api/add_user/([^/]+)?", addUser),
        (r"/api/recovery/", recoveryData),
        (r"/api/stream_genset/([^/]+)?", streamGensetData)
        ]
    return Application(urls, debug=True)

if __name__ == '__main__':
    try:
        print("__ S T A R T __")        
        insert_user = db.check_users()
        if insert_user is not True :
            db.input_default_user()
        app = make_app()
        app.listen(9379)
        IOLoop.instance().start()

    
    except Exception as e:
        print("Runtime Error : ",e)
        traceback.print_exc(file=sys.stdout)
    
