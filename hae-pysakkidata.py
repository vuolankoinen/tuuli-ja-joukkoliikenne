#import paho.mqtt.subscribe as subscribe

#viestit = subscribe.simple("/hfp/v1/journey/ongoing/tram/+/+/1008/#", hostname="mqtt.hsl.fi", msg_count=30, retained=True)
# #1004 = nelosratikka, 1008 = kasiratikka

#for msg in viestit:
#    print("%s \n----\n %s" % (msg.topic, msg.payload))

import requests
from datetime import datetime # datetime(c)
import time

def query_HSY(q):
    d = requests.post('https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql', json={'query': q})
    return(d.json())

dataHSY = query_HSY('''
{
  cancelledTripTimes(
    feeds: ["HSL"]
    minDate: "2016-04-08"
    maxDate: "2019-06-21"
  ) {
    scheduledDeparture
    serviceDay
     trip {
      routeShortName
      directionId
      route {
        longName
      }
    }
    }
}''')

#print(dataHSY)

dataHSY = dataHSY['data']['cancelledTripTimes']

for hmm in dataHSY:
    # print('Pv {}, reitti {}, suunta {}'.format(time.ctime(hmm['serviceDay']), hmm['trip']['routeShortName'], hmm['trip']['directionId']))
    print('Pv {}, reitti {}, suunta {}'.format(time.strftime('%Y %B %d', time.localtime(hmm['serviceDay'])), hmm['trip']['routeShortName'], hmm['trip']['directionId']))




#  {
#    cancelledTripTimes(
#      feeds: ["HSL"]
#    ) {
#      scheduledDeparture
#      serviceDay
#      trip {
#        gtfsId
#        tripHeadsign
#        routeShortName
#        directionId
#        pattern {
#          code
#          name
#        }
#        route {
#          gtfsId
#          longName
#        }
#      }
#      realtimeState
#      headsign
#    }
#  }
