# EE104Lab7_Low_Crystal
This is Lab 7 for EE104 at SJSU. 

Download provided in this github.

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
  
  3) The .wav files created will save in the file explorer where the code is saved 
  
  
II. Heart Rate Analysis

For this code, it will do the task of ploting the heart rate signal and find the time-domain measurements for the heartbeat sound collected. 

Import Packages: 

  import heartpy as hp
  
  import matplotlib.pyplot as plt

Instructions: 

  Open code: Low_heartrateanalysis in the file Heart_Rate_Analysis

  1) Retreive .wav from https://www.kaggle.com/kinguistics/heartbeat-sounds
  
  2) Convert .wav file to .csv file with the python program provided in the modules on canvas
      - Run the program and then enter in the .wav file name 
  
  3) Run the program and the results will show signal from the .csv file and the measurements for the heartbeat
 
III. Red Alert

The goal of this game is to click the red snowflake image at the best of your ability. 

Import Packages: 

  import pgzrun
  
  import pygame
  
  import pgzero
  
  import random
  
  from pgzero.builtins import Actor
  
  from random import randint

Instructions: 
  
  Open code: Low_redalert in the file Game

  1) Run the code 
  
  2) Click on the red snowflake to get to the next level 
  
  3) If player fails to complete the game press spacebar to retry or if the player wants to play again press spacebar to    play again.





