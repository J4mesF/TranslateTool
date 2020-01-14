


import pygame as pg


def Speak(name):
    
     
    volume=0.8
    # set up the mixer
    freq = 29999     # audio CD quality
    bitsize = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = 2048    # number of samples (experiment to get best sound)
    pg.mixer.init(freq, bitsize, channels, buffer)
    # volume value 0.0 to 1.0
    pg.mixer.music.set_volume(volume)
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(name)
    except pg.error:
        return
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        clock.tick(30)
