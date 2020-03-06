# created for use in micro:bit
# and the 12 neopixels ring
# use the micro:bit radio color to control the color of the spinning tail

import neopixel
import radio
from microbit import *

# which pin and number of pixels
pixels = neopixel.NeoPixel(pin2, 12)

# generate color
def gen_tail(seed, length):
    arr = []
    step_size = length
    step_red = seed[0] / step_size if seed[0] > 0 else 0
    step_green = seed[1] / step_size if seed[1] > 0 else 0
    step_blue = seed[2] / step_size if seed[2] > 0 else 0
    for idx in range(0, length):
        red = round(seed[0] - (idx * step_red)) if step_red > 0 else 0
        green = round(seed[1] - (idx * step_green)) if step_green > 0 else 0
        blue = round(seed[2] - (idx * step_blue)) if step_blue > 0 else 0
        arr.append([red, green, blue])
    return arr

def spin_tail(arr, i):
    pixels.clear()
    for pixel_id in range(0, len(arr)):
        if i - pixel_id < 0:
            pixels[len(pixels) + (i - pixel_id)] = arr[pixel_id]
        else:
            pixels[i - pixel_id] = arr[pixel_id]
    pixels.show()

# generate and seed with each color
map = {'R': 0, 'G': 0, 'B': 0}
num = 8
tail = gen_tail([map['R'], map['G'], map['B']], num)

# current state
head = 0
radio.on()

while True:
    message = radio.receive()
    if message is not None and len(message) > 1 and (message[0] == 'R' or message[0] == 'G' or message[0] == 'B'):
        map[message[0]] = int(message[1:])
        tail = gen_tail([map['R'], map['G'], map['B']], num)

    spin_tail(tail, head)
    sleep(100)

    head += 1
    if head > 11:
        head = 0



