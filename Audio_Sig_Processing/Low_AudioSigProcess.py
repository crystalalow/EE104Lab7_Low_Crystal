# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 10:09:56 2022

@author: Crystal
"""

import numpy as np
from scipy import fftpack, signal
from matplotlib import pyplot as plt
import pandas as pd
from scipy.io import wavfile
import pandas as pd
import sys, os, os.path

#Set the constants for the signals to make easier to call 
timestep = 1/44100
noiseamplitude=0.25
noiseamplitudetwo=0.5

#signal 1 @ 215HZ
frequency_one=215 
period_one = 1/frequency_one
time_vec = np.arange(0, 1, timestep)
signal_one = 1000*(np.sin(2 * np.pi / period_one * time_vec))
plt.figure(figsize=(20,10))
plt.xticks(fontsize=23)
plt.yticks(fontsize=23)
plt.xlabel('Time (s)', fontsize=27)
plt.ylabel('Amplitude', fontsize=27)
plt.title('Signal at 215 Hz', fontsize=40)
plt.xlim(0,.01)
plt.plot(time_vec, signal_one)

#signal 2 @ 713Hz
frequency_two=713 
period_two = 1/frequency_two
time_vec = np.arange(0, 1, timestep)
signal_two = noiseamplitude*1000*(np.sin(2 * np.pi / period_two * time_vec))
plt.figure(figsize=(20,10))
plt.xticks(fontsize=23)
plt.yticks(fontsize=23)
plt.xlabel('Time (s)', fontsize=27)
plt.ylabel('Amplitude', fontsize=27)
plt.title('Signal at 713 Hz', fontsize=40)
plt.xlim(0,.01)
plt.plot(time_vec, signal_two)

#signal 3 @ 805
frequency_three=805 
period_three = 1/frequency_three
time_vec = np.arange(0, 1, timestep)
signal_three = noiseamplitudetwo*1000*(np.sin(2 * np.pi / period_three * time_vec))
plt.figure(figsize=(20,10))
plt.xticks(fontsize=23)
plt.yticks(fontsize=23)
plt.xlabel('Time (s)', fontsize=27)
plt.ylabel('Amplitude', fontsize=27)
plt.title('Signal at 805 Hz', fontsize=40)
plt.xlim(0,.01) 
plt.plot(time_vec, signal_three)

#Combine all signals together into one plot
signal_combine = signal_one + signal_two + signal_three
plt.figure(figsize=(60,30))
plt.xticks(fontsize=60)
plt.yticks(fontsize=60)
plt.xlabel('Time (s)', fontsize=70)
plt.ylabel('Amplitude', fontsize=70)
plt.title('Signals Combined with Freqs of 215 Hz, 713 Hz, 805 Hz', fontsize=100)
plt.xlim(0,1)
plt.plot(time_vec, signal_combine)


#create .wav file without noise cancelation
wavfile.write('unfiltered.wav', 44100, signal_combine.astype(np.int16))

#FFT plot and power for the combined signals
signal_fft = fftpack.fft(signal_combine)
power = np.abs(signal_fft)**2
sample_freq = fftpack.fftfreq(signal_combine.size, d=timestep)
plt.figure(figsize=(60, 30))
plt.xticks(fontsize=55)
plt.yticks(fontsize=55)
plt.xlabel('Frequency (Hz)', fontsize=60)
plt.ylabel('Power', fontsize=60)
plt.title('Combined Signals in Frequency Domain Unfiltered', fontsize=100)
plt.xlim(-1000,1000)
plt.plot(sample_freq, power)


#Finding the peak frequency 
pos_mask = np.where(sample_freq > 0)
freqs = sample_freq[pos_mask]
peak_freq = freqs[power[pos_mask].argmax()]

#Filtering high frequencies 
high_freq_fft = signal_fft.copy()
high_freq_fft[np.abs(sample_freq) > peak_freq] = 0
filtered_sig = fftpack.ifft(high_freq_fft)

#create .wav file with noise cancelation 
wavfile.write('filtered.wav', 44100, filtered_sig.astype(np.int16))


#Confirmation for filter signal FFT 
signal_fft1 = fftpack.fft(filtered_sig)
power = np.abs(signal_fft1)**2
sample_freq = fftpack.fftfreq(filtered_sig.size, d=timestep)

# Filtered FFT (noise cancelation)
plt.figure(figsize=(60, 30))
plt.xticks(fontsize=60)
plt.yticks(fontsize=60)
plt.xlabel('Frequency (Hz)', fontsize=60)
plt.ylabel('Power', fontsize=60)
plt.title('Filtered Signal in Frequency Domain', fontsize=100)
plt.xlim(-1500,1500)
plt.plot(sample_freq, power)

#Graph to show the orignal and filtered time domain signal graph comparison
plt.figure(figsize=(60,30))
plt.plot(time_vec, signal_combine, label='Original signal')
plt.plot(time_vec, filtered_sig, linewidth=5, label='Filtered signal')
plt.xticks(fontsize=60)
plt.yticks(fontsize=60)
plt.xlabel('Time (s)', fontsize=60)
plt.ylabel('Amplitude', fontsize=60)
plt.title('Time Domain Comparison for the Original and Filtered Signal', fontsize=100)
plt.legend(loc='best',fontsize=70)
plt.xlim(0,.01)


