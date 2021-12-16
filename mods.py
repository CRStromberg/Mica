import pygame
import RPi.GPIO as GPIO
import time

def aud():
    pygame.mixer.init()
    pygame.mixer.music.load("test.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    
def motor():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.out)

    p = GPIO.PWM(12, 50)

    p.start(2.5)
    p.ChangeDutyCycle(2.5)
    time.sleep(5)
    p.ChangeDutyCycle(7.5)
    time.sleep(1)
    p.ChangeDutyCycle(2.5)

    p.stop()
    GPIO.cleanup()
