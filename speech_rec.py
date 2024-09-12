
import speech_recognition as sr
from gtts import gTTS 
import os
import sys
import webbrowser

#print(sr.Microphone.list_microphone_names()) #Index of Micro
microId = 3

webbrowser.register('Opera', None, webbrowser.BackgroundBrowser('C:/Users/user/AppData/Local/Programs/Opera GX/launcher.exe'))

def talk (words):
	speech = gTTS(text = words, lang = 'en', slow = False)
	print(words)
	speech.save('talk.mp3')
	os.system('start talk.mp3')


talk('Connection complete!')


def command():
	r = sr.Recognizer()
	task = ""

	with sr.Microphone(device_index=microId) as source:
		print('Say')

		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source, duration = 1)

		audio = r.listen(source)

	try:
		task = r.recognize_google(audio, language = 'en-EN').lower()

		text = 'You said: ' + task
		print(text)

	except sr.UnknownValueError:
		if 'bro' in task:
			talk('I did not understand what you meant')

	return task


def makeTask(task):
	if 'bro' in task:
		if 'open web' in task:
			talk("Already open!")
			url = 'https://www.google.com'
			webbrowser.open(url)

while True:
    task = command()
    if task:
        makeTask(task)
