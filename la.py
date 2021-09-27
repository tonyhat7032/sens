#!/usr/bin/python

import requests , json
from datetime  import date, timedelta

tday = date.today()
yday = tday - timedelta(days=1)

u = 'https://api2.metvy.com/auth/users/message-report'

Bhagavan = {"rahul": 7207210608 , "Shitha": 9995054745 , "Soorya" : 7592010589  ,  "Debosmita" : 8335929288 , "Mansi" : 8826758257 ,  "Sheetal" : 9582951525, "Aashi" : 9368031141 , "Lavanya" : 9654161420 , "Ridhi" : 9953195026 , "Rushikesh" : 7093611014 }
Akhil = {"Ranu" : 8778178927 , "Ravinder " : 7680968360 ,  "Bhanu" : 9502953924 , "Dinesh" : 9515768511 , "Jeevan" : 7569788437 , "Jatin" : 6302016711  }
l = [Bhagavan,Akhil]

for k in range(len(l)):
    print("------------------------------------------------------------")
    send = []
    receive = []
    for j, i in l[k].items():
        p = {"startDate": str(yday) + "T18:30:00.000Z",
             "endDate": str(tday) + "T18:29:59.999Z",
             "mobile": i}
        r = requests.post(url=u, data=p).content
        data = json.loads(r)
        print(j,":",data)
        send.append(data["uniqueSendTo"])
        receive.append(data["uniqueReceiver"])
    sos = sum(send)
    sor = sum(receive)
    print("Sum of Msgs sent :", sos)
    print("Sum of Msgs received:", sor)
    print("Average reply rate =",(sor/sos)*100)
    print("------------------------------------------------------------")