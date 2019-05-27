import paho.mqtt.client as mqtt #import the client1
import time
import json
def on_message(client, userdata, message):
    #print(str(message.payload.decode("utf-8")))
    data = str(message.payload.decode("utf-8"))
    #print data
    Dict = json.loads(data)
    params = Dict.get("Acc",None)
    Acc = params.get('Acc-X-axis')
    print 'acc:' + str(Acc)
broker_address="192.168.10.150"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","house/bulbs/bulb1")
client.subscribe("#")
time.sleep(20) # wait
client.loop_stop()
#stop the loop

#############################################
###########################################
import psycopg2
from config import config
 
 
def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE Acceleration (
                Acc_X INTEGER NOT NULL,
                Acc_Y INTEGER NOT NULL
git chec
        )
        """,
        """ CREATE TABLE Temp (
                Temp INTEGER NOT NULL,
                Humidity INTEGER NOT NULL 
                )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(host="192.168.10.50", database="datalogdb", user="postgres", password="dbPassword")
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.open()
 
 
if __name__ == '__main__':::::::::::::::::::::
    create_tables()
    #######################################
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(host="192.168.10.50", database="datalogdb", user="postgres", password="dbPassword")
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.open()
