#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.sql import func
from sqlalchemy import case
import time
import decimal
import datetime
import configparser
import json
import sys, traceback
import enum
import token_maker


config = configparser.ConfigParser()
config.read('config.ini')

db_server = str(config['DB']['db_server'])+":"+str(config['DB']['db_port'])
db_username = str(config['DB']['db_username'])
db_pass = str(config['DB']['db_pswrd'])
db_name = str(config['DB']['db_name'])
db_dialect = str(config['DB']['db_engine'])
db_driver = str(config['DB']['db_driver'])

tm = token_maker.TokenMaker()

connection = u""+db_dialect+"+"+db_driver+"://"+db_username+":"+db_pass+"@"+db_server+"/"+db_name
db_engine = db.create_engine(connection,echo = False, pool_size=2048, max_overflow=0)
exp = db.sql.expression
session = db.orm.sessionmaker(bind=db_engine)
Base = db.ext.declarative.declarative_base()


class Genset(Base):
    __tablename__ = 'genset_ASI'
    genset_id = db.Column('genset_id', db.String(length=20), primary_key=True)
    genset_name = db.Column('genset_name', db.String(length=25))
    genset_details = db.Column('genset_details', db.String(length=250))
    genset_tank_capacity = db.Column('genset_tank_capacity', db.SmallInteger)
    genset_displacement = db.Column('genset_displacement', db.String(30))
    genset_starting_system = db.Column('genset_starting_system', db.String(length=50))
    genset_design_features = db.Column('genset_design_features', db.String(length=50))
    genset_full_load_consumption = db.Column('genset_full_load_consumption', db.Float)
    genset_three_quarter_load_consumption = db.Column('genset_three_quarter_load_consumption', db.Float)
    genset_half_load_consumption = db.Column('genset_half_load_consumption', db.Float)
    genset_quarter_load_consumption = db.Column('genset_quarter_load_consumption', db.Float)
    genset_bore_stroke = db.Column('genset_bore_stroke', db.String(length=125))
    genset_continuous_rated_output = db.Column('genset_continuous_rated_output', db.Float)
    genset_voltage_allowance = db.Column('genset_voltage_allowance', db.String(length=20))
    organization = db.Column('organization', db.String(length=75))
    
    def __repr__(self):
        result = {}
        result['genset_id'] = self.genset_id
        result['genset_name'] = self.genset_name
        result['genset_details'] = self.genset_details
        result['genset_tank_capacity'] = self.genset_tank_capacity
        result['genset_displacement'] = self.genset_displacement
        result['genset_starting_system'] = self.genset_starting_system
        result['genset_design_features'] = self.genset_design_features
        result['genset_full_load_consumption'] = self.genset_full_load_consumption
        result['genset_three_quarter_load_consumption'] = self.genset_three_quarter_load_consumption
        result['genset_half_load_consumption'] = self.genset_half_load_consumption
        result['genset_quarter_load_consumption'] = self.genset_quarter_load_consumption
        result['genset_bore_stroke'] = self.genset_bore_stroke
        result['genset_continuous_rated_output'] = self.genset_continuous_rated_output
        result['genset_voltage_allowance'] = self.genset_voltage_allowance
        result['organization'] = self.organization
        return json.dumps(result)
    
class Stream(Base):
    __tablename__ = 'data_stream_ASI'
    msg_id = db.Column('msg_id', db.Integer, db.Sequence('msg_id_seq'), primary_key=True)
    genset_id = db.Column('genset_id', db.String(length=20))
    timestamp = db.Column('timestamp', db.Integer)
    temperature = db.Column('temperature', db.DECIMAL)
    longitude = db.Column('longitude', db.Float)
    latitude = db.Column('latitude', db.Float)
    stream_date = db.Column('stream_date', db.DateTime)
    engine_hour = db.Column('engine_hour', db.Float)
    fuel_consumption = db.Column('fuel_consumption', db.SmallInteger)
    oil_level = db.Column('oil_level', db.SmallInteger)
    engine_status = db.Column('engine_status', db.SmallInteger)
    genset_mode = db.Column('genset_mode', db.SmallInteger)
    engine_speed = db.Column('engine_speed', db.Float)
    oil_pressure = db.Column('oil_pressure', db.Float)
    power_output = db.Column('power_output', db.Float)
    output_stream = db.Column('output_stream', db.Float)
    voltage_1_phase = db.Column('voltage_1_phase', db.Float)
    voltage_3_phase = db.Column('voltage_3_phase', db.Float)
    frequency = db.Column('frequency', db.Float)
    batery_voltage = db.Column('batery_voltage', db.Float)
    
    def __repr__(self):
        result = {}
        result['msg_id'] = self.msg_id
        result['genset_id'] = self.genset_id
        result['timestamp'] = int(self.timestamp)
        result['temperature'] = self.temperature
        result['longitude'] = self.longitude
        result['latitude'] = self.latitude
        result['stream_date'] = self.stream_date.strftime('%d-%m-%Y %H:%M:%S')
        result['engine_hour'] = float(self.engine_hour)
        result['fuel_consumption'] = float(self.fuel_consumption)
        result['oil_level'] = float(self.oil_level)
        result['engine_status'] = self.engine_status
        result['genset_mode'] = self.genset_mode
        result['engine_speed'] = float(self.engine_speed)
        result['oil_pressure'] = float(self.oil_pressure)
        result['power_output'] = float(self.power_output)
        result['output_stream'] = float(self.output_stream)
        result['voltage_1_phase'] = float(self.voltage_1_phase)
        result['voltage_3_phase'] = float(self.voltage_3_phase)
        result['frequency'] = float(self.frequency)
        result['batery_voltage'] = float(self.batery_voltage)
        result_json = json.dumps(result)
        return result_json

class Temperature(Base):
    __tablename__ = 'average_temperature_daily_ASI'
    avg_id = db.Column('avg_id', db.Integer, db.Sequence('avg_id_seq'), primary_key=True)
    genset_id = db.Column('genset_id', db.String(length=20))
    avg_date = db.Column('avg_date', db.Date)
    avg_temperature = db.Column('avg_temperature', db.Integer)
    avg_engine_hour = db.Column('avg_engine_hour', db.Integer)
    avg_fuel_consumption = db.Column('avg_fuel_consumption', db.Float)
    avg_engine_speed = db.Column('avg_engine_speed', db.Float)
    avg_off = db.Column('avg_off', db.SmallInteger)
    
    def __repr__(self):
        result = {}
        result['avg_id'] = self.avg_id
        result['genset_id'] = self.genset_id
        result['avg_date'] = self.avg_date.strftime('%d-%m-%Y')
        result['avg_temperature'] = self.avg_temperature
        result['avg_engine_hour'] = self.avg_engine_hour
        result['avg_fuel_consumption'] = self.avg_fuel_consumption
        result['avg_engine_speed'] = self.avg_engine_speed
        result['avg_off'] = self.avg_off
        result_json = json.dumps(result)
        return result_json

class Raw(Base):
    __tablename__ = 'raw_data_ASI'
    raw_id = db.Column('raw_id', db.Integer, db.Sequence('raw_id_seq'), primary_key=True)
    raw_data = db.Column('raw_data', db.Text)

    def __repr__(self):
        result = {}
        result['raw_id'] = self.raw_id
        result['raw_data'] = self.raw_data
        result_json = json.dumps(result)
        return result_json

class TypeOfUser(enum.Enum):
    user = "user"
    admin = "admin"
    root = "root"


class Users(Base):
    __tablename__ = 'users'
    user_id = db.Column('user_id', db.Integer, db.Sequence('user_id_seq'), primary_key=True)
    username = db.Column('username', db.String(length=25))
    email = db.Column('email', db.String(length = 100))
    secret = db.Column('secret', db.String(length=256))
    status = db.Column('status', db.SMALLINT)
    user_type = db.Column('user_type', db.Enum(TypeOfUser))
    password = db.Column('password', db.String(length=256))
    organization = db.Column('organization', db.String(length=75))

    def __repr__(self):
        result = {}
        result['user_id'] = self.user_id
        result['username'] = self.username
        result['secret'] = self.secret
        result['status'] = self.status
        result['user_type'] = self.user_type
        result['password'] = self.password
        result['organization'] = self.organization
        result_json = json.dumps(result)
        return result_json

class DataLog(Base):
    __tablename__ = "data_log"
    log_id = db.Column('log_id', db.BIGINT, db.Sequence('log_id_seq'), primary_key=True)
    user_id = db.Column('user_id', db.INTEGER)
    username = db.Column('username', db.String(length=25))
    activity = db.Column('activity', db.String(length=200))
    ip_address = db.Column('ip_address', db.String(length=20))
    access = db.Column('access', db.String(length=15))
    activity_time = db.Column('activity_time', db.DateTime)

    def __repr__(self):
        result = {}
        result['log_id'] = self.log_id
        result['user_id'] = self.user_id
        result['username'] = self.username
        result['activity'] = self.activity
        result['ip_address'] = self.ip_address
        result['access'] = self.access
        result['activity_time'] = self.activity_time
        result_json = json.dumps(result)
        return result_json
        
class Models():
    
    def __init__(self):
        Base.metadata.bind = db_engine        
        Base.metadata.create_all()
        self.Session = db.orm.sessionmaker(bind=db_engine)
        
        
    
    def insert_stream(self, data):
        session = self.Session()
        data_stream = Stream(
            genset_id = data['Id'],
            timestamp = data['Time'],
            temperature = data['Tmp'],
            longitude = data['Lng'],
            latitude = data['Lat'],
            stream_date = data['Date'],
            engine_hour = data['Ehr'],
            engine_status = data['Eng'],
            fuel_consumption = data['FuelCons'],
            oil_level = 0,
            genset_mode = data['gensetMode'],
            engine_speed = data['engineSpeed'],
            oil_pressure = data['oilPressure'],
            power_output = data['powerOutput'],
            output_stream = data['outputStream'],
            voltage_1_phase = data['voltage_1_phase'],
            voltage_3_phase = data['voltage_3_phase'],
            frequency = data['frequency'],
            batery_voltage = data['bateryVoltage']
        )
        session.add(data_stream)
        session.commit()

    def insert_raw(self, data):        
        session = self.Session()        
        raw_data = Raw(
            raw_data = data
        )
        session.add(raw_data)
        session.commit()

    def insert_user(self, data):        
        session = self.Session()        
        user_data = Users(
            username = data['username'],
            email = data['email'],
            secret = data['secret'],
            status = data['status'],
            user_type = TypeOfUser(data['user_type']).value,            
            password = data['password']
        )
        session.add(user_data)
        session.commit()

    def insert_log(self,data):
        session = self.Session()
        log_data = DataLog(
            user_id = data['user_id'],
            username = data['username'],
            activity = data['activity'],
            ip_address = data['ip_address'],
            access = data['access'],
            activity_time = data['activity_time']
        )
        session.add(log_data)
        session.commit()

    def get_all_log(self):
        session = self.Session()
        q = session.query(DataLog)
        result = session.execute(q).fetchall()
        result_json = self.format_json(result)
        return result_json
        
        
    def insert_genset(self, data):
        session = self.Session()
        data_genset = Genset(
            genset_id = data['Id'],
            genset_name = data['name'],
            genset_details = data['detail'],
            genset_tank_capacity = int(data['tank_capacity']),
            genset_displacement = data['displacement'],
            genset_starting_system = data['starting_system'],
            genset_design_features = data['design_features'],
        	genset_full_load_consumption = self.covert_float(data['full_load_consumption']),
        	genset_three_quarter_load_consumption = self.covert_float(data['three_quarter_load_consumption']),
        	genset_half_load_consumption = self.covert_float(data['half_load_consumption']),
        	genset_quarter_load_consumption = self.covert_float(data['quarter_load_consumption']),
        	genset_bore_stroke = data['bore_stroke'],
        	genset_continuous_rated_output = self.covert_float(data['continuous_rated_output']),
        	genset_voltage_allowance = data['voltage_allowance']
        )
        session.add(data_genset)
        session.commit()
    
        
    def update_genset(self, data):
        session = self.Session()        
        session.query(Genset).filter(Genset.genset_id == data['Id']).update({
            Genset.genset_name : data['name'],
            Genset.genset_details : data['detail'],
            Genset.genset_tank_capacity : data['tank_capacity'],
            Genset.genset_displacement : data['displacement'],
            Genset.genset_starting_system : data['starting_system'],
            Genset.genset_design_features : data['design_features'],
        	Genset.genset_full_load_consumption : data['full_load_consumption'],
        	Genset.genset_three_quarter_load_consumption : data['three_quarter_load_consumption'],
        	Genset.genset_half_load_consumption : data['half_load_consumption'],
        	Genset.genset_quarter_load_consumption : data['quarter_load_consumption'],
        	Genset.genset_bore_stroke : data['bore_stroke'],
        	Genset.genset_continuous_rated_output : data['continuous_rated_output'],
        	Genset.genset_voltage_allowance : data['voltage_allowance']},
        synchronize_session = False)
        session.commit()

    def update_users(self, data):
        session = self.Session()
        session.query(Users).filter(db.and_(Users.user_id == data['user_id'], Users.password == data['old_password'])).update({            
            Users.email : data['email'],
            Users.password : data['new_password']}
        )

    def check_users(self):
        session = self.Session()
        q = session.query(Users)
        result = session.execute(q).fetchall()
        result_json = self.format_json(result)
        if result_json:
            return True
        else:
            return False

    def input_default_user(self):
        session = self.Session()
        user_data = Users(
            username = 'admin',
            email = 'admin@imaniprima.co.id',
            secret = tm.generate_secret_key(),
            status = 1,
            user_type = TypeOfUser.root,            
            password = tm.create_password('R4H45!@')
        )
        session.add(user_data)
        session.commit()

    def get_user(self, username, password):
        session = self.Session()
        q = session.query(Users.username, Users.user_type, Users.user_id, Users.organization, Users.email).filter(db.and_(db.or_(Users.username == username, Users.email == username), Users.password == password, Users.status == 1))
        results = session.execute(q).fetchall()
        result_json = self.format_json(results)
        return result_json

    def get_raw_data(self):
        session = self.Session()
        q = session.query(Raw)
        results = session.execute(q).fetchall()
        result_json = self.format_json(results)
        return result_json

    
    def insert_avg_temp(self,data):
        session = self.Session()
        data_avg = Temperature(
            genset_id = str(data['genset_id']),
            avg_date = str(data['date']),
            avg_temperature = float(data['temp']),
            avg_fuel_consumption = float(data['fuel']),
            avg_off = int(data['off']),
            avg_engine_hour = int(data['ehr'])
        )
        session.add(data_avg)
        session.commit()

    def clear_avg_temp(self):
        session = self.Session()
        q = session.query(Temperature).delete()
        session.execute(q)

    
    def get_all_genset_data(self):
        session = self.Session()
        q = session.query(Genset).order_by(Genset.genset_id)
        results = session.execute(q).fetchall()
        result_json = self.format_json(results)
        return result_json
    
    def get_genset_data(self, id):
        session = self.Session()
        q = session.query(Genset).filter(Genset.genset_id == id)
        results = session.execute(q).fetchall()
        result_json = self.format_json(results)
        return result_json

    def get_genset_stream(self, id):
        session = self.Session()
        q = session.query(Stream).filter(Stream.genset_id == id).order_by(Stream.genset_id,Stream.timestamp)
        results = session.execute(q).fetchall()
        result_json = self.format_json(results)
        return result_json
        
    
    def get_stream_range_data(self, id, start_date, end_date):
        session = self.Session()
        q = session.query(Stream).filter(db.and_(Stream.genset_id == id,Stream.stream_date >= start_date, Stream.stream_date <= end_date)).order_by(Stream.timestamp)
        results = session.execute(q).fetchall()
        result_json = self.format_json(results)
        return result_json
        
    def get_all_stream_data(self):
        session = self.Session()        
        q = session.query(Stream)
        results = session.execute(q).fetchall()
        result_json = self.format_json(results)
        return result_json

    def get_avg_data(self):
        session = self.Session()
        yesterday = datetime.datetime.strftime(datetime.datetime.now() - datetime.timedelta(1), '%Y-%m-%d')        
        q = session.query(
                func.avg(Stream.temperature).label('temp'), 
                func.date(Stream.stream_date).label('date'), 
                Stream.genset_id.label('genset_id'),
                func.max(Stream.engine_hour).label('ehr'),
                func.avg(Stream.fuel_consumption).label('fuel'),
                func.avg(Stream.engine_speed).label('speed'), 
                func.sum(
                    case(
                        [
                            (Stream.engine_status == 0, 1)
                        ],
                        else_= 0
                    )
                ).label('off')
            ).filter(func.date(Stream.stream_date) == yesterday).group_by(func.date(Stream.stream_date), Stream.genset_id)
        results = session.execute(q).fetchall()        
        result_json = self.format_input_json(results)
        return result_json 

    def get_avg_data_all(self):
        session = self.Session()           
        q = session.query(
                func.avg(Stream.temperature).label('temp'), 
                func.date(Stream.stream_date).label('date'), 
                Stream.genset_id.label('genset_id'),
                func.max(Stream.engine_hour).label('ehr'),
                func.avg(Stream.fuel_consumption).label('fuel'),
                func.avg(Stream.engine_speed).label('speed'),
                func.sum(
                    case(
                        [
                            (Stream.engine_status == 0, 1)
                        ],
                        else_= 0
                    )
                ).label('off')
            ).group_by(func.date(Stream.stream_date), Stream.genset_id)
        results = session.execute(q).fetchall()        
        result_json = self.format_input_json(results)      
        
        return result_json 

    def get_period_avg_data(self, period, genset_id):
        session = self.Session()
        enddate = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
        startdate = self.getPeriodDate(period)
        q = session.query(
            func.avg(Temperature.avg_temperature).label('temp'),
            func.avg(Temperature.avg_off).label('engine_off')
        ).filter(db.and_(func.date(Temperature.avg_date) >= startdate, func.date(Temperature.avg_date) <= enddate, Temperature.genset_id == genset_id ))
        results = session.execute(q).fetchall()        
        result_json = self.format_json(results)
        return result_json 

        
    def getPeriodDate(self, period):
        date = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
        if(period == 'week'):
            date = datetime.datetime.strftime(datetime.datetime.now() - datetime.timedelta(days=7), '%Y-%m-%d')
        elif(period == 'month'):
            date = datetime.datetime.strftime(datetime.datetime.now() - datetime.timedelta(days=30), '%Y-%m-%d')
        elif(period == 'year'):
            date = datetime.datetime.strftime(datetime.datetime.now() - datetime.timedelta(days=365), '%Y-%m-%d')
        
        return date

    def format_json(self, data):
        res = []
        if data:
            for rows in data:
                itm = {}
                for row in rows.items():
                    row_lst = list(row)
                    if row_lst is None:
                        return False

                    if isinstance(row_lst[1], datetime.datetime) == True:
                        itm[row_lst[0]] = row_lst[1].strftime("%d-%m-%Y")
                    elif isinstance(row_lst[1], datetime.time) == True:
                        itm[row_lst[0]] = row_lst[1].strftime("%H:%M:%S")
                    elif isinstance(row_lst[1], datetime.date) == True:
                        itm[row_lst[0]] = row_lst[1].strftime("%d-%m-%Y")
                    elif isinstance(row_lst[1], decimal.Decimal) == True:
                        itm[row_lst[0]] = float(row_lst[1])
                    elif isinstance(row_lst[1], enum.Enum) == True:
                        itm[row_lst[0]] = TypeOfUser(row_lst[1]).value
                    else:
                        itm[row_lst[0]] = row_lst[1]
                res.append(itm)
            result_json = json.dumps(res)
            return result_json
        else:
            return None

    def format_input_json(self, data):
        res = []
        if data:
            for rows in data:
                itm = {}
                for row in rows.items():
                    row_lst = list(row)
                    if isinstance(row_lst[1], datetime.datetime) == True:
                        itm[row_lst[0]] = row_lst[1].strftime("%Y-%m-%d")
                    elif isinstance(row_lst[1], datetime.time) == True:
                        itm[row_lst[0]] = row_lst[1].strftime("%H:%M:%S")
                    elif isinstance(row_lst[1], datetime.date) == True:
                        itm[row_lst[0]] = row_lst[1].strftime("%Y-%m-%d")
                    elif isinstance(row_lst[1], decimal.Decimal) == True:
                        itm[row_lst[0]] = round( float(row_lst[1]), 2)
                    else:
                        itm[row_lst[0]] = row_lst[1]
                res.append(itm)
            result_json = json.dumps(res)
            return result_json
        else:
            return None
    def covert_float(self, x):
        val = str.replace(x, ',', '.')
        result = float(val)
        return result
        

class Convert():    
    def __init__(self):
        self.mysql_date = "%Y-%m-%d"
        self.mysql_datetime = "%Y-%m-%d %H:%M:%S"
    
    def format_data_stream(self, data):
        try:
            data_json = json.loads(data)
            result_data = {}
            if 'A' in data_json:
                result_data['Id'] = data_json['A']
                result_data['Time'] = int(data_json['B'])
                result_data['Lat'] = float(data_json['C'][0])
                result_data['Lng'] = float(data_json['C'][1])
                result_data['Tmp'] = float(data_json['G'])
                result_data['Ehr'] = float(data_json['F'])
                result_data['Eng'] = float(data_json['I'])
                result_data['Date'] = datetime.datetime.fromtimestamp(int(data_json['B']))
                result_data['FuelCons'] = int(data_json['N'])                
                result_data['gensetMode'] = int(data_json['V'])
                result_data['engineSpeed'] = float(data_json['P'])
                result_data['oilPressure'] = float(data_json['O'])
                result_data['powerOutput'] = float(data_json['L'][0])
                result_data['outputStream']  = float(data_json['T'])
                result_data['voltage_1_phase'] = float(data_json['K'][0])
                result_data['voltage_3_phase']= float(data_json['K'][2])
                result_data['frequency'] = float(data_json['U'])
                result_data['bateryVoltage'] = float(data_json['H'])
                # result_data['Id'] = data_json['Id']
                # result_data['Time'] = int(data_json['Time'])
                # result_data['Lat'] = float(data_json['Lat'])
                # result_data['Lng'] = float(data_json['Lng'])
                # result_data['Tmp'] = float(data_json['Tmp'])
                # result_data['Ehr'] = float(data_json['Eh'])
                # result_data['Eng'] = float(data_json['Eng'])
                # result_data['Date'] = datetime.datetime.fromtimestamp(int(data_json['Time']))
                print(result_data)
                return result_data
            else:
                return False
        except Exception as e:
            print(e)
            traceback.print_exc(file=sys.stdout)
            pass
        

        
if __name__ == "__main__":
    
    try:
        models = Models()
        models.get_raw_data()
    except Exception as e:
        print(e)
        traceback.print_exc(file=sys.stdout)
        pass
        
        
        
