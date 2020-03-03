# created for use in micro:bit
# and the 12 neopixels ring
import neopixel

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
reds = gen_tail([255, 0, 0], 8)
greens = gen_tail([0, 255, 0], 8)
blues = gen_tail([0, 0, 255], 8)

# current state
current = blues
head = 0

while True:
    spin_tail(current, head)
    sleep(100)

    if button_a.is_pressed():
        current = greens
    elif button_b.is_pressed():
        current = reds
    else:
        current = blues