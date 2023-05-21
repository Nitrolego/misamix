#imports
from os import makedirs
from pydub import AudioSegment
from pathlib import Path
from shutil import copy, unpack_archive
from os.path import exists, join, dirname
from datetime import datetime
import logging

class MisaClass:
    def __init__(self, bfr_folder, new_folder, debug) -> None:
        #file path for folder for Misamino
        self.absolute_path = dirname(__file__)
        self.src_folder = join(self.absolute_path, "sfx/default")
        self.bfr_folder = bfr_folder
        self.new_folder = new_folder
        self.preprocess = join(self.bfr_folder, "preprocess")
        self.log_folder = join(self.absolute_path, "logs")
        self.req_folder = [self.bfr_folder, self.new_folder]
        for folder in self.req_folder:
            if not exists(folder):
                makedirs(folder)
        if debug == True:
            if not exists(join(self.log_folder)):
                makedirs(join(self.log_folder))
            now = datetime.utcnow().strftime("%Y-%m-%d-%H%M%S")
            logfile = join(self.log_folder, f"misamix-log-{now}.txt")
            logging.basicConfig(filename=logfile, level=logging.DEBUG, format='')


        #define dictionary for sfx search
        self.convertDict = {}
        self.convertDict['clearbtb'] = ['sfx_b2b_tetris','sfx_b2b_tspin_mini',
                           'sfx_b2b_tspin_single', 'sfx_b2b_tspin_double',
                           'sfx_b2b_tspin_triple']
        self.convertDict['clearline'] = ['sfx_single', 'sfx_double',
                                    'sfx_triple', 'sfx_lineattack']
        self.convertDict['clearspin'] = ['sfx_tspin_zero', 'sfx_tspin_mini',
                                    'sfx_tspin_single', 'sfx_tspin_double',
                                    'sfx_tspin_triple']
        self.convertDict['losestock'] = ['sfx_gameover', 'sfx_ko']
        self.convertDict['harddrop'] = ['sfx_harddrop']
        self.convertDict['hold'] = ['sfx_hold']
        self.convertDict['move'] = ['sfx_move']
        self.convertDict['rotate'] = ['sfx_rotate']
        self.convertDict['softdrop'] = ['sfx_softdrop']
        self.convertDict['clearquad'] = ['sfx_tetris']
        self.convertDict['allclear'] = ['sfx_perfectclear']
        for i in range(1,17):
            self.convertDict[f'combo_{i}'] = [f'sfx_combo{i}']
        self.convertDict['undefined'] = ['sfx_combo17', 'sfx_combo18',
                            'sfx_combo19', 'sfx_combo19',
                            'sfx_combo20', 'sfx_lockdown',
                            'sfx_movefail', 'sfx_rotatefail']
        
    #function to simplify exporting to WAV files
    def export_to_wav_from_ogg(self, path, misaname):
        song = AudioSegment.from_ogg(path)
        song.export(join(self.new_folder, f"{misaname}.wav"), format="wav")
        #print(f"converted {path.name} to {misaname}.wav successfully!")
        logging.debug(f"converted {path.name} to {misaname}.wav successfully!")
        #f string for easy identification of Misamino sfx names

    def export_to_wav_from_mp3(self, path, misaname):
        song = AudioSegment.from_mp3(path)
        song.export(join(self.new_folder, f"{misaname}.wav"), format="wav")
        #print(f"converted {path.name} to {misaname}.wav successfully!")
        logging.debug(f"converted {path.name} to {misaname}.wav successfully!")
        #f string for easy identification of Misamino sfx names

    def copy_from_wav_to_wav(self, path, misaname):
        copy(path, join(self.new_folder, f'{misaname}.wav'))
        #print(f"renamed {path.name} to {misaname}.wav successfully!")
        logging.debug(f"renamed {path.name} to {misaname}.wav successfully!")

    def replace_missing_sounds(self, oriname, misaname):
        copy(join(self.src_folder, f'{misaname}.wav'), self.new_folder)
        #print(f"replaced {oriname} with {misaname}.wav successfully!")
        logging.debug(f"replaced {oriname} with {misaname}.wav successfully!")

    def check_zip(self):
        #check if soundsfx folder is zipped, if zipped unzip
        zippaths = [path for path in Path(self.bfr_folder).rglob("*.zip")]
        preprocesspath = [path for path in Path(self.preprocess).rglob("*")]

        if zippaths and not preprocesspath:
            for path in zippaths:
                if not exists(self.preprocess):
                    makedirs(self.preprocess)
                unpack_archive(path, self.preprocess)
                #print(f"{path.name} unzipped successfully!")
                logging.debug(f"{path.name} unzipped successfully!")
        elif zippaths:
            #print("preprocess directory already occupied, skipping unpack")
            logging.debug("preprocess directory already occupied, skipping unpack")

    def main(self):
        self.check_zip()

        #Looping through all ogg, mp3, and wav files in before folder
        oggpaths = [path for path in Path(self.bfr_folder).rglob("*.ogg")]
        mp3paths = [path for path in Path(self.bfr_folder).rglob("*.mp3")]
        wavpaths = [path for path in Path(self.bfr_folder).rglob("*.wav")]

        allpaths = oggpaths + mp3paths + wavpaths

        #if folder is not empty, run logic
        if allpaths:
            #refactored processing of all file formats
            for path in allpaths:
                #print("processing: " + path.name)
                logging.debug("processing: " + path.name)
                for originalnames, misanames in self.convertDict.items():
                    #cheaty way of knowing when the loop reaches the end of the dictionary
                    if originalnames == "undefined":
                        #print("this sound does not exist in misamino")
                        logging.debug("this sound does not exist in misamino")
                        break
                    if path.name == f'{originalnames}.ogg':
                        for sfx in misanames:
                            self.export_to_wav_from_ogg(path, sfx)
                            continue
                        break
                    elif path.name == f'{originalnames}.mp3':
                        for sfx in misanames:
                            self.export_to_wav_from_mp3(path, sfx)
                            continue
                        break
                    elif path.name == f'{originalnames}.wav':
                        for sfx in misanames:
                            self.copy_from_wav_to_wav(path, sfx)
                            continue
                        break

            afterpaths = [path for path in Path(self.new_folder).rglob("*.wav")]
            #only check for missing files that need replacing after processing is over         
            for path in afterpaths:
                for originalnames, misanames in self.convertDict.items():
                    for sfx in misanames:
                        if not exists(join(self.new_folder, f'{sfx}.wav')):
                            self.replace_missing_sounds(originalnames, sfx)
                            continue
            return True

        #else, usually when the folder is empty or that the before folder is deleted.
        else:
            #print('empty folder, quitting')
            logging.debug('empty folder, quitting')
            return False