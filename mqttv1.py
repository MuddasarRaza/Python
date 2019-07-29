import paho.mqtt.client as mqtt #import the client1
import time
import psycopg2
import os
import json
global Dict
Dict = []        
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
        timestamp = Dict ['Value']['timestamp']
        print "Rotation_X_axis",Rot_x
        print "Rotation_Y_axis",Rot_y
        print "Rotation_Z_axis", Rot_z
        print "timestamp", timestamp
        conn = None
        try:
            conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="dbPassword")
            print "Connected to database"
            cur = conn.cursor()
            Postgres_insert_rot = """INSERT INTO rotation (rot_x_axis,rot_y_axis,rot_z_axis,timestamp) values (%s,%s,%s,%s)"""
            values_rotation = (Rot_x,Rot_y,Rot_z,timestamp)
            cur.execute(Postgres_insert_rot,values_rotation)
            print "data inserted for Rotation"
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
            
    elif Id == [50]:
        Acc_x = Dict['Value']['Acc-X-axis']
        Acc_y = Dict['Value']['Acc-Y-axis']
        Acc_z = Dict['Value']['Acc-Z-axis']
        timestamp = Dict ['Value']['timestamp']
        print "Acceleration_X_axis",Acc_x
        print "Acceleration_Y_axis",Acc_y
        print "Acceleration_Z_axis",Acc_z
        print "timestamp", timestamp
        conn = None
        try:
            conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="dbPassword")
            print "Connected to database"
            cur = conn.cursor()
            Postgres_insert_Acc = """INSERT INTO acceleration (Acc_x,Acc_y,Acc_z,timestamp) values (%s,%s,%s,%s)"""
            values_Acceleration = (Acc_x,Acc_y,Acc_z,timestamp)
            cur.execute(Postgres_insert_Acc,values_Acceleration)
            print "data inserted for Acceleration"
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        
    elif Id == [55]:
        Ang_x = Dict['Value']['Ang-X-axis']
        Ang_y = Dict['Value']['Ang-Y-axis']
        Ang_z = Dict['Value']['Ang-Z-axis']
        timestamp = Dict ['Value']['timestamp']
        print "timestamp", timestamp
        print "Ang-X-axis",Ang_x
        print "Ang-Y-axis",Ang_y
        print "Ang-Z-axis",Ang_z
        conn= None
        try:
            conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="dbPassword")
            print "Connected to database"
            cur = conn.cursor()
            Postgres_insert_Ang = """INSERT INTO angular (ang_x_axis,ang_y_axis,ang_z_axis,timestamp) values (%s,%s,%s,%s)"""
            values_Angular = (Ang_x,Ang_y,Ang_z,timestamp)
            cur.execute(Postgres_insert_Ang,values_Angular)
            print "data inserted for angular"
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        
    elif Id == [40]:
        Temp = Dict['Value']['Temperature']
        Air_Pressure = Dict['Value']['Luftdruck']
        Humidity = Dict['Value']['Luftfeuchtigkeit']
        timestamp = Dict ['Value']['timestamp']
        print "Temperature", Temp
        print "Humidity", Humidity
        print "AirPressure", Air_Pressure
        print "timestamp", timestamp
        conn = None
        try:
            conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="dbPassword")
            print "Connected to database"
            cur = conn.cursor()
            Postgres_insert_temp = """INSERT INTO environment (temperature,airpressure,humidity,timestamp) values (%s,%s,%s,%s)"""
            values_Env = (Temp,Air_Pressure,Humidity,timestamp)
            cur.execute(Postgres_insert_temp,values_Env)
            print "data inserted for Env"
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
def on_disconnect(client, userdata, message):
    if message != 0:
        print "Unexpected MQTT disconnection."
##        client.connect(broker_address)
        print "trying to reconnect"
        os.execv('/C/Python/mqttv1.py', [''])
        print "restarted"
        #client.loop_start()
def on_connect(client, userdata, message):
    print "Connected to broker"
    ##    #client.connect(broker_address)
##    client.loop_start() #start the loop
##    print "loop started"
##    print("Subscribing to Sensordata")
##    client.subscribe("#")
##    print "subscribed"
    
broker_address="192.168.10.150"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message
client.on_disconnect = on_disconnect
#client.on_connect = on_connect
print("connecting to broker")
client.connect(broker_address) #connect to broker
#client.loop_start() #start the loop
print("Subscribing to Sensordata")
client.subscribe("#")
#time.sleep(800)# If you want to wait
client.loop_forever()



