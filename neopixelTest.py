import board
import digitalio
import time
import neopixel

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

# board.BUTTON
delay = 0.25
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.05, auto_write=False)
    
while True:
    led.value = True
    time.sleep(delay)
    led.value = False
    time.sleep(delay)
    
    pixels.fill(RED)
    pixels.show()
    time.sleep(delay)
    
    pixels.fill(GREEN)
    pixels.show()
    time.sleep(delay)
    
    pixels.fill(BLUE)
    pixels.show()
    time.sleep(delay)
    
    pixels.fill(PURPLE)
    pixels.show()
    time.sleep(delay)
    
    pixels.fill(YELLOW)
    pixels.show()
    time.sleep(delay)
    
    pixels.fill(CYAN)
    pixels.show()
    time.sleep(delay)