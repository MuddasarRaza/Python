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
client.loop_stop() #stop the loop
