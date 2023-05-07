#imports
from os import makedirs, rename
from pydub import AudioSegment
from pathlib import Path
from shutil import copy, move
from os.path import exists, join, dirname

#file path for folder for Misamino
absolute_path = dirname(__file__)
src_folder = join(absolute_path, "sfx/default")
new_folder = join(absolute_path, "after/sfx/default")
if not exists(new_folder):
    makedirs(new_folder)

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
wavpaths = [path for path in Path(absolute_path).rglob("*.wav")]

allpaths = oggpaths + mp3paths + wavpaths

for path in allpaths:
    print(path.name)
    if path.name.startswith("sfx_"):
        continue
    if path.name == "clearbtb.ogg":
        export_to_wav_from_ogg(path, "sfx_b2b_tetris")
        export_to_wav_from_ogg(path, "sfx_b2b_tspin_mini")
        export_to_wav_from_ogg(path, "sfx_b2b_tspin_single")
        export_to_wav_from_ogg(path, "sfx_b2b_tspin_double")
        export_to_wav_from_ogg(path, "sfx_b2b_tspin_triple")
        continue
    elif path.name == "clearbtb.mp3":
        export_to_wav_from_mp3(path, "sfx_b2b_tetris")
        export_to_wav_from_mp3(path, "sfx_b2b_tspin_mini")
        export_to_wav_from_mp3(path, "sfx_b2b_tspin_single")
        export_to_wav_from_mp3(path, "sfx_b2b_tspin_double")
        export_to_wav_from_mp3(path, "sfx_b2b_tspin_triple")
        continue
    elif path.name == "clearbtb.wav":
        copy(path, join(new_folder, "sfx_b2b_tetris.wav"))
        copy(path, join(new_folder, "sfx_b2b_tspin_mini.wav"))
        copy(path, join(new_folder, "sfx_b2b_tspin_single.wav"))
        copy(path, join(new_folder, "sfx_b2b_tspin_double.wav"))
        copy(path, join(new_folder, "sfx_b2b_tspin_triple.wav"))
        continue
    #elif statements to replace the file should it not exist
    elif exists(join(new_folder, "sfx_b2b_tetris.wav")) == False:
        copy(join(src_folder, "sfx_b2b_tetris.wav"), new_folder)
    elif exists(join(new_folder, "sfx_b2b_tspin_mini.wav")) == False:
        copy(join(src_folder, "sfx_b2b_tspin_mini.wav"), new_folder)
    elif exists(join(new_folder, "sfx_b2b_tspin_single.wav")) == False:
        copy(join(src_folder, "sfx_b2b_tspin_single.wav"), new_folder)
    elif exists(join(new_folder, "sfx_b2b_tspin_double.wav")) == False:
        copy(join(src_folder, "sfx_b2b_tspin_double.wav"), new_folder)
    elif exists(join(new_folder, "sfx_b2b_tspin_triple.wav")) == False:
        copy(join(src_folder, "sfx_b2b_tspin_triple.wav"), new_folder)
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
    elif path.name == "clearline.wav":
        copy(path, join(new_folder, "sfx_single.wav"))
        copy(path, join(new_folder, "sfx_double.wav"))
        copy(path, join(new_folder, "sfx_triple.wav"))
        copy(path, join(new_folder, "sfx_lineattack.wav"))
        continue
    elif exists(join(new_folder, "sfx_single.wav")) == False:
        copy(join(src_folder, "sfx_single.wav"), new_folder)
    elif exists(join(new_folder, "sfx_double.wav")) == False:
        copy(join(src_folder, "sfx_double.wav"), new_folder)
    elif exists(join(new_folder, "sfx_triple.wav")) == False:
        copy(join(src_folder, "sfx_triple.wav"), new_folder)
    elif exists(join(new_folder, "sfx_lineattack.wav")) == False:
        copy(join(src_folder, "sfx_lineattack.wav"), new_folder)
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
    elif path.name == "clearspin.wav":
        copy(path, join(new_folder, "sfx_tspin_zero.wav"))
        copy(path, join(new_folder, "sfx_tspin_mini.wav"))
        copy(path, join(new_folder, "sfx_tspin_single.wav"))
        copy(path, join(new_folder, "sfx_tspin_double.wav"))
        copy(path, join(new_folder, "sfx_tspin_triple.wav"))
        continue
    elif exists(join(new_folder, "sfx_tspin_zero.wav")) == False:
        copy(join(src_folder, "sfx_tspin_zero.wav"), new_folder)
    elif exists(join(new_folder, "sfx_tspin_zero.wav")) == False:
        copy(join(src_folder, "sfx_tspin_mini.wav"), new_folder)
    elif exists(join(new_folder, "sfx_tspin_zero.wav")) == False:
        copy(join(src_folder, "sfx_tspin_single.wav"), new_folder)
    elif exists(join(new_folder, "sfx_tspin_zero.wav")) == False:
        copy(join(src_folder, "sfx_tspin_double.wav"), new_folder)
    elif exists(join(new_folder, "sfx_tspin_zero.wav")) == False:
        copy(join(src_folder, "sfx_tspin_triple.wav"), new_folder)
        continue 

    if path.name == "losestock.ogg":
        export_to_wav_from_ogg(path, "sfx_gameover")
        export_to_wav_from_ogg(path, "sfx_ko")
        continue
    elif path.name == "losestock.mp3":
        export_to_wav_from_mp3(path, "sfx_gameover")
        export_to_wav_from_mp3(path, "sfx_ko")
        continue
    elif path.name == "losestock.wav":
        copy(path, join(new_folder, "sfx_gameover.wav"))
        copy(path, join(new_folder, "sfx_ko.wav"))
        continue
    elif exists(join(new_folder, "sfx_gameover.wav")) == False:
        copy(join(src_folder, "sfx_gameover.wav"), new_folder)
    elif exists(join(new_folder, "sfx_ko.wav")) == False:
        copy(join(src_folder, "sfx_ko.wav"), new_folder)
        continue

    if path.name == "harddrop.ogg":
        export_to_wav_from_ogg(path, "sfx_harddrop")
        continue
    elif path.name == "harddrop.mp3":
        export_to_wav_from_mp3(path, "sfx_harddrop")
        continue
    if path.name == "harddrop.wav":
        copy(path, join(new_folder, "sfx_harddrop.wav"))
        continue
    elif exists(join(new_folder, "sfx_harddrop.wav")) == False:
        copy(join(src_folder, "sfx_harddrop.wav"), new_folder)
        continue

    if path.name == "hold.ogg":
        export_to_wav_from_ogg(path, "sfx_hold")
        continue
    elif path.name == "hold.mp3":
        export_to_wav_from_mp3(path, "sfx_hold")
        continue
    elif path.name == "hold.wav":
        copy(path, join(new_folder, "sfx_hold.wav"))
        continue
    elif exists(join(new_folder, "sfx_hold.wav")) == False:
         copy(join(src_folder, "sfx_hold.wav"), new_folder)
         continue

    if path.name == "move.ogg":
        export_to_wav_from_ogg(path, "sfx_move")
        continue
    elif path.name == "move.mp3":
        export_to_wav_from_mp3(path, "sfx_move")
        continue
    elif path.name == "move.wav":
        copy(path, join(new_folder, "sfx_move.wav"))
        continue
    elif exists(join(new_folder, "sfx_move.wav")) == False:
        copy(join(src_folder, "sfx_move.wav"), new_folder)
        continue

    if path.name == "rotate.ogg":
        export_to_wav_from_ogg(path, "sfx_rotate")
        continue
    elif path.name == "rotate.mp3":
        export_to_wav_from_mp3(path, "sfx_rotate")
        continue
    elif path.name == "rotate.wav":
        copy(path, join(new_folder, "sfx_rotate.wav"))
        continue
    elif exists(join(new_folder, "sfx_rotate.wav")) == False:
        copy(join(src_folder, "sfx_rotate.wav"), new_folder)
        continue

    if path.name == "softdrop.ogg":
        export_to_wav_from_ogg(path, "sfx_softdrop")
        continue
    elif path.name == "softdrop.mp3":
        export_to_wav_from_mp3(path, "sfx_softdrop")
        continue
    elif path.name == "softdrop.wav":
        copy(path, join(new_folder, "sfx_softdrop.wav"))
        continue
    elif exists(join(new_folder, "sfx_softdrop.wav")) == False:
        copy(join(src_folder, "sfx_softdrop.wav"), new_folder)
        continue

    if path.name == "clearquad.ogg":
        export_to_wav_from_ogg(path, "sfx_tetris")
        continue
    elif path.name == "clearquad.mp3":
        export_to_wav_from_mp3(path, "sfx_tetris")
        continue
    elif path.name == "clearquad.wav":
        copy(path, join(new_folder, "sfx_tetris.wav"))
        continue
    elif exists(join(new_folder, "sfx_tetris.wav")) == False:
        copy(join(src_folder, "sfx_tetris.wav"), new_folder)
        continue

    if path.name == "allclear.ogg":
        export_to_wav_from_ogg(path, "sfx_perfectclear")
        continue
    elif path.name == "allclear.mp3":
        export_to_wav_from_mp3(path, "sfx_perfectclear")
        continue
    elif path.name == "allclear.wav":
        copy(path, join(new_folder, "sfx_perfectclear.wav"))
        continue
    elif exists(join(new_folder, "sfx_perfectclear.wav")) == False:
        copy(join(src_folder, "sfx_perfectclear.wav"), new_folder)
        continue
    
    for i in range(1,17):
        if path.name == f"combo_{i}.ogg":
            export_to_wav_from_ogg(path, f"sfx_combo{i}")
            continue
        elif path.name == f"combo_{i}.mp3":
            export_to_wav_from_mp3(path, f"sfx_combo{i}")
            continue
        elif path.name == f"combo_{i}.wav":
            copy(path, join(new_folder, f"sfx_combo{i}.wav"))
            continue
        elif exists(join(new_folder, f"sfx_combo{i}.wav")) == False:
            copy(join(src_folder, f"sfx_combo{i}.wav"), new_folder)
            continue


#The following sounds are not avaliable in most tetrio soundpacks
copy(join(src_folder, "sfx_combo17.wav"), new_folder)
copy(join(src_folder, "sfx_combo18.wav"), new_folder)
copy(join(src_folder, "sfx_combo19.wav"), new_folder)
copy(join(src_folder, "sfx_combo20.wav"), new_folder)
copy(join(src_folder, "sfx_lockdown.wav"), new_folder)
copy(join(src_folder, "sfx_movefail.wav"), new_folder)
copy(join(src_folder, "sfx_rotatefail.wav"), new_folder)