#imports
import os
from pydub import AudioSegment
from pathlib import Path

#file path for folder for Misamino
absolute_path = os.path.dirname(__file__)
new_folder = os.path.join(absolute_path, "after/sfx/default")
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

#function to simplify exporting to WAV files
def export_to_wav(path, misaname):
    song = AudioSegment.from_ogg(path)
    song.export(os.path.join(new_folder, f"{misaname}.wav"), 
                    format="wav")
    #f string for easy identification of Misamino sfx names

#Looping through all ogg files in repository to convert to WAV
for path in Path(absolute_path).rglob('*.ogg'):
    if path.name == "clearbtb.ogg":
        export_to_wav(path, "sfx_b2b_tetris")
        export_to_wav(path, "sfx_b2b_tspin_double")
        export_to_wav(path, "sfx_b2b_tspin_mini")
        export_to_wav(path, "sfx_b2b_tspin_single")
        export_to_wav(path, "sfx_b2b_tspin_triple")
    
    if path.name == "clearline.ogg":
        export_to_wav(path, "sfx_single")
        export_to_wav(path, "sfx_double")
        export_to_wav(path, "sfx_triple")
        export_to_wav(path, "sfx_lineattack")

    if path.name == "clearspin.ogg":
        export_to_wav(path, "sfx_tspin_double")
        export_to_wav(path, "sfx_tspin_mini")
        export_to_wav(path, "sfx_tspin_single")
        export_to_wav(path, "sfx_tspin_triple")

    if path.name == "losestock.ogg":
        export_to_wav(path, "sfx_gameover")
        export_to_wav(path, "sfx_ko")

    if path.name == "harddrop.ogg":
        export_to_wav(path, "sfx_harddrop")
    
    if path.name == "hold.ogg":
        export_to_wav(path, "sfx_hold")

    if path.name == "move.ogg":
        export_to_wav(path, "sfx_move")

    if path.name == "rotate.ogg":
        export_to_wav(path, "sfx_rotate")

    if path.name == "softdrop.ogg":
        export_to_wav(path, "sfx_softdrop")

    if path.name == "clearquad.ogg":
        export_to_wav(path, "sfx_tetris")

    if path.name == "allclear.ogg":
        export_to_wav(path, "sfx_perfectclear")
        
    if path.name == "combo_1.ogg":
        export_to_wav(path, "sfx_combo1")
    
    if path.name == "combo_2.ogg":
        export_to_wav(path, "sfx_combo2")

    if path.name == "combo_3.ogg":
        export_to_wav(path, "sfx_combo3")

    if path.name == "combo_4.ogg":
        export_to_wav(path, "sfx_combo4")
    
    if path.name == "combo_5.ogg":
        export_to_wav(path, "sfx_combo5")
    
    if path.name == "combo_6.ogg":
        export_to_wav(path, "sfx_combo6")

    if path.name == "combo_7.ogg":
        export_to_wav(path, "sfx_combo7")

    if path.name == "combo_8.ogg":
        export_to_wav(path, "sfx_combo8")

    if path.name == "combo_9.ogg":
        export_to_wav(path, "sfx_combo9")
    
    if path.name == "combo_10.ogg":
        export_to_wav(path, "sfx_combo10")

    if path.name == "combo_11.ogg":
        export_to_wav(path, "sfx_combo11")

    if path.name == "combo_12.ogg":
        export_to_wav(path, "sfx_combo12")
    
    if path.name == "combo_13.ogg":
        export_to_wav(path, "sfx_combo13")
    
    if path.name == "combo_14.ogg":
        export_to_wav(path, "sfx_combo14")

    if path.name == "combo_15.ogg":
        export_to_wav(path, "sfx_combo15")

    if path.name == "combo_16.ogg":
        export_to_wav(path, "sfx_combo16")

    print(path.name)