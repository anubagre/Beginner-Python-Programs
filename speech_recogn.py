# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 21:20:46 2023

@author: HP
"""

import speech_recognition as sr
ad=("E:\Chalti h purvahi.wav")
r=sr.Recognizer()

with sr.AudioFile(ad) as source:
    audio=r.record(source)

try:
    print("Audio file contains:",r.recognize_google(audio))
except sr.UnknownValueError:
    print("Couldn't recognize Audio")
except sr.RequestError:
    print("Couldn't get results from Google")
    