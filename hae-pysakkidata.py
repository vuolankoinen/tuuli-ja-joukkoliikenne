Import paho.mqtt.client as mqtt

lukija =mqtt.Client("ratikka")

lukija.connect("mqtt.hsl.fi")

lukija.subscribe("/hfp/v1/journey/ongoing/tram/#")
