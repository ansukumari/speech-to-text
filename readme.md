- activate virtualenv


**using python speech recognition - google api**
---
- `pip install SpeechRecognition`
- `python`
	> \>\>\> import speech_recognition as sr <br>
	> \>\>\> sr.\_\_version__ <br>
	'3.8.1'
- `python main.py`
	> error: if not isinstance(actual_result, dict) or len(actual_result.get("alternative", [])) == 0: raise UnknownValueError()<br>speech_recognition.UnknownValueError
- change main.py from `r.recognize_google(audio)` to `r.recognize_google(audio, show_all=True)`
	> output: []<br>
	(maybe because earlier google provided a generic key for recognition that it revoked lately. to get your personal key create account on google cloud and change code to r.recognize_google(audio, key='GOOGLE_KEY', show_all=True))


**using google speech-to-text api directly**
---
- visit: https://cloud.google.com/speech-to-text/docs/sync-recognize
- `pip install --upgrade google-cloud-speech`
- `export GOOGLE_APPLICATION_CREDENTIALS=~/Downloads/ofcred.json`
- run speech detection code: google_speech.py
	> error: google.api_core.exceptions.InvalidArgument: 400 sample_rate_hertz (16000) in RecognitionConfig must either be omitted 	or match the value in the WAV header ( 44100)
- remove line sample_rate_hertz=16000 from code, run file again
	> error: google.api_core.exceptions.InvalidArgument: 400 Must use single channel (mono) audio, but WAV header indicates 2 channels.
- try to convert 2 channels to mono: https://github.com/jiaaro/pydub/issues/246 (or find a single channel audio)<br>
... to be continued


**using python speech recognition - sphinx**
---
- change the code from `r.recognize_google(audio, show_all=True)` to `r.recognize_sphinx(audio, show_all=True)`
- install pocketsphinx: 
	> `sudo apt-get install python3 python3-all-dev python3-pip build-essential swig git libpulse-dev libasound2-dev`<br>
	`pip install pocketsphinx`
- print(r.recognize_google(audio, show_all=True))
	> output: <pocketsphinx.pocketsphinx.Decoder; proxy of <Swig Object of type 'Decoder *' at 0x7fa991076750> >
- print(r.recognize_google(audio)
	> output: this they'll smell of old we're lingers it takes heat to bring out the odor called it restores health and zest case all the colt is fine with him couples all pastore my favorite is as full food is the hot cross mon


**using mic for speach recognition**
---
- install pyaudio
	> `sudo apt-get install python-pyaudio python3-pyaudio`<br>
	`sudo apt-get install libjack-jackd2-dev portaudio19-dev`<br>
	`pip install pyaudio`<br>
- run the default listening script: `python -m speech_recognition`


**important links**
---
- https://realpython.com/python-speech-recognition/
- https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst
- https://pypi.org/project/SpeechRecognition/3.1.2/
- https://cloud.google.com/speech-to-text/docs/sync-recognize