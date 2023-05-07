#imports
import os

#determining file path
absolute_path = os.path.dirname(__file__)
before_path = "before/allclear.ogg"
after_path = "after/sfx_perfectclear.wav"
full_before_path = os.path.join(absolute_path, before_path)
full_after_path = os.path.join(absolute_path, after_path)

#os.rename(full_before_path, full_after_path)
#print("renamed")

#if no dir, make dir (default/sfx)

#pydub experimentation
from pydub import AudioSegment
song = AudioSegment.from_ogg(full_before_path)
song.export(full_after_path, format="wav")
