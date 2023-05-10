#imports
from os import makedirs
from pydub import AudioSegment
from pathlib import Path
from shutil import copy, unpack_archive
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
    print(f"converted {path.name} to {misaname}.wav successfully!")
    #f string for easy identification of Misamino sfx names

def export_to_wav_from_mp3(path, misaname):
    song = AudioSegment.from_mp3(path)
    song.export(join(new_folder, f"{misaname}.wav"), format="wav")
    print(f"converted {path.name} to {misaname}.wav successfully!")
    #f string for easy identification of Misamino sfx names

def copy_from_wav_to_wav(path, misaname):
    copy(path, join(new_folder, f'{misaname}.wav'))
    print(f"renamed {path.name} to {misaname}.wav successfully!")

def replace_missing_sounds(oriname, misaname):
    copy(join(src_folder, f'{misaname}.wav'), new_folder)
    print(f"replaced {oriname} with {misaname}.wav successfully!")

#creating dictionary to link each file 
convertDict = {}

convertDict['clearbtb'] = ['sfx_b2b_tetris','sfx_b2b_tspin_mini',
                           'sfx_b2b_tspin_single', 'sfx_b2b_tspin_double',
                           'sfx_b2b_tspin_triple']
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
convertDict['undefined'] = ['sfx_combo17', 'sfx_combo18',
                            'sfx_combo19', 'sfx_combo19',
                            'sfx_combo20', 'sfx_lockdown',
                            'sfx_movefail', 'sfx_rotatefail']

#if soundsfx is zipped, unzip
zippaths = [path for path in Path(bfr_folder).rglob("*.zip")]

if zippaths:
    for path in zippaths:
        preprocess = join(bfr_folder, "preprocess")
        if not exists(preprocess):
            makedirs(preprocess)
        unpack_archive(path, preprocess)

#Looping through all ogg,mp3, and wav files in before folder
oggpaths = [path for path in Path(bfr_folder).rglob("*.ogg")]
mp3paths = [path for path in Path(bfr_folder).rglob("*.mp3")]
wavpaths = [path for path in Path(bfr_folder).rglob("*.wav")]

allpaths = oggpaths + mp3paths + wavpaths

#if folder is not empty, run logic
if allpaths:
    #refactored processing of all file formats
    for path in allpaths:
        print("processing: " + path.name)
        for originalnames, misanames in convertDict.items():
            #cheaty way of knowing when the loop reaches the end of the dictionary
            if originalnames == "undefined":
                print("this sound does not exist in misamino")
                break
            if path.name == f'{originalnames}.ogg':
                for sfx in misanames:
                    export_to_wav_from_ogg(path, sfx)
                    continue
                break
            elif path.name == f'{originalnames}.mp3':
                for sfx in misanames:
                    export_to_wav_from_mp3(path, sfx)
                    continue
                break
            elif path.name == f'{originalnames}.wav':
                for sfx in misanames:
                    copy_from_wav_to_wav(path, sfx)
                    continue
                break

    afterpaths = [path for path in Path(new_folder).rglob("*.wav")]
    #only check for missing files that need replacing after processing is over         
    for path in afterpaths:
        for originalnames, misanames in convertDict.items():
            for sfx in misanames:
                if not exists(join(new_folder, f'{sfx}.wav')):
                    replace_missing_sounds(originalnames, sfx)
                    continue

#else, usually when the folder is empty or that the before folder is deleted.
else:
    print('empty folder, quitting')
    quit()