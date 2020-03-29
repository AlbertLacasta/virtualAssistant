from speech import speak	
import os

def open(application):
	sentence = "open -a {}".format(application)
	os.system(sentence)
	speak("I have opened the application {}".format(application))