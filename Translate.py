#!/usr/bin/python3


import sys
import os
from termcolor import colored
from Voices.Speak import *
from Library.Savefile import *
import requests
from gtts import gTTS
import os
###
Mode=1
INPUT=None
data =None
Voice=None
Mode =1
###
def SpeakAV(INPUT):
    global Voice    
    tts = gTTS(text=INPUT, lang='en')
    name= 'Voices/'+INPUT+'.mp3'
    tts.save(name)
    Voice=name 
    #return Voice
def Bye():
    print(colored("You wanna leave I'm gonna miss you so much",'red'))
    Speak("SoundProcess/You wanna leave------ I'm gonna miss you so much.mp3")
    print(colored("Take care of yourself", "yellow"))
    Speak("SoundProcess/good bye.mp3")
    print(colored("Good Bye!",'red'))
    
def Translate(Text,Language):
    global data    
    file=open('ConfigFiles/API_KEY.txt', "r")
    API_KEY=file.read()    
    url='https://translate.yandex.net/api/v1.5/tr.json/translate'
    params=dict(key=API_KEY, text =Text, lang=Language)
    res=requests.get(url,params=params)
    json=res.json()
    data=json['text'][0]
    #return data        
def Trans():
    global INPUT, Mode
    print(Mode)    
    INPUT=input("Enter words you wanna translate: \r\n------------->")
    if INPUT=='--mode':
        print('changing mode')
        if Mode==1:
            print(colored("Hi There!",'yellow'))
            Speak("SoundProcess/You've just changed mode from ENGLISH VIETNAMESE to VIETNAMESE ENGLISH.mp3")
            print("You've just changed mode from ENGLISH-VIETNAMESE to VIETNAMESE-ENGLISH")
            Mode=0
            print(colored("Process Successed!",'red'))
            Trans()
        else :
            print(colored("Hi There!",'yellow'))
            Speak("SoundProcess/You've just changed mode from VIETNAMESE- ENGLISH to ENGLISH- VIETNAMESE .mp3")
            print("You've just changed mode from VIETNAMESE-ENGLISH to ENGLISH-VIETNAMESE")
            Mode=0
            print(colored("Process Successed!",'red'))            
            Mode=1
            Trans()
def Run():
    Trans()
    if Mode==1:
        Translate(INPUT,'en-vi')
        print(data)
        Savefile(INPUT,data)
        SpeakAV(INPUT)
        Speak(Voice)
        choice=input("Enter to continue or n + Enter to stop:\r\n==Enter====>")
        if choice =='n' :
            Bye()
        else :
            Run()        
    if Mode ==0:
        Translate(INPUT,'vi-en')
        print(data)
        Savefile(data,INPUT)
        SpeakAV(data)
        Speak(Voice)
        if choice ==n :
            Bye()
        else :
            Run()        
    
        
        
    



#####

if Mode==1:
    
    print('----------------ENGLISH------TO-------VIETNAMESE-----------------------------')
    print('Type --mode to change mode')
    print(colored("Hope You Have A Good Day!",'yellow'))
    #Speak('Voices/hi.mp3')
if Mode==0:
    
    print('-------------VIETNAMESE---------TO-------ENGLISH-----------------------------')
    print('Type --mode to change mode')
    print(colored("Hope You Have A Good Day!",'yellow'))
    #Speak('Voices/hi.mp3')    
Run()
    