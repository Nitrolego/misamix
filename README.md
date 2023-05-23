# MisaMix

MisaMix allows users to create [MisaMino](https://harddrop.com/forums/index.php?showtopic=5292) compatible soundpacks from [YHF@TETR.IO+](https://you.have.fail/at/tetrioplus/) with a GUI!

## Dependencies

To use the console based script:
pydub ffmpeg

To use the GUI version:
ffmpeg

To develop the GUI version:
pydub babel ffmpeg

## Usage
Prerequisites:
1. install dependencies as listed above.

To use the script
1. Load the zip folder of the TETR.IO compatible soundpack into ./before
2. Run the script
3. The converted audio files should be found in ./after/sfx/default

To use the GUI
1. Run the exe.
2. Select the location of the zip folder of the TETR.IO compatible soundpack with the "Browse" button on the first row. (Default=./before)
3. Select the output location of the audio files with the "Browse" button on the second row. (Default=./after/sfx/default)
4. Click Run.
5. The specified output folder should contain the converted audio files.

After conversion
1. copy the sfx folder into MisaMino's sound/sfx folder
2. enjoy new sound effects!


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)