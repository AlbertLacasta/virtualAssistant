import sys
import re

# modules
from speech import speak
import chrome
import date
from help import help
import joke
import aplication
import weather
from speech import speak


def assistant(command):

	if "how are you" in command:
		speak("i am well")
	elif "open " in command:
		reg_ex = re.search("open (.*)", command)
		chrome.open(reg_ex)
	elif "set up my desktop" in command:
		chrome.setupDesktop()
	elif "what date is today" in command:
		date.date()
	elif "what time is it" in command:
		date.time()
	elif "application" in command:
		reg_ex = re.search("application (.*)", command)
		application = reg_ex.group(1)
		aplication.open(application)
	elif "hello" in command:
		date.welcome()
	elif "help me" in command:
		help()
	elif "make a joke" in command:
		joke.makeJoke()
	elif "tell me about" in command:
		reg_ex = re.search('tell me about (.*)', command)
		chrome.about(reg_ex)
	elif "shut down" in command:
		speak('Bye bye Sir. Have a nice day')
		sys.exit()					
	elif "what is the weather in" in command:
		reg_ex = re.search('what is the weather in(.*)', command)
		weather.tellWeather(reg_ex)
	elif "i go outside" in command:
		speak("don't be idiot and stay at home")
