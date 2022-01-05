# README #

DAVID
version 2.0
March 2018

D.A.V.I.D. (Da amazing voice inflection device) is a real-time voice transformation tool able to “colour” any voice recording with an emotion that wasn’t intended by its speaker. D.A.V.I.D. was especially designed with affective psychology and neuroscientist in mind, and aims to provide researchers with new ways to produce and control affective stimuli, both for offline listening and for real-time paradigms. A scientific description can be found here: http://biorxiv.org/content/early/2016/01/28/038133

### LICENSE ###

The MIT License (MIT)

Copyright (c) 2015 CNRS UMR 9912 STMS / IRCAM

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

### HOWTO ###

To open the patch, double click on the DAVID.maxproj file

# AUDIO SETUP

The upper left box in DAVID allows to specify the audio setup for Max: audio drivers, and I/O devices. Two buffers sizes can also be specified, according to Max options: [IOvs] for exchanging audio between Max and the audio card, [sigvs] within Max. When this is allowed by the specific setup, the suggested values for [IOvs] and [sigvs] are 128 and 64, respectively.
A roundtrip latency estimation depending on the selected sizes is given in the green number box [roundtrip latency].

# INPUT SOUND

DAVID can be either used with sound files or a folder of sound files (the [PLAY ITER] button after ), by choosing and playing them from the upper left part of the patch ; either with a microphone (first input channel of the audio card), by hitting on the [MICROPHONE OFF] button.

* using a sound file: 
- choose the sound file with the [Open soundfile] button
- hit the play button on the play bar or the space key on your keyboard; the arrow to the right of the play bar is to turn loop on or off

* using a folder of sound files: 
- choose the folder with the [Open folder] button
- hit the [PLAY ITER] button

# EFFECTS

4 effects modules are available in the central panel, with their own parameters to set: constant pitch shift, vibrato, inflexion, filter.

# CONSOLE AND AUTOMATION

The lower panel provides 4 effect sliders and a [MASTER] slider. Each effect slider is related to the corresponding processing module, and control its intensity: 100% gives the full intensity specified by the module’s parameters, while at 0% the module is excluded.

The [MASTER] slider allows to control all of the sliders activated by the current effect at once, preserving proportions; its range varies from 0% to 200%.

If the [AUTOMATION] check box is on, playing or recording a transformation makes the [MASTER] slider to automatically start a linear ramp from 0% to 100% in [RAMP TIME] seconds, after an initial time of [HOLD TIME] seconds where the effects are not applied

# PRESETS

9 default presets for the effects parameters are proposed: the neutral one, with no transformation; happy, afraid, sad are presets intended as limit cases, artefacts may occur; the presets whose names contain "brm" are the ones used for the validation experiments in the paper "DAVID: An Open-source platform for real-time emotional speech transformation" (Rachman, L., Liuni, M., Arias, P., Lind, A., Johansson, P., Hall, L., Richardson, D., Watanabe, K., Aucouturier, J.J. - Behavior Research Methods, 2017). 

* recall a preset: use the panel with small squares, each square is a preset; pass upon a lighted square with the mouse to know the preset’s name, click on a square to recall a preset

* define a preset: 
- define a sliders and effects configuration you want to store
- type the preset name in the text box
- the software automatically proposes a preset number that can be used (current limit is 44 presets) 
- hit the [SAVE AS PRESET <n>] button

* overwrite a preset (presets from 1 to 9 cannot be modified): 
- recall a preset
- define a new sliders and effects configuration you want to store
- optionally type a new preset name in the text box
- hit the [OVERWRITE PRESET <n>] button

* the [SHOW] button provides a list of the available presets and parameters that are controlled

* the [LOAD] button allows to load a .json file of presets (e.g. to replace the standard .json file distributed with DAVID with other presets saved from previous versions of the software)

# RECORDING

To record a transformation:

* using a sound file: 
- choose the sound file with the [Open soundfile] button
- hit the [RECORD] button: the output file is saved in the "patchers" folder of the DAVID project; recording automatically ends at the end of the file, if you don’t stop it before
- hit the [RECORD IN] button and choose a destination folder: recording automatically ends at the end of the file, if you don’t stop it before
- two files are produced: 
1) modified sound: filename is given by <original filename>_<preset name>.wav
2) non modified sound: filename is given by <original filename>_<preset name>_NM.wav

* using a sounds folder: 
- choose the sound folder with the [Open folder] button
- hit the [RECORD] button and choose a destination folder: recording automatically ends when all of the sound file in the folders have been processed
- the recorded files are stored in the chosen folder, filename is given by <original filename>_<effect name>.wav

* using a microphone
- switch on the [MIC OFF] button
- hit the [RECORD] button and choose a destination folder to start recording, hit again to end
- the recorded file is stored in the chosen folder, filename is given by <date>_<hour>.wav

Turning on the microphone excludes sound files to be recorded

### Who do I talk to? ###

* marco.liuni@ircam.fr
* cream.ircam.fr