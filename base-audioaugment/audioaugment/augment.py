import os
from pathlib import Path
import random
import sys
import wave
import ffmpegio

import scipy.io.wavfile as wav
from scipy.io import wavfile
import tempfile
import numpy as np

def read_audio_to_array(file_path):
    try:
        samplerate, data = wav.read(file_path)
    except ValueError:
        # If it's not a wav file, use ffmpegio to convert it to wav format
        temp_wav_file = tempfile.mktemp(suffix='.wav')
        ffmpegio.transcode(file_path, temp_wav_file)
        samplerate, data = wav.read(temp_wav_file)
        os.remove(temp_wav_file)  # Clean up temp file
    return samplerate, data
           
def augment_audio_ffmpegio(input_file, output_file):
    filters = ''
    pitch_shift_factor = 2**(random.uniform(-0.3, 0.3))
    pitch_shift = f"asetrate=44100*{pitch_shift_factor}"
    filters += pitch_shift
    filters += ','
    
    atempo = f"atempo={1/pitch_shift_factor}"
    filters += atempo
    filters += ','
    
    volume = f"volume={random.uniform(0.6, 1.2)}"
    filters += volume

    # Random highpass filter (apply with 50% chance)
    if random.random() > 0.5:
        highpass = f"highpass=f={random.uniform(100, 300)}"
        filters += ','
        filters += highpass
        
    
    ffmpegio.transcode(
        input_file,
        output_file,
        acodec='pcm_s16le',
        af=filters
    )
    
def main():
    filename = sys.argv[1]
    samplerate, data = read_audio_to_array(filename)
    temp_input_file = tempfile.mktemp(suffix='.wav')
    
    wav.write(temp_input_file, samplerate, data)

    augment_audio_ffmpegio(temp_input_file, f'{Path(filename).stem}_augmented.wav')
