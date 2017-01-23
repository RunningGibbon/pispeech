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

decoder = Decoder(config)

with sr.Microphone() as source:
    print("Say something!")
    decoder.listen(source)

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + recognizer.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))