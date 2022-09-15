import numpy as np
import random
from PIL import Image

class MarkovPainting:

    def __init__(self, pixels, width, height, mode):
        """
        Simulates a painting in the style of de Kooning or Malevich based on a Markov chain.
        Args:
            pixels (PixelAccess): pixels from original painting
            width (int): width of painting
            height (int): height of painting
            mode (str): mode of painting
        """
        self.pixels = pixels
        self.output = pixels
        self.width = width
        self.height = height
        self.mode = mode
        self.matrix = {}

    def gen_new_pixels(self):
        """
        Generates the pixels of the new (Markov chain generate) painting
        """
        new_image = Image.new(self.mode, (self.width, self.height))
        self.output = new_image.load()
        return new_image

    def assemble_new_image(self):
        """
        Assembles the image of the new (Markov chain generate) painting
        """
        prev_pixel = self.pixels[random.randint(0, self.width-1), random.randint(0, self.height-1)]
        for x in range(self.width):
            for y in range(self.height):
                if x == 0 and y == 0:
                    self.output[x, y] = prev_pixel
                    prev_pixel = self.output[x, y]
                else:
                    self.output[x, y] = self.determine_next(prev_pixel)
                    prev_pixel = self.output[x, y]

    def determine_next(self, prev_pixel):
        """
        Determines the next pixel of the painting based on the previous pixel
        Args:
            prev_pixel (tuple): the previous pixel
        """
        rand = random.random()
        if rand < 0.005:
            return self.pixels[random.randint(0, self.width-1), random.randint(0, self.height-1)]
        seen = 0.0
        count = 0
        keys = list(self.matrix[prev_pixel].keys())
        vals = list(self.matrix[prev_pixel].values())
        while seen < rand:
            seen += vals[count]
            count += 1

        return keys[count-1]

    def get_next_pixel(self, x, y):
        """
        Gets the next pixel of the painting to be assembled
        Args:
            x (int): x coordinate of previous pixel
            y (int): y coordinate of previous pixel
        """
        if x != self.width-1 and y != self.height-1:
            return self.pixels[x, y+1]
        elif y == self.height-1 and x != self.width-1: # end of column
            return self.pixels[x+1, 0]
        else: # last pixel
            return self.pixels[self.width-1, self.height-1]

    def gen_counts(self):
        """
        Generates the counts of successor pixels into the transition matrix
        """
        for x in range(self.width):
            for y in range(self.height):
                curr_pixel = self.pixels[x, y]
                next_pixel = self.get_next_pixel(x, y)
                if curr_pixel not in self.matrix.keys():
                    self.matrix[curr_pixel] = {next_pixel : 1}
                elif curr_pixel in self.matrix.keys() and next_pixel in self.matrix[curr_pixel].keys():
                    self.matrix[curr_pixel][next_pixel] += 1
                else:
                    self.matrix[curr_pixel][next_pixel] = 1

    def adjust_matrix_to_probabilities(self):
        """
        Turns the counts of successor pixels into probabilities inside the transition matrix
        """
        for item in self.matrix.keys():
            vals = list(self.matrix[item].values())
            keys = list(self.matrix[item].keys())
            total = sum(vals)
            seen = 0
            for dict in self.matrix[item]:
                self.matrix[item][keys[seen]] = vals[seen]/total
                seen += 1

def main():
    original_painting = Image.open("deKooning.jpg", 'r') # read painting
    width, height = original_painting.size # get height and width

    pic_mode = original_painting.mode # get mode
    pixels = original_painting.load() # lod pixels

    markov_inspired_painting = MarkovPainting(pixels, width, height, pic_mode)
    markov_inspired_painting.gen_counts()
    markov_inspired_painting.adjust_matrix_to_probabilities()
    new_image = markov_inspired_painting.gen_new_pixels()
    markov_inspired_painting.assemble_new_image() # assemble new painting

    new_image.save('examples/MalevichMarkov5.png') # save new painting to examples directory

if __name__ == "__main__":
    main()

