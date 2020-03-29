import webbrowser
from speech import speak	
import wikipedia


# open website	
def open(reg_ex):
		if reg_ex:
			domain = reg_ex.group(1)
			url = "https://www." + domain
			webbrowser.open(url)
			print('browser opened')
			speak("The website you have requested has been opened for you")
		else:
			pass

def setupDesktop():
	websites = ["open.spotify.com", "www.youtube.com"]
	for web in websites:
		webbrowser.open("https://" + web)
		print("setup done")

	speak("your desktop is now set up")	

def about(reg_ex):
	try:
		if reg_ex:
			topic = reg_ex.group(1)
			ny = wikipedia.page(topic)
			speak(ny.content[:500].encode('utf-8'))
	except Exception as e:
		print(e)
		speak(e)	