import numpy as np
import random
from PIL import Image

class MarkovMalevich:

    def __init__(self, pixels, width, height, mode):
        self.pixels = pixels
        self.output = pixels
        self.width = width
        self.height = height
        self.mode = mode

    def gen_new_pixels(self):
        new_image = Image.new(self.mode, (self.width, self.height))
        self.output = new_image.load()
        return new_image

    def gen_new_image(self):
        # Print(pixels[0,0]) is the format for using pixel data
        for x in range(self.width):
            for y in range(self.height):
                self.output[x, y] = self.pixels[x, y]



def main():
    airplane_flying = Image.open("AirplaneFlying.jpg", 'r')
    width, height = airplane_flying.size

    airplane_flying_mode = airplane_flying.mode
    pixels = airplane_flying.load()

    markov_inspired_malevich = MarkovMalevich(pixels, width, height, airplane_flying_mode)
    new_image = markov_inspired_malevich.gen_new_pixels()
    markov_inspired_malevich.gen_new_image()

    new_image.save('NewImage3.png')

if __name__ == "__main__":
    main()

