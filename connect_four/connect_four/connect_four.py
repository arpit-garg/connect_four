__author__ = 'arpitgarg'
import json
from board import Board

def main():
    input = json.load(open("/tmp/input.json"))
    nrow = input['rows']
    ncol = input['cols']
    moves = input['moves']
    b = Board(nrow, ncol, moves)
    b.move()

if __name__ == "__main__":
    main()
