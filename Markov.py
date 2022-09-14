import numpy as np
import random
from PIL import Image

def main():
    airplane_flying = Image.open("AirplaneFlying.jpg", 'r')
    width, height = airplane_flying.size
    airplane_flying_mode = airplane_flying.mode
    
    pixels = airplane_flying.load()
    #print(pixels[0,0]) is the format for using pixel data

    new_image = Image.new(airplane_flying_mode, (width, height))
    new_pixels = new_image.load()

    for x in range(width):
        for y in range(height):
            # Copy the original pixel to the new pixel map.
            new_pixels[x, y] = pixels[x, y]
            # new_pixels[x, y] = pixels[random.randint(0, width-1), random.randint(0, height-1)]
            # random pixels

    new_image.save('NewImage.png')

if __name__ == "__main__":
    main()

