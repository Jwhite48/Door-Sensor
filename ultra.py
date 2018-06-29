#Libraries
import RPi.GPIO as GPIO
from gpiozero import Button
import time
import datetime
import os
import random

#Disable warnings
GPIO.setwarnings(False)

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

#Button Setup
Travis = Button(26)
Jesse = Button(19)
Tyler = Button(13)
Ian = Button(6)
Will = Button(5)
Miguel = Button(11)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

#Play a random song from an array of files determiend
#by intervals of time
def sensor():
    if(distance()<=10):
        #Next line for testing the time intervals:
        #now = datetime.now() + datetime.timeDelta(hour=8)
        now = datetime.datetime.now()
        #Time Interval 12am - 8am
        if(now.hour >=0 and now.hour<8):
            files = ["ARFARF.wav", "blegh.mp3", "DEATH.mp3", "probably.wav", "yaaaaa.wav", "Crickets.mp3", "Crickets.mp3", "Crickets.mp3", "Crickets.mp3", "Crickets.mp3", "Crickets.mp3", "Crickets.mp3", "Crickets.mp3", "Crickets.mp3", "Crickets.mp3", "Crickets.mp3", "Crickets.mp3", "Crickets.mp3", "Crickets.mp3", "Crickets.mp3", "Crickets.mp3", "Crickets.mp3", "Crickets.mp3", "Crickets.mp3", "Crickets.mp3"]
        #Time Interval 8am - 1pm
        elif(now.hour >=8 and now.hour<13):
            files = ["03.mp3", "04.mp3", "05.mp3", "07.mp3", "09.mp3", "10.mp3", "11.mp3", "12.mp3", "13.mp3", "14.mp3", "15.mp3", "16.mp3", "17.mp3", "18.mp3", "19.mp3", "20.mp3", "21.mp3", "22.mp3", "23.mp3", "24.mp3", "25.mp3", "26.mp3", "80.mp3", "Fail.wav", "Laugh.mp3", "Win.mp3"]
        #Time Interval 1pm - 2pm
        elif(now.hour >=13 and now.hour<14):
            files = ["ARFARF.wav", "blegh.mp3", "DEATH.mp3", "probably.wav", "yaaaaa.wav"]
        #Time Interval 2pm - 6pm
        elif(now.hour >=14 and now.hour<18):
            files = ["03.mp3", "04.mp3", "05.mp3", "07.mp3", "09.mp3", "10.mp3", "11.mp3", "12.mp3", "13.mp3", "14.mp3", "15.mp3", "16.mp3", "17.mp3", "18.mp3", "19.mp3", "20.mp3", "21.mp3", "22.mp3", "23.mp3", "24.mp3", "25.mp3", "26.mp3", "Applause.mp3", "ComeTogether.wav", "Macho.mp3", "NO.mp3", "Smash.wav", "YA.mp3"]
        #Time Interval 6pm - 12am
        elif(now.hour >=18 and now.hour<24):
            files = ["03.mp3", "04.mp3", "05.mp3", "07.mp3", "09.mp3", "10.mp3", "11.mp3", "12.mp3", "13.mp3", "14.mp3", "15.mp3", "16.mp3", "17.mp3", "18.mp3", "19.mp3", "20.mp3", "21.mp3", "Gay.wav", "22.mp3", "23.mp3", "24.mp3", "25.mp3", "26.mp3", "AirHorn.mp3", "Cena.mp3", "Cheer.mp3", "Evil.mp3", "whistle.mp3"]

        n = random.randint(0, len(files)-1)
        sound = files[n]
        #Runs terminal command to play file
        os.system("omxplayer "+sound+" &")
        print ("Playing "+sound)
        time.sleep(10)

#Customized buttons that play theme songs for each suitemate
def buttonman():
    button = False
    #Creates customized array of theme songs
    #Sets button equal to true
    if(Travis.is_pressed):
        Travis.wait_for_press(timeout=None)
        Travis.wait_for_release(timeout=None)
        files = ["Travis1.wav", "Travis2.wav", "Travis3.wav"]
        button = True

    elif(Jesse.is_pressed):
        Jesse.wait_for_press(timeout=None)
        Jesse.wait_for_release(timeout=None)
        files = ["oman.wav", "grill.wav"]
        button = True

    elif(Tyler.is_pressed):
        Tyler.wait_for_press(timeout=None)
        Tyler.wait_for_release(timeout=None)
        files = ["GG.wav", "SNC.wav"]
        button = True

    elif(Ian.is_pressed):
        Ian.wait_for_press(timeout=None)
        Ian.wait_for_release(timeout=None)
        files = ["Ian.wav"]
        button = True

    elif(Will.is_pressed):
        Will.wait_for_press(timeout=None)
        Will.wait_for_release(timeout=None)
        files = ["Will.wav"]
        button = True

    elif(Miguel.is_pressed):
        Miguel.wait_for_press(timeout=None)
        Miguel.wait_for_release(timeout=None)
        files = ["Miguel.wav"]
        button = True

    #If a button was pressed, picks a random theme song from the array
    #uses terminal to play sound
    if(button):
        n = random.randint(0, len(files)-1)
        sound = files[n]
        os.system("omxplayer "+sound+" &")
        print ("playing "+sound)
        time.sleep(15)

if __name__ == '__main__':
    while True:
        sensor()
        buttonman()
