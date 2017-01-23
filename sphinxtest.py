#!/usr/bin/env python
from os import environ, path

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

print("setting model directories")
MODELDIR = "cmusphinx-nl-5.2/"
DATADIR = "pocketsphinx/test/data"

# Create a decoder with certain model
print("creating decoder.")
config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'model_parameters/voxforge_nl_sphinx.cd_cont_2000'))
config.set_string('-lm', path.join(MODELDIR, 'etc/voxforge_nl_sphinx.lm.bin'))
config.set_string('-dict', path.join(MODELDIR, 'etc/voxforge_nl_sphinx.dic'))
decoder = Decoder(config)

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