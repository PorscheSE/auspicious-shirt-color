#from line_notify import LineNotify
import pandas as pd
from datetime import date
import datetime 
import calendar

def findDay(date): 
    born = datetime.datetime.strptime(date, '%Y-%m-%d').weekday() 
    return (calendar.day_name[born]) 

def lineNotify(message):
    payload = {'message':message}
    return _lineNotify(payload)

def notifyFile(filename):
    file = {'imageFile':open(filename,'rb')}
    payload = {'message': 'test'}
    return _lineNotify(payload,file)

def notifyPicture(url):
    payload = {'message':" ",'imageThumbnail':url,'imageFullsize':url}
    return _lineNotify(payload)

def notifySticker(stickerID,stickerPackageID):
    payload = {'message':" ",'stickerPackageId':stickerPackageID,'stickerId':stickerID}
    return _lineNotify(payload)

def _lineNotify(payload,file=None):
    import requests
    url = 'https://notify-api.line.me/api/notify'
    token = 'AeMslSf497dIxzDRpuowSA9RC6RQ4667NeIVnMJ0RuN'	#EDIT
    headers = {'Authorization':'Bearer '+token}
    return requests.post(url, headers=headers , data = payload, files=file)

#ACCESS_TOKEN = "AeMslSf497dIxzDRpuowSA9RC6RQ4667NeIVnMJ0RuN"
#ACCESS_TOKEN = "ZczbHt4HlJdd0rqq4QCgjTt9vlGDx4kN7hoJ9rgkGy9"

week= ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
if findDay(str(date.today())) == week[1]:
    notifyPicture('https://cms.dmpcdn.com/women/2018/01/03/7ea8225e-c1fe-425a-a3f2-47555201a713.jpg')
elif findDay(str(date.today())) == week[2]:
    notifyPicture('https://cms.dmpcdn.com/women/2018/01/03/b6a999cd-2130-4ca4-8729-4a4d350ee44a.jpg')
elif findDay(str(date.today())) == week[3]:
    notifyPicture('https://cms.dmpcdn.com/women/2018/01/03/3bbf152b-dc8f-4917-af05-499ff8efcdd5.jpg')
elif findDay(str(date.today())) == week[4]:
    notifyPicture('https://cms.dmpcdn.com/women/2018/01/03/273f8c10-def6-48b3-ac20-1d029fc5717b.jpg')
elif findDay(str(date.today())) == week[5]:
    notifyPicture('https://cms.dmpcdn.com/women/2018/01/03/2d96f3b8-124c-4b36-81ba-426783dbc899.jpg')
elif findDay(str(date.today())) == week[6]:
    notifyPicture('https://cms.dmpcdn.com/women/2018/01/03/c370196f-efd7-47d4-ba2e-cd9e17be3839.jpg')
elif findDay(str(date.today())) == week[0]:
    notifyPicture('https://cms.dmpcdn.com/women/2018/01/03/fc4a81f0-5344-4724-9cbf-5ccebb92abf2.jpg')


