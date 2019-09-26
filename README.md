# Tick-Tac-Toe AI in Python
For those tricky situations when you don't have a partner to play tic-tac-toe with.
This AI learns to play the game (and if it can't come up with a move it'll randomly pick one)
until it will either beat you or tie with you every game.  Play at your own risk!

# Modules Used
In order to create this I used the NEAT package to create the FeedForward neural network
and got a base config file from Tech With Tim on youtube (https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg).


# Startup python environment
## on windows
ENV\Scripts\activate
## on mac or Unix
source ENV/bin/activate

Once the environment has been initialized run main.py and you will be playing against the ai in a terminal.
One thing to note is that if the AI cannot make a move the move will be randomized and its fitness will decrease!