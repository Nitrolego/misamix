#imports
import os
from pydub import AudioSegment
from pathlib import Path
import shutil

#file path for folder for Misamino
absolute_path = os.path.dirname(__file__)

src_folder = os.path.join(absolute_path, "sfx/default")

new_folder = os.path.join(absolute_path, "after/sfx/default")
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

#function to simplify exporting to WAV files
def export_to_wav_from_ogg(path, misaname):
    song = AudioSegment.from_ogg(path)
    song.export(os.path.join(new_folder, f"{misaname}.wav"), 
                    format="wav")
    #f string for easy identification of Misamino sfx names

def export_to_wav_from_mp3(path, misaname):
    song = AudioSegment.from_mp3(path)
    song.export(os.path.join(new_folder, f"{misaname}.wav"), 
                    format="wav")
    #f string for easy identification of Misamino sfx names



#Looping through all ogg files in repository to convert to WAV
for path in Path(absolute_path).rglob('*.ogg'):
    if path.name == "clearbtb.ogg":
        export_to_wav_from_ogg(path, "sfx_b2b_tetris")
        export_to_wav_from_ogg(path, "sfx_b2b_tspin_mini")
        export_to_wav_from_ogg(path, "sfx_b2b_tspin_single")
        export_to_wav_from_ogg(path, "sfx_b2b_tspin_double")
        export_to_wav_from_ogg(path, "sfx_b2b_tspin_triple")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_b2b_tetris.wav"), new_folder)
    #     shutil.copy(os.path.join(src_folder, "sfx_b2b_tspin_mini.wav"), new_folder)
    #     shutil.copy(os.path.join(src_folder, "sfx_b2b_tspin_single.wav"), new_folder)
    #     shutil.copy(os.path.join(src_folder, "sfx_b2b_tspin_double.wav"), new_folder)
    #     shutil.copy(os.path.join(src_folder, "sfx_b2b_tspin_triple.wav"), new_folder)

    if path.name == "clearline.ogg":
        export_to_wav_from_ogg(path, "sfx_single")
        export_to_wav_from_ogg(path, "sfx_double")
        export_to_wav_from_ogg(path, "sfx_triple")
        export_to_wav_from_ogg(path, "sfx_lineattack")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_single.wav"), new_folder)
    #     shutil.copy(os.path.join(src_folder, "sfx_double.wav"), new_folder)
    #     shutil.copy(os.path.join(src_folder, "sfx_triple.wav"), new_folder)
    #     shutil.copy(os.path.join(src_folder, "sfx_lineattack.wav"), new_folder)

    if path.name == "clearspin.ogg":
        export_to_wav_from_ogg(path, "sfx_tspin_zero")
        export_to_wav_from_ogg(path, "sfx_tspin_mini")
        export_to_wav_from_ogg(path, "sfx_tspin_single")
        export_to_wav_from_ogg(path, "sfx_tspin_double")
        export_to_wav_from_ogg(path, "sfx_tspin_triple")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_tspin_zero.wav"), new_folder)
    #     shutil.copy(os.path.join(src_folder, "sfx_tspin_mini.wav"), new_folder)
    #     shutil.copy(os.path.join(src_folder, "sfx_tspin_single.wav"), new_folder)
    #     shutil.copy(os.path.join(src_folder, "sfx_tspin_double.wav"), new_folder)
    #     shutil.copy(os.path.join(src_folder, "sfx_tspin_triple.wav"), new_folder)
        

    if path.name == "losestock.ogg":
        export_to_wav_from_ogg(path, "sfx_gameover")
        export_to_wav_from_ogg(path, "sfx_ko")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_gameover.wav"), new_folder)
    #     shutil.copy(os.path.join(src_folder, "sfx_ko.wav"), new_folder)

    if path.name == "harddrop.ogg":
        export_to_wav_from_ogg(path, "sfx_harddrop")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_harddrop.wav"), new_folder)

    if path.name == "hold.ogg":
        export_to_wav_from_ogg(path, "sfx_hold")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_hold.wav"), new_folder)

    if path.name == "move.ogg":
        export_to_wav_from_ogg(path, "sfx_move")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_move.wav"), new_folder)

    if path.name == "rotate.ogg":
        export_to_wav_from_ogg(path, "sfx_rotate")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_rotate.wav"), new_folder)

    if path.name == "softdrop.ogg":
        export_to_wav_from_ogg(path, "sfx_softdrop")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_softdrop.wav"), new_folder)

    if path.name == "clearquad.ogg":
        export_to_wav_from_ogg(path, "sfx_tetris")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_tetris.wav"), new_folder)

    if path.name == "allclear.ogg":
        export_to_wav_from_ogg(path, "sfx_perfectclear")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_perfectclear.wav"), new_folder)
        
    if path.name == "combo_1.ogg":
        export_to_wav_from_ogg(path, "sfx_combo1")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo1.wav"), new_folder)
    
    if path.name == "combo_2.ogg":
        export_to_wav_from_ogg(path, "sfx_combo2")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo2.wav"), new_folder)

    if path.name == "combo_3.ogg":
        export_to_wav_from_ogg(path, "sfx_combo3")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo3.wav"), new_folder)

    if path.name == "combo_4.ogg":
        export_to_wav_from_ogg(path, "sfx_combo4")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo4.wav"), new_folder)
    
    if path.name == "combo_5.ogg":
        export_to_wav_from_ogg(path, "sfx_combo5")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo5.wav"), new_folder)
    
    if path.name == "combo_6.ogg":
        export_to_wav_from_ogg(path, "sfx_combo6")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo6.wav"), new_folder)

    if path.name == "combo_7.ogg":
        export_to_wav_from_ogg(path, "sfx_combo7")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo7.wav"), new_folder)

    if path.name == "combo_8.ogg":
        export_to_wav_from_ogg(path, "sfx_combo8")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo8.wav"), new_folder)

    if path.name == "combo_9.ogg":
        export_to_wav_from_ogg(path, "sfx_combo9")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo9.wav"), new_folder)
    
    if path.name == "combo_10.ogg":
        export_to_wav_from_ogg(path, "sfx_combo10")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo10.wav"), new_folder)

    if path.name == "combo_11.ogg":
        export_to_wav_from_ogg(path, "sfx_combo11")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo11.wav"), new_folder)

    if path.name == "combo_12.ogg":
        export_to_wav_from_ogg(path, "sfx_combo12")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo12.wav"), new_folder)

    if path.name == "combo_13.ogg":
        export_to_wav_from_ogg(path, "sfx_combo13")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo13.wav"), new_folder)
    
    if path.name == "combo_14.ogg":
        export_to_wav_from_ogg(path, "sfx_combo14")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo14.wav"), new_folder)

    if path.name == "combo_15.ogg":
        export_to_wav_from_ogg(path, "sfx_combo15")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo15.wav"), new_folder)

    if path.name == "combo_16.ogg":
        export_to_wav_from_ogg(path, "sfx_combo16")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo16.wav"), new_folder)

    print(path.name)

#Looping through all mp3 files in repository to convert to WAV
for path in Path(absolute_path).rglob('*.mp3'):
    if path.name == "clearbtb.mp3":
        export_to_wav_from_mp3(path, "sfx_b2b_tetris")
        export_to_wav_from_mp3(path, "sfx_b2b_tspin_mini")
        export_to_wav_from_mp3(path, "sfx_b2b_tspin_single")
        export_to_wav_from_mp3(path, "sfx_b2b_tspin_double")
        export_to_wav_from_mp3(path, "sfx_b2b_tspin_triple")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_b2b_tetris.wav"), new_folder)
    #     shutil.copy(os.path.join(src_folder, "sfx_b2b_tspin_mini.wav"), new_folder)
    #     shutil.copy(os.path.join(src_folder, "sfx_b2b_tspin_single.wav"), new_folder)
    #     shutil.copy(os.path.join(src_folder, "sfx_b2b_tspin_double.wav"), new_folder)
    #     shutil.copy(os.path.join(src_folder, "sfx_b2b_tspin_triple.wav"), new_folder)

    if path.name == "clearline.mp3":
        export_to_wav_from_mp3(path, "sfx_single")
        export_to_wav_from_mp3(path, "sfx_double")
        export_to_wav_from_mp3(path, "sfx_triple")
        export_to_wav_from_mp3(path, "sfx_lineattack")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_single.wav"), new_folder)
    #     shutil.copy(os.path.join(src_folder, "sfx_double.wav"), new_folder)
    #     shutil.copy(os.path.join(src_folder, "sfx_triple.wav"), new_folder)
    #     shutil.copy(os.path.join(src_folder, "sfx_lineattack.wav"), new_folder)

    if path.name == "clearspin.mp3":
        export_to_wav_from_mp3(path, "sfx_tspin_zero")
        export_to_wav_from_mp3(path, "sfx_tspin_mini")
        export_to_wav_from_mp3(path, "sfx_tspin_single")
        export_to_wav_from_mp3(path, "sfx_tspin_double")
        export_to_wav_from_mp3(path, "sfx_tspin_triple")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_tspin_zero.wav"), new_folder)
    #     shutil.copy(os.path.join(src_folder, "sfx_tspin_mini.wav"), new_folder)
    #     shutil.copy(os.path.join(src_folder, "sfx_tspin_single.wav"), new_folder)
    #     shutil.copy(os.path.join(src_folder, "sfx_tspin_double.wav"), new_folder)
    #     shutil.copy(os.path.join(src_folder, "sfx_tspin_triple.wav"), new_folder)
        

    if path.name == "losestock.mp3":
        export_to_wav_from_mp3(path, "sfx_gameover")
        export_to_wav_from_mp3(path, "sfx_ko")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_gameover.wav"), new_folder)
    #     shutil.copy(os.path.join(src_folder, "sfx_ko.wav"), new_folder)

    if path.name == "harddrop.mp3":
        export_to_wav_from_mp3(path, "sfx_harddrop")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_harddrop.wav"), new_folder)

    if path.name == "hold.mp3":
        export_to_wav_from_mp3(path, "sfx_hold")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_hold.wav"), new_folder)

    if path.name == "move.mp3":
        export_to_wav_from_mp3(path, "sfx_move")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_move.wav"), new_folder)

    if path.name == "rotate.mp3":
        export_to_wav_from_mp3(path, "sfx_rotate")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_rotate.wav"), new_folder)

    if path.name == "softdrop.mp3":
        export_to_wav_from_mp3(path, "sfx_softdrop")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_softdrop.wav"), new_folder)

    if path.name == "clearquad.mp3":
        export_to_wav_from_mp3(path, "sfx_tetris")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_tetris.wav"), new_folder)

    if path.name == "allclear.mp3":
        export_to_wav_from_mp3(path, "sfx_perfectclear")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_perfectclear.wav"), new_folder)
        
    if path.name == "combo_1.mp3":
        export_to_wav_from_mp3(path, "sfx_combo1")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo1.wav"), new_folder)
    
    if path.name == "combo_2.mp3":
        export_to_wav_from_mp3(path, "sfx_combo2")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo2.wav"), new_folder)

    if path.name == "combo_3.mp3":
        export_to_wav_from_mp3(path, "sfx_combo3")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo3.wav"), new_folder)

    if path.name == "combo_4.mp3":
        export_to_wav_from_mp3(path, "sfx_combo4")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo4.wav"), new_folder)
    
    if path.name == "combo_5.mp3":
        export_to_wav_from_mp3(path, "sfx_combo5")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo5.wav"), new_folder)
    
    if path.name == "combo_6.mp3":
        export_to_wav_from_mp3(path, "sfx_combo6")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo6.wav"), new_folder)

    if path.name == "combo_7.mp3":
        export_to_wav_from_mp3(path, "sfx_combo7")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo7.wav"), new_folder)

    if path.name == "combo_8.mp3":
        export_to_wav_from_mp3(path, "sfx_combo8")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo8.wav"), new_folder)

    if path.name == "combo_9.mp3":
        export_to_wav_from_mp3(path, "sfx_combo9")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo9.wav"), new_folder)
    
    if path.name == "combo_10.mp3":
        export_to_wav_from_mp3(path, "sfx_combo10")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo10.wav"), new_folder)

    if path.name == "combo_11.mp3":
        export_to_wav_from_mp3(path, "sfx_combo11")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo11.wav"), new_folder)

    if path.name == "combo_12.mp3":
        export_to_wav_from_mp3(path, "sfx_combo12")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo12.wav"), new_folder)

    if path.name == "combo_13.mp3":
        export_to_wav_from_mp3(path, "sfx_combo13")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo13.wav"), new_folder)
    
    if path.name == "combo_14.mp3":
        export_to_wav_from_mp3(path, "sfx_combo14")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo14.wav"), new_folder)

    if path.name == "combo_15.mp3":
        export_to_wav_from_mp3(path, "sfx_combo15")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo15.wav"), new_folder)

    if path.name == "combo_16.mp3":
        export_to_wav_from_mp3(path, "sfx_combo16")
    # else:
    #     shutil.copy(os.path.join(src_folder, "sfx_combo16.wav"), new_folder)

    print(path.name)

#The following sounds are not avaliable in most tetrio soundpacks
shutil.copy(os.path.join(src_folder, "sfx_combo17.wav"), new_folder)
shutil.copy(os.path.join(src_folder, "sfx_combo18.wav"), new_folder)
shutil.copy(os.path.join(src_folder, "sfx_combo19.wav"), new_folder)
shutil.copy(os.path.join(src_folder, "sfx_combo20.wav"), new_folder)
shutil.copy(os.path.join(src_folder, "sfx_lockdown.wav"), new_folder)
shutil.copy(os.path.join(src_folder, "sfx_movefail.wav"), new_folder)
shutil.copy(os.path.join(src_folder, "sfx_rotatefail.wav"), new_folder)