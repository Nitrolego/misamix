#imports
import os
from pydub import AudioSegment
from pathlib import Path
import shutil
from os.path import exists, join, dirname

#file path for folder for Misamino
absolute_path = dirname(__file__)

src_folder = join(absolute_path, "sfx/default")

new_folder = join(absolute_path, "after/sfx/default")
if not exists(new_folder):
    os.makedirs(new_folder)

#function to simplify exporting to WAV files
def export_to_wav_from_ogg(path, misaname):
    song = AudioSegment.from_ogg(path)
    song.export(join(new_folder, f"{misaname}.wav"), 
                    format="wav")
    #f string for easy identification of Misamino sfx names

def export_to_wav_from_mp3(path, misaname):
    song = AudioSegment.from_mp3(path)
    song.export(join(new_folder, f"{misaname}.wav"), 
                    format="wav")
    #f string for easy identification of Misamino sfx names

#Looping through all ogg files in repository to convert to WAV
oggpaths = [path for path in Path(absolute_path).rglob("*.ogg")]
mp3paths = [path for path in Path(absolute_path).rglob("*.mp3")]

allpaths = oggpaths + mp3paths

for path in allpaths:
    print(path.name)
    if path.name == "clearbtb.ogg":
        export_to_wav_from_ogg(path, "sfx_b2b_tetris")
        export_to_wav_from_ogg(path, "sfx_b2b_tspin_mini")
        export_to_wav_from_ogg(path, "sfx_b2b_tspin_single")
        export_to_wav_from_ogg(path, "sfx_b2b_tspin_double")
        export_to_wav_from_ogg(path, "sfx_b2b_tspin_triple")
        continue
    if path.name == "clearbtb.mp3":
        export_to_wav_from_mp3(path, "sfx_b2b_tetris")
        export_to_wav_from_mp3(path, "sfx_b2b_tspin_mini")
        export_to_wav_from_mp3(path, "sfx_b2b_tspin_single")
        export_to_wav_from_mp3(path, "sfx_b2b_tspin_double")
        export_to_wav_from_mp3(path, "sfx_b2b_tspin_triple")
        continue
    #elif statements to replace the file should it not exist
    elif exists(join(new_folder, "sfx_b2b_tetris.wav")) == False:
        shutil.copy(join(src_folder, "sfx_b2b_tetris.wav"), new_folder)
    elif exists(join(new_folder, "sfx_b2b_tspin_mini.wav")) == False:
        shutil.copy(join(src_folder, "sfx_b2b_tspin_mini.wav"), new_folder)
    elif exists(join(new_folder, "sfx_b2b_tspin_single.wav")) == False:
        shutil.copy(join(src_folder, "sfx_b2b_tspin_single.wav"), new_folder)
    elif exists(join(new_folder, "sfx_b2b_tspin_double.wav")) == False:
        shutil.copy(join(src_folder, "sfx_b2b_tspin_double.wav"), new_folder)
    elif exists(join(new_folder, "sfx_b2b_tspin_triple.wav")) == False:
        shutil.copy(join(src_folder, "sfx_b2b_tspin_triple.wav"), new_folder)
        continue

    if path.name == "clearline.ogg":
        export_to_wav_from_ogg(path, "sfx_single")
        export_to_wav_from_ogg(path, "sfx_double")
        export_to_wav_from_ogg(path, "sfx_triple")
        export_to_wav_from_ogg(path, "sfx_lineattack")
        continue
    elif path.name == "clearline.mp3":
        export_to_wav_from_mp3(path, "sfx_single")
        export_to_wav_from_mp3(path, "sfx_double")
        export_to_wav_from_mp3(path, "sfx_triple")
        export_to_wav_from_mp3(path, "sfx_lineattack")
        continue
    elif exists(join(new_folder, "sfx_single.wav")) == False:
        shutil.copy(join(src_folder, "sfx_single.wav"), new_folder)
    elif exists(join(new_folder, "sfx_double.wav")) == False:
        shutil.copy(join(src_folder, "sfx_double.wav"), new_folder)
    elif exists(join(new_folder, "sfx_triple.wav")) == False:
        shutil.copy(join(src_folder, "sfx_triple.wav"), new_folder)
    elif exists(join(new_folder, "sfx_lineattack.wav")) == False:
        shutil.copy(join(src_folder, "sfx_lineattack.wav"), new_folder)
        continue

    if path.name == "clearspin.ogg":
        export_to_wav_from_ogg(path, "sfx_tspin_zero")
        export_to_wav_from_ogg(path, "sfx_tspin_mini")
        export_to_wav_from_ogg(path, "sfx_tspin_single")
        export_to_wav_from_ogg(path, "sfx_tspin_double")
        export_to_wav_from_ogg(path, "sfx_tspin_triple")
        continue
    elif path.name == "clearspin.mp3":
        export_to_wav_from_mp3(path, "sfx_tspin_zero")
        export_to_wav_from_mp3(path, "sfx_tspin_mini")
        export_to_wav_from_mp3(path, "sfx_tspin_single")
        export_to_wav_from_mp3(path, "sfx_tspin_double")
        export_to_wav_from_mp3(path, "sfx_tspin_triple")
        continue
    elif exists(join(new_folder, "sfx_tspin_zero.wav")) == False:
        shutil.copy(join(src_folder, "sfx_tspin_zero.wav"), new_folder)
    elif exists(join(new_folder, "sfx_tspin_zero.wav")) == False:
        shutil.copy(join(src_folder, "sfx_tspin_mini.wav"), new_folder)
    elif exists(join(new_folder, "sfx_tspin_zero.wav")) == False:
        shutil.copy(join(src_folder, "sfx_tspin_single.wav"), new_folder)
    elif exists(join(new_folder, "sfx_tspin_zero.wav")) == False:
        shutil.copy(join(src_folder, "sfx_tspin_double.wav"), new_folder)
    elif exists(join(new_folder, "sfx_tspin_zero.wav")) == False:
        shutil.copy(join(src_folder, "sfx_tspin_triple.wav"), new_folder)
        continue 

    if path.name == "losestock.ogg":
        export_to_wav_from_ogg(path, "sfx_gameover")
        export_to_wav_from_ogg(path, "sfx_ko")
        continue
    elif path.name == "losestock.mp3":
        export_to_wav_from_mp3(path, "sfx_gameover")
        export_to_wav_from_mp3(path, "sfx_ko")
        continue
    elif exists(join(new_folder, "sfx_gameover.wav")) == False:
        shutil.copy(join(src_folder, "sfx_gameover.wav"), new_folder)
    elif exists(join(new_folder, "sfx_ko.wav")) == False:
        shutil.copy(join(src_folder, "sfx_ko.wav"), new_folder)
        continue

    if path.name == "harddrop.ogg":
        export_to_wav_from_ogg(path, "sfx_harddrop")
        continue
    elif path.name == "harddrop.mp3":
        export_to_wav_from_mp3(path, "sfx_harddrop")
        continue
    elif exists(join(new_folder, "sfx_harddrop.wav")) == False:
        shutil.copy(join(src_folder, "sfx_harddrop.wav"), new_folder)
        continue

    if path.name == "hold.ogg":
        export_to_wav_from_ogg(path, "sfx_hold")
        continue
    elif path.name == "hold.mp3":
        export_to_wav_from_mp3(path, "sfx_hold")
        continue
    elif exists(join(new_folder, "sfx_hold.wav")) == False:
         shutil.copy(join(src_folder, "sfx_hold.wav"), new_folder)
         continue

    if path.name == "move.ogg":
        export_to_wav_from_ogg(path, "sfx_move")
        continue
    elif path.name == "move.mp3":
        export_to_wav_from_mp3(path, "sfx_move")
        continue
    elif exists(join(new_folder, "sfx_move.wav")) == False:
         shutil.copy(join(src_folder, "sfx_move.wav"), new_folder)
         continue

    if path.name == "rotate.ogg":
        export_to_wav_from_ogg(path, "sfx_rotate")
        continue
    if path.name == "rotate.mp3":
        export_to_wav_from_mp3(path, "sfx_rotate")
        continue
    elif exists(join(new_folder, "sfx_rotate.wav")) == False:
        shutil.copy(join(src_folder, "sfx_rotate.wav"), new_folder)
        continue

    if path.name == "softdrop.ogg":
        export_to_wav_from_ogg(path, "sfx_softdrop")
        continue
    elif path.name == "softdrop.mp3":
        export_to_wav_from_mp3(path, "sfx_softdrop")
        continue
    elif exists(join(new_folder, "sfx_softdrop.wav")) == False:
        shutil.copy(join(src_folder, "sfx_softdrop.wav"), new_folder)
        continue

    if path.name == "clearquad.ogg":
        export_to_wav_from_ogg(path, "sfx_tetris")
        continue
    elif path.name == "clearquad.mp3":
        export_to_wav_from_mp3(path, "sfx_tetris")
        continue
    elif exists(join(new_folder, "sfx_tetris.wav")) == False:
        shutil.copy(join(src_folder, "sfx_tetris.wav"), new_folder)
        continue

    if path.name == "allclear.ogg":
        export_to_wav_from_ogg(path, "sfx_perfectclear")
        continue
    elif path.name == "allclear.mp3":
        export_to_wav_from_mp3(path, "sfx_perfectclear")
        continue
    elif exists(join(new_folder, "sfx_perfectclear.wav")) == False:
        shutil.copy(join(src_folder, "sfx_perfectclear.wav"), new_folder)
        continue
        
    if path.name == "combo_1.ogg":
        export_to_wav_from_ogg(path, "sfx_combo1")
        continue
    elif path.name == "combo_1.mp3":
        export_to_wav_from_mp3(path, "sfx_combo1")
        continue
    elif exists(join(new_folder, "sfx_combo1.wav")) == False:
        shutil.copy(join(src_folder, "sfx_combo1.wav"), new_folder)
        continue

    if path.name == "combo_2.ogg":
        export_to_wav_from_ogg(path, "sfx_combo2")
        continue
    elif path.name == "combo_2.mp3":
        export_to_wav_from_mp3(path, "sfx_combo2")
        continue
    elif exists(join(new_folder, "sfx_combo2.wav")) == False:
        shutil.copy(join(src_folder, "sfx_combo2.wav"), new_folder)
        continue

    if path.name == "combo_3.ogg":
        export_to_wav_from_ogg(path, "sfx_combo3")
        continue
    elif path.name == "combo_3.mp3":
        export_to_wav_from_mp3(path, "sfx_combo3")
        continue
    elif exists(join(new_folder, "sfx_combo3.wav")) == False:
        shutil.copy(join(src_folder, "sfx_combo3.wav"), new_folder)
        continue

    if path.name == "combo_4.ogg":
        export_to_wav_from_ogg(path, "sfx_combo4")
        continue
    elif path.name == "combo_4.mp3":
        export_to_wav_from_mp3(path, "sfx_combo4")
        continue
    elif exists(join(new_folder, "sfx_combo4.wav")) == False:
        shutil.copy(join(src_folder, "sfx_combo4.wav"), new_folder)
        continue

    if path.name == "combo_5.ogg":
        export_to_wav_from_ogg(path, "sfx_combo5")
        continue
    elif path.name == "combo_5.mp3":
        export_to_wav_from_mp3(path, "sfx_combo5")
        continue
    elif exists(join(new_folder, "sfx_combo5.wav")) == False:
        shutil.copy(join(src_folder, "sfx_combo5.wav"), new_folder)
        continue

    if path.name == "combo_6.ogg":
        export_to_wav_from_ogg(path, "sfx_combo6")
        continue
    elif path.name == "combo_6.mp3":
        export_to_wav_from_mp3(path, "sfx_combo6")
        continue
    elif exists(join(new_folder, "sfx_combo6.wav")) == False:
        shutil.copy(join(src_folder, "sfx_combo6.wav"), new_folder)
        continue

    if path.name == "combo_7.ogg":
        export_to_wav_from_ogg(path, "sfx_combo7")
        continue
    elif path.name == "combo_7.mp3":
        export_to_wav_from_mp3(path, "sfx_combo7")
        continue
    elif exists(join(new_folder, "sfx_combo7.wav")) == False:
        shutil.copy(join(src_folder, "sfx_combo7.wav"), new_folder)
        continue

    if path.name == "combo_8.ogg":
        export_to_wav_from_ogg(path, "sfx_combo8")
        continue
    elif path.name == "combo_8.mp3":
        export_to_wav_from_mp3(path, "sfx_combo8")
        continue
    elif exists(join(new_folder, "sfx_combo8.wav")) == False:
        shutil.copy(join(src_folder, "sfx_combo8.wav"), new_folder)
        continue

    if path.name == "combo_9.ogg":
        export_to_wav_from_ogg(path, "sfx_combo9")
        continue
    elif path.name == "combo_9.mp3":
        export_to_wav_from_mp3(path, "sfx_combo9")
        continue
    elif exists(join(new_folder, "sfx_combo9.wav")) == False:
        shutil.copy(join(src_folder, "sfx_combo9.wav"), new_folder)
        continue

    if path.name == "combo_10.ogg":
        export_to_wav_from_ogg(path, "sfx_combo10")
        continue
    elif path.name == "combo_10.mp3":
        export_to_wav_from_mp3(path, "sfx_combo10")
        continue
    elif exists(join(new_folder, "sfx_combo10.wav")) == False:
        shutil.copy(join(src_folder, "sfx_combo10.wav"), new_folder)
        continue

    if path.name == "combo_11.ogg":
        export_to_wav_from_ogg(path, "sfx_combo11")
        continue
    elif path.name == "combo_11.mp3":
        export_to_wav_from_mp3(path, "sfx_combo11")
        continue
    elif exists(join(new_folder, "sfx_combo11.wav")) == False:
        shutil.copy(join(src_folder, "sfx_combo11.wav"), new_folder)
        continue

    if path.name == "combo_12.ogg":
        export_to_wav_from_ogg(path, "sfx_combo12")
        continue
    elif path.name == "combo_12.mp3":
        export_to_wav_from_mp3(path, "sfx_combo12")
        continue
    elif exists(join(new_folder, "sfx_combo12.wav")) == False:
        shutil.copy(join(src_folder, "sfx_combo12.wav"), new_folder)
        continue

    if path.name == "combo_13.ogg":
        export_to_wav_from_ogg(path, "sfx_combo13")
        continue
    elif path.name == "combo_13.mp3":
        export_to_wav_from_mp3(path, "sfx_combo13")
        continue
    elif exists(join(new_folder, "sfx_combo13.wav")) == False:
        shutil.copy(join(src_folder, "sfx_combo13.wav"), new_folder)
        continue

    if path.name == "combo_14.ogg":
        export_to_wav_from_ogg(path, "sfx_combo14")
        continue
    elif path.name == "combo_14.mp3":
        export_to_wav_from_mp3(path, "sfx_combo14")
        continue
    elif exists(join(new_folder, "sfx_combo14.wav")) == False:
        shutil.copy(join(src_folder, "sfx_combo14.wav"), new_folder)
        continue

    if path.name == "combo_15.ogg":
        export_to_wav_from_ogg(path, "sfx_combo15")
        continue
    elif path.name == "combo_15.mp3":
        export_to_wav_from_mp3(path, "sfx_combo15")
        continue
    elif exists(join(new_folder, "sfx_combo15.wav")) == False:
        shutil.copy(join(src_folder, "sfx_combo15.wav"), new_folder)
        continue

    if path.name == "combo_16.ogg":
        export_to_wav_from_ogg(path, "sfx_combo16")
        continue
    elif path.name == "combo_16.mp3":
        export_to_wav_from_mp3(path, "sfx_combo16")
        continue
    elif exists(join(new_folder, "sfx_combo16.wav")) == False:
        shutil.copy(join(src_folder, "sfx_combo16.wav"), new_folder)
        continue


#The following sounds are not avaliable in most tetrio soundpacks
shutil.copy(join(src_folder, "sfx_combo17.wav"), new_folder)
shutil.copy(join(src_folder, "sfx_combo18.wav"), new_folder)
shutil.copy(join(src_folder, "sfx_combo19.wav"), new_folder)
shutil.copy(join(src_folder, "sfx_combo20.wav"), new_folder)
shutil.copy(join(src_folder, "sfx_lockdown.wav"), new_folder)
shutil.copy(join(src_folder, "sfx_movefail.wav"), new_folder)
shutil.copy(join(src_folder, "sfx_rotatefail.wav"), new_folder)