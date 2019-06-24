import paho.mqtt.client as mqtt #import the client1
import time
import json
global Dict
Dict = []
def on_message(client, userdata, message):
    #print(str(message.payload.decode("utf-8")))
    data = str(message.payload.decode("utf-8"))
    #print data
    Dict = json.loads(data)
##    print Dict
    Id = Dict['ID']
    print "ID",Id
    if Id == [45]:
        Rot_x = Dict['Value']['Rot-X-axis']
        Rot_y = Dict['Value']['Rot-Y-axis']
        Rot_z = Dict['Value']['Rot-Z-axis']
        print "Rotation_X_axis",Rot_x
        print "Rotation_Y_axis",Rot_y
        print "Rotation_Z_axis", Rot_z
    elif Id == [50]:
        Acc_x = Dict['Value']['Acc-X-axis']
        Acc_y = Dict['Value']['Acc-Y-axis']
        Acc_z = Dict['Value']['Acc-Z-axis']
        print "Acceleration_X_axis",Acc_x
        print "Acceleration_Y_axis",Acc_y
        print "Acceleration_Z_axis",Acc_z
    elif Id == [55]:
        Ang_x = Dict['Value']['Ang-X-axis']
        Ang_y = Dict['Value']['Ang-Y-axis']
        Ang_z = Dict['Value']['Ang-Z-axis']
        print "Ang-X-axis",Ang_x
        print "Ang-Y-axis",Ang_y
        print "Ang-Z-axis",Ang_z
    else Id == [40]
        Temp = Dict['Value']['Temperature']
        Air_Pressure = Dict['Value']['Luftdruck']
        Humidity = Dict['Value']['Luftfeuchtigkeit']
##    print "Acc-X-axis", Acc_x
##    Acc_y = Dict['Acc-Y-axis']
##    print "Acc-Y-axis", Acc_y
##    Acc_z = Dict['Acc-Z-axis']
##    print "Acc-Z-axis", Acc_z
##    Temp = Dict['Temperature']
##    print "Temperature", Temp
##    AirPressure = Dict['Luftdruck']
##    Humidity = Dict['Luftfeuchtigkeit']
##    Ang_x = Dict['Ang-X-axis']
##    Ang_Y = Dict['Ang-Y-axis']
##    Ang_Z = Dict['Ang-Z-axis']
##    Rot_x = Dict['Value']['Rot-X-axis']
##    Rot_y = Dict['Rot-Y-axis']
##    Rot_z = Dict['Rot-Z-axis']
##    
    
     
##    print "Acc-Y-axis", Acc_y
##    print "Acc-Z-axis", Acc_z
##    print "Temperature", Temp
##    print "Rot-X-axis", Rot_x

    
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
client.loop_stop() #stop the loop

