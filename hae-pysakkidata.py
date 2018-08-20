import paho.mqtt.subscribe as subscribe

viestit = subscribe.simple("/hfp/v1/journey/ongoing/tram/+/+/1008/#", hostname="mqtt.hsl.fi", msg_count=30, retained=True)
#1004 = nelosratikka, 1008 = kasiratikka

for msg in viestit:
    print("%s \n----\n %s" % (msg.topic, msg.payload))
    #x=1


import requests
