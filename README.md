Markov Painter\
Drew Hofer\
September 15, 2022

To run:\
Make sure you are in 'Markov-Mission' directory\
On line 107 of Markov.py, enter the name of the painting you would like to simulate (either 'AirplaneFlying.png' and 'deKooning.png')\
Set output image name on line 119 of Markov.py\
Run 'python3 Markov.py' from the command line\
Output image will be saved to 'examples' directory

This program simulates the paintings of Willem de Kooning and Kazimir Malevich. The Markov transition matrix was constructed by calculating relative probabilities of pixels occurring directly after any given pixel. The matrix is then used to create original images inspired by the colors and form of de Kooning and Malevich.

This system is personally meaningful to me because I am a big fan of the art of Willem de Kooning and Kazimir Malevich. I became more interested in art after I took my first year seminar in the art history department. I specifically like de Kooning and Malevich becuase of the simultaneous ambiguity and simplicity in their work. Each of their pieces has an infinite number of interpretations, yet they remain rooted in a small color palette and their own unique styles. Thus, it was a no brainer for me to use a Markov chain to recreate their work. 

I pushed myself outside of my comfort zone in a number of ways. First, I utilized many tools and techniques that I was completely unfamiliar with before starting the project. I had never used the Python Imaging Library or implemented a Markov chain. Getting familiar with the PIL was no easy task, and took lots of trial and error. Implementing the Markov chain was equally as tricky because I had never seen it implemented in code before. This required copious planning and psuedocode. 

This challenge was important for me because I did not want to do something I already knew how to do. I thought about doing something with turtle, but I already knew how to do that. I thought that would be taking the easy way out. By learning and implementing new tools and methods I was able to create something much mroe meaningful to me. The result was worth the challenge. 

The next steps for me are making the generated paintings look more like the orignials. Obvisouly I do not want to exactly copy them, but I think I could do more with more time. The pixels are read from the original and also reconstructed in a column by column manner. The transition matrix is then only based off the one pixel that was read as the successor for each respective pixel. In actuality, each pixel touches at least 2 (and almost always 4) other pixels. Adjusting the transition matrix to accont for all surrounding pixels would likely lead to a less "streaky" look in the generated images. Nonetheless, I am satisfied with what I was able to accomplish with the amount of time and resources I had available. 

I do believe this system is creative. First and foremost, it is inspired by two of the best painters of all time who broke many barriers in their respective fields. I see the reconstruction of pixels based on their original paintings as putting a creative twist on an already creative object (the paintings). Additionally, no two of my Markov generated paintings will ever be the same. Each one is undoubtedly unique, yet (strives to) simulate the brilliant creative minds of de Kooning and Malevich.

Sources:\
For the inspiration for working with images: https://magenta.as/using-machine-learning-to-make-art-84df7d3bb911 \
For gaining familiarity with the Python Imaging Library: https://magenta.as/using-machine-learning-to-make-art-84df7d3bb911