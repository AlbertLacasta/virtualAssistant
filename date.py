
import datetime
from speech import speak

currentDate = datetime.datetime.now()

def date():
	date = currentDate.strftime("%a %m %Y")
	speak(date)

def time():
	time = currentDate.strftime("%H:%M")
	speak(time)	

def welcome():
	day_time = int(currentDate.strftime('%H'))
	if day_time < 12:
		speak('Hello Albert. Good morning')
	elif 12 <= day_time < 18:
		speak('Hello Albert. Good afternoon')
	else:
		speak('Hello Albert. Good evening')	