## Instructions

Implementation of the game [Connect-4](http://en.wikipedia.org/wiki/Connect_Four).

In Connect-4, there are two players, and each of the players take turns trying to get four or more of their game pieces in a row.
 
This is a functional subset of a presumably large code for the game board, game pieces, and player state. The code includes functions to place a piece into the game board and check if one of the players has won the game.

This code prints out the board, in ASCII. For example, here is a plausible print out after two turns - one from player 'x' and player 'o':
 
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * x o * * * *
 

At the end of a game, the program prints the following to stdout:

    Player x won! n pieces played.

Where `x` is either 1 or 2, and `n` is the total number of pieces played on the board. If there's no winner, it prints "Draw". Examples:

    Player 1 won! 7 pieces played.
    Player 2 won! 11 pieces played.
    Draw


## Running the code using docker

These commands will be used to build and run your docker image:

    docker build --tag connect_four .
    docker run -v $(pwd)/games/example.json:/tmp/input.json connect_four

example.json contains the already given moves between two players. You may change the file to give your own set of moves or fork it and change the code to give custom moves using command line.

Game moves (alternating between both players) and board size (could be significantly larger than a standard Connect-4 board) is specified in a JSON file mounted at `/tmp/input.json` within the Docker image. 