#imports
from os import makedirs
from pydub import AudioSegment
from pathlib import Path
from shutil import copy
from os.path import exists, join, dirname

#file path for folder for Misamino
absolute_path = dirname(__file__)
src_folder = join(absolute_path, "sfx/default")
bfr_folder = join(absolute_path, "before")
new_folder = join(absolute_path, "after/sfx/default")
req_folder = [bfr_folder, new_folder]
for folder in req_folder:
    if not exists(folder):
        makedirs(folder)

#function to simplify exporting to WAV files
def export_to_wav_from_ogg(path, misaname):
    song = AudioSegment.from_ogg(path)
    song.export(join(new_folder, f"{misaname}.wav"), format="wav")
    #f string for easy identification of Misamino sfx names

def export_to_wav_from_mp3(path, misaname):
    song = AudioSegment.from_mp3(path)
    song.export(join(new_folder, f"{misaname}.wav"), format="wav")
    #f string for easy identification of Misamino sfx names

#creating dictionary to link each file 
convertDict = {}

convertDict['clearbtb'] = ['sfx_b2b_tetris','sfx_b2b_tspin_mini',
                           'sfx_b2b_tspin_double','sfx_b2b_tspin_triple']
convertDict['clearline'] = ['sfx_single', 'sfx_double',
                            'sfx_triple', 'sfx_lineattack']
convertDict['clearspin'] = ['sfx_tspin_zero', 'sfx_tspin_mini',
                            'sfx_tspin_single', 'sfx_tspin_double',
                            'sfx_tspin_triple']
convertDict['losestock'] = ['sfx_gameover', 'sfx_ko']
convertDict['harddrop'] = ['sfx_harddrop']
convertDict['hold'] = ['sfx_hold']
convertDict['move'] = ['sfx_move']
convertDict['rotate'] = ['sfx_rotate']
convertDict['softdrop'] = ['sfx_softdrop']
convertDict['clearquad'] = ['sfx_tetris']
convertDict['allclear'] = ['sfx_perfectclear']
for i in range(1,17):
    convertDict[f'combo_{i}'] = [f'sfx_combo{i}']

#Looping through all ogg,mp3, and wav files in before folder
oggpaths = [path for path in Path(bfr_folder).rglob("*.ogg")]
mp3paths = [path for path in Path(bfr_folder).rglob("*.mp3")]
wavpaths = [path for path in Path(bfr_folder).rglob("*.wav")]

allpaths = oggpaths + mp3paths + wavpaths

#if folder is not empty, run logic
if allpaths:
    #refactored processing of all file formats
    for path in allpaths:
        print(path.name)
        for originalnames, misanames in convertDict.items():
            for sfx in misanames:
                if path.name == f'{originalnames}.ogg':
                    export_to_wav_from_ogg(path, f'{sfx}')
                    continue
                elif path.name == f'{originalnames}.mp3':
                    export_to_wav_from_mp3(path, f'{sfx}')
                    continue
                elif path.name == f'{originalnames}.wav':
                    copy(path, join(new_folder, f'{sfx}.wav'))
                    continue
                elif not exists(join(new_folder, f'{sfx}.wav')):
                    copy(join(src_folder, f'{sfx}.wav'), new_folder)
                    continue

    #The following sounds are not avaliable in most tetrio soundpacks
    copy(join(src_folder, "sfx_combo17.wav"), new_folder)
    copy(join(src_folder, "sfx_combo18.wav"), new_folder)
    copy(join(src_folder, "sfx_combo19.wav"), new_folder)
    copy(join(src_folder, "sfx_combo20.wav"), new_folder)
    copy(join(src_folder, "sfx_lockdown.wav"), new_folder)
    copy(join(src_folder, "sfx_movefail.wav"), new_folder)
    copy(join(src_folder, "sfx_rotatefail.wav"), new_folder)
#else, usually when the folder is empty or that the before folder is deleted.
else:
    print('empty folder, quitting')
    quit()