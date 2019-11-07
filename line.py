#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from datetime import date
import calendar
import datetime

def notify(message):
	payload = {'message':message}
	return _lineNotify(payload)

def notifyPicture(message,url):
	payload = {'message':message,'imageThumbnail':url,'imageFullsize':url}
	return _lineNotify(payload)

def notifySticker(message,stickerID,stickerPackageID):
	payload = {'message':message,'stickerPackageId':stickerPackageID,'stickerId':stickerID}
	return _lineNotify(payload)

def _lineNotify(payload):
	import requests
	url = 'https://notify-api.line.me/api/notify'
	token = 'bbDiYnBd6uPscxkK6hy43VV1BvemwX9ZmNzXbF9OAM7'
	headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
	return requests.post(url, headers=headers, data=payload)
    
my_date = date.today()
# dt = '25/03/2012'
# day, month, year = (int(x) for x in dt.split('/'))    
# my_date = datetime.date(year, month, day)

week_day = calendar.day_name[my_date.weekday()]
week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',  'Friday', 'Saturday']
#print (notify('สวัสดี hello'))
#print (notifySticker("สวัสดี ทดสอบส่งสติกเกอร์",2,1))
#print (notifyPicture("สวัสดี ทดสอบส่งรูปภาพ","https://pbs.twimg.com/media/D9b9p7GVAAAunxY.jpg"))
#print (notify(week_day))
if week_day == week[0] :
 	print (notifyPicture("สวัสดี วันอาทิตย์","https://cms.dmpcdn.com/women/2018/01/03/fc4a81f0-5344-4724-9cbf-5ccebb92abf2.jpg"))
elif  week_day == week[1] :
	print (notifyPicture("สวัสดี วันจันทร์","https://cms.dmpcdn.com/women/2018/01/03/7ea8225e-c1fe-425a-a3f2-47555201a713.jpg"))
elif  week_day == week[2] :
	print (notifyPicture("สวัสดี วันอังคาร","https://cms.dmpcdn.com/women/2018/01/03/b6a999cd-2130-4ca4-8729-4a4d350ee44a.jpg"))
elif  week_day == week[3] :
	print (notifyPicture("สวัสดี วันพุธ","https://cms.dmpcdn.com/women/2018/01/03/3bbf152b-dc8f-4917-af05-499ff8efcdd5.jpg"))
elif  week_day == week[4] :
	print (notifyPicture("สวัสดี วันพฤหัสบดี","https://cms.dmpcdn.com/women/2018/01/03/273f8c10-def6-48b3-ac20-1d029fc5717b.jpg"))
elif  week_day == week[5] :
	print (notifyPicture("สวัสดี วันศุกร์","https://cms.dmpcdn.com/women/2018/01/03/2d96f3b8-124c-4b36-81ba-426783dbc899.jpg"))
elif  week_day == week[6] :
	print (notifyPicture("สวัสดี วันเสาร์","https://cms.dmpcdn.com/women/2018/01/03/c370196f-efd7-47d4-ba2e-cd9e17be3839.jpg"))

