
import pyttsx3

def speak(audioString):

	converter = pyttsx3.init()

	# set speed of speak
	converter.setProperty('rate', 200)
	
	#set volume
	converter.setProperty('volumne', 0.7)

	# set voice
	voice_id = "com.apple.speech.synthesis.voice.Victoria"
	converter.setProperty('voice', voice_id)

	# Queue the entered text  
	# There will be a pause between 
	# each one like a pause in  
	# a sentence 
	converter.say(audioString)

	# Empties the say() queue 
	# Program will not continue 
	# until all speech is done talking 
	converter.runAndWait()