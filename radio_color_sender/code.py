import radio
import math
from microbit import *

radio.on()

def get_linear_img(bino):
    img = (25 - bino) * '0' + bino * '1'
    img = '{0}:{1}:{2}:{3}:{4}'.format(img[0:5], img[5:10], img[10:15], img[15:20], img[20:25])
    return Image(img)

which = 'R'
mode = 'setup'

rr = ['R', 'G', 'B']
rv = [0, 0, 0]
ri = 0

def which_color():
    return rr[ri % len(rr)]

def which_value():
    return rv[ri % len(rr)]

def update_value(dev):
    rv[ri % len(rr)] = rv[ri % len(rr)] + dev

def reset():
    mode = 'setup'
    display.scroll(mode)
    display.scroll(which_color())
    # reset button presses
    button_a.was_pressed()
    button_b.was_pressed()

reset()

while True:
    if mode == 'setup':
        if button_a.was_pressed():
            ri += 1
            display.scroll(which_color())
        if button_b.was_pressed():
            mode = 'play'
            display.scroll(mode)
    else:
        if button_a.is_pressed() and button_b.is_pressed():
            reset()
        else:
            old_val = which_value()
            if button_a.was_pressed() and which_value() > 0:
                update_value(-1)
            elif button_b.was_pressed() and which_value() < 25:
                update_value(1)

            if old_val != which_value():
                radio.send(which_color() + str(which_value() * 10))
                display.show(get_linear_img(which_value()))
                print(which_color() + str(which_value() * 10))
