Markov Painter\
Drew Hofer\
September 15, 2022

To run:\
Make sure you are in 'Markov-Mission' directory\
On line 107 of Markov.py, enter the name of the painting you would like to simulate (either 'AirplaneFlying.png' and 'deKooning.png')\
Set output image name on line 119 of Markov.py\
Run python3 Markov.py from the command line

This program simulates the paintings of Willem de Kooning and Kazimir Malevich. The Markov transition matrix was constructed by calculating relative probabilities of pixels occurring after any given pixel. The matrix is then used to create original images inspired by the colors and form of de Kooning and Malevich.