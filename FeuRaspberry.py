import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

led_vert1 = 7
led_vert2 = 11
led_orange1 = 12
led_orange2 = 13
led_rouge1 = 15
led_rouge2 = 16

GPIO.setup(led_vert1, GPIO.OUT)
GPIO.setup(led_vert2, GPIO.OUT)
GPIO.setup(led_orange1, GPIO.OUT)
GPIO.setup(led_orange2, GPIO.OUT)
GPIO.setup(led_rouge1, GPIO.OUT)
GPIO.setup(led_rouge2, GPIO.OUT)

while True:
    GPIO.output(led_vert1, True)
    GPIO.output(led_rouge2, True)
    GPIO.output(led_vert2, False)
    GPIO.output(led_rouge1, False)
    GPIO.output(led_orange1,False)
    GPIO.output(led_orange2, False)
    time.sleep(5)
    GPIO.output(led_orange1, True)
    GPIO.output(led_vert1, False)
    GPIO.output(led_rouge2, True)
    GPIO.output(led_orange2,False)
    GPIO.output(led_vert2,False)
    GPIO.output(led_rouge1,False)
    time.sleep(2)
    GPIO.output(led_vert2, True)
    GPIO.output(led_rouge1, True)
    GPIO.output(led_rouge2, False)
    GPIO.output(led_orange1, False)
    GPIO.output(led_vert1,False)
    GPIO.output(led_orange2, False)
    time.sleep(5)
    GPIO.output(led_orange2, True)
    GPIO.output(led_vert2, False)
    GPIO.output(led_rouge1, True)
    GPIO.output(led_orange1, False)
    GPIO.output(led_vert1, False)
    GPIO.output(led_rouge2, False)
    time.sleep(2)
