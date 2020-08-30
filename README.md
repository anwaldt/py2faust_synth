This is an example project for controlling
a synth, programmed and compiled with Faust,
through a Python script.
The synth runs as a JACK client on
Linux systems and the output
is automatically recorded by jack_capture.

The following examples are written for
Debian systems.

# Faust Synth

This is a quick example for a subtractive
synth, modified from the Faust documentation.

## Get the Faust Compiler

The recent Faust compiler
can be cloned from the repository:

https://github.com/grame-cncm/faust


## Compile the Faust Code

With GUI (for testing):

 faust2jaqt -osc subtractive_synth.dsp 

Without GUI:

 faust2jackconsole -osc subtractive_synth.dsp


This will create a binary:

 subtractive_synth

## OSC control

The synth listens to OSC commands on the
defauilt Faust-UDP ports 5510, 5511 and 5512.

## Run the Synth

- after starting the JACK server:

 ./subtractive_synth



# Python Control

## Install pythonosc

 $ pip3 install pythonosc

## Run Script

- after making sure that 'synth_control.py' is executable, run:

 $ ./synth_control.py

