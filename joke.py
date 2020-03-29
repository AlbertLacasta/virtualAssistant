import requests
from speech import speak	

def makeJoke():
	res = requests.get(
			'https://icanhazdadjoke.com/',
			headers={"Accept":"application/json"})
	if res.status_code == requests.codes.ok:
		speak(str(res.json()['joke']))
	else:
		speak('oops!I ran out of jokes')