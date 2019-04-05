# Recognizing speech using Sphinx since google ain't converting for some reason
# To recognize using google api change line `r.recognize_sphinx(audio)` to `r.recognize_google(audio)`

import speech_recognition as sr
r = sr.Recognizer()

def convertSpeech(file=None):
	if file:
		harvard = sr.AudioFile(file)
		with harvard as source: audio = r.record(source)
		print('converting...')
		print(r.recognize_sphinx(audio))

	else:
		with sr.Microphone() as source:
			print('say something...')
			audio = r.listen(source)
			print(r.recognize_sphinx(audio))

if __name__ == '__main__':
	ans = input('Do you want to use mic? (y/n): ')
	if ans == 'n': 
		file = input('Enter the file name that needs to be converted (Leave blank to use default file): ')
		if file: convertSpeech(file)
		else: convertSpeech('audio_files/harvard.wav')
	else: convertSpeech()