import paho.mqtt.client as mqtt #import the client1
import time
import psycopg2
import json
global Dict
Dict = []
##class ManageDatabase():
##   def __init__(self):
##        self.conn = psycopg2.connect(host="172.27.40.97", database="postgres", user="postgres", password="dbPassword")
##        self.conn.commit()
##        self.cur = self.conn.cursor()
##   def add_del_update_db_record(self, sql_query, args=()):
##        self.cur.execute(sql_query, args)
##        self.conn.commit()
##        return
##   def __del__(self):
##        self.cur.close()
##        self.conn.close()       
    
def on_message(client, userdata, message):
    print "Data Received"
    data = str(message.payload.decode("utf-8"))
    Dict = json.loads(data)
    Id = Dict['ID']
    print "ID",Id
    if Id == [45]:
        Rot_x = Dict['Value']['Rot-X-axis']
        Rot_y = Dict['Value']['Rot-Y-axis']
        Rot_z = Dict['Value']['Rot-Z-axis']
        print "Rotation_X_axis",Rot_x
        print "Rotation_Y_axis",Rot_y
        print "Rotation_Z_axis", Rot_z
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="dbPassword")
        print "Connected"
        cur = conn.cursor()
        print "cur"
        Postgres_insert = """INSERT INTO rotation (rot_x_axis,rot_y_axis,rot_z_axis) values (%s,%s,%s)"""
        values_rotation = (Rot_x,Rot_y,Rot_z)
        cur.execute(Postgres_insert,values_rotation)
        print "data inserted"
        conn.commit()
        conn.close()

    elif Id == [50]:
        Acc_x = Dict['Value']['Acc-X-axis']
        Acc_y = Dict['Value']['Acc-Y-axis']
        Acc_z = Dict['Value']['Acc-Z-axis']
        print "Acceleration_X_axis",Acc_x
        print "Acceleration_Y_axis",Acc_y
        print "Acceleration_Z_axis",Acc_z
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="dbPassword")
        print "Connected"
        cur = conn.cursor()
        print "cur"
        Postgres_insert_Acc = """INSERT INTO acceleration (Acc_x,Acc_y,Acc_z) values (%s,%s,%s)"""
        values_Acceleration = (Acc_x,Acc_y,Acc_z)
        cur.execute(Postgres_insert_Acc,values_Acceleration)
        print "data inserted for Acceleration"
        conn.commit()
        conn.close()
    elif Id == [55]:
        Ang_x = Dict['Value']['Ang-X-axis']
        Ang_y = Dict['Value']['Ang-Y-axis']
        Ang_z = Dict['Value']['Ang-Z-axis']
        print "Ang-X-axis",Ang_x
        print "Ang-Y-axis",Ang_y
        print "Ang-Z-axis",Ang_z
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="dbPassword")
        print "Connected"
        cur = conn.cursor()
        print "cur"
        Postgres_insert_Ang = """INSERT INTO angular (ang_x_axis,ang_y_axis,ang_z_axis) values (%s,%s,%s)"""
        values_Angular = (Ang_x,Ang_y,Ang_z)
        cur.execute(Postgres_insert_Acc,values_Angular)
        print "data inserted for angular"
        conn.commit()
        conn.close()
    elif Id == [40]:
        Temp = Dict['Value']['Temperature']
        Air_Pressure = Dict['Value']['Luftdruck']
        Humidity = Dict['Value']['Luftfeuchtigkeit']
        print "Temperature", Temp
        print "Humidity", Humidity
        print "AirPressure", Air_Pressure
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="dbPassword")
        print "Connected"
        cur = conn.cursor()
        print "cur"
        Postgres_insert_Ang = """INSERT INTO environment (temperature,airpressure,humidity) values (%s,%s,%s)"""
        values_Env = (Temp,Air_Pressure,Humidity)
        cur.execute(Postgres_insert_Acc,values_Env)
        print "data inserted for Env"
        conn.commit()
        conn.close()

 
broker_address="192.168.10.150"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to Sensordata")
client.subscribe("#")
time.sleep(20) # wait
client.loop_forever() #stop the loop

