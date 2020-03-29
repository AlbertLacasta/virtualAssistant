
import speech_recognition as sr

#modules 
from speech import speak

#assistant
from assistant import assistant

# assistant listen for voice
def assistantCommand():

	r = sr.Recognizer()

	with sr.Microphone() as source:
		print("listen...")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source, duration=1)

		audio = r.listen(source)
		try:
			command = r.recognize_google(audio).lower()
			print("you said: {}".format(command))

		# if the command is not known continue to listen  
		except sr.UnknownValueError:
			speak("Sorry could not recognize what you said")
			command = assistantCommand()

	return command
		 
speak("Hello Albert, what can i help you?")

#loop to continue executing multiple commands
while True:
	assistant(assistantCommand())