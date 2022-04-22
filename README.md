# EE104Lab7_Low_Crystal
This is Lab 7 for EE104 at SJSU 
Download and Extract File: Lab7_Low_Crystal 

There are three part to this lab.

I. FFT/IFFT Audio Signal Processing
For this code, it will take three different frequencies and combined them together to make a sound. The code will plot a few different graphs accordingly. The graphs included are the individual plots for the three frequencies, the three signals combined, the FFT plot without the filtering, the comparison in time domain for the original signal and the filtered signal and the FFT plot with filtering. Then the program will create .wav files for the demonstration of noise cancelation using the three frequencies that were shown combined. 

Import Packages: 
  
  import numpy as np
  
  from scipy import fftpack, signal
  
  from matplotlib import pyplot as plt
  
  import pandas as pd
  
  from scipy.io import wavfile
  
  import pandas as pd
  
  import sys, os, os.path

Instructions: 
  
  Open code: Low_AudioSigProcess in the file Audio_Sig_Processing
  
  1) Run the code and the user will see the following results
  
  2) Results will show:
      
      a) Signal at 215 Hz
      
      b) Signal at 713 Hz
      
      c) Signal at 805 Hz
      
      d) All three signals combined
      
      e) FFT without Filtering of the three signals 
      
      f) FFT with Filtering for the three signals
      
      g) Time domain comparison between the original and filtered signal
