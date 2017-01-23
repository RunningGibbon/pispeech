#!/usr/bin/env python
from os import environ, path

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
import speech_recognition as sr

print("setting model directories")
MODELDIR = "../cmusphinx-nl-5.2/"

# Create a decoder with certain model
print("creating decoder.")
config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'model_parameters/voxforge_nl_sphinx.cd_cont_2000'))
config.set_string('-lm', path.join(MODELDIR, 'etc/voxforge_nl_sphinx.lm.bin'))
config.set_string('-dict', path.join(MODELDIR, 'etc/voxforge_nl_sphinx.dic'))
decoder = Decoder(config)

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


# Decode streaming data.
print("decoding streaming data")
decoder = Decoder(config)
decoder.start_utt()
stream = open(path.join(DATADIR, 'goforward.raw'), 'rb')
while True:
  buf = stream.read(1024)
  if buf:
    decoder.process_raw(buf, False, False)
  else:
    break
decoder.end_utt()
print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])