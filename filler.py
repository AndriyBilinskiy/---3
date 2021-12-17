#!/usr/bin/env python
# -*- coding: utf-8 -*-
from logging import DEBUG, debug, getLogger
import logging

getLogger().setLevel(DEBUG)
logging.basicConfig(filename="test.log", level = logging.DEBUG, 
format='%(asctime)s:%(funcName)s:%(message)s')

def parse_field_info():
    """
    Parse the info about the field.
    Plateau 15 17:
    """

    inp = input()
    debug(f"Description of the field: {inp}")
    inp = inp.split()
    return [inp[1],inp[2][:-1]]


def parse_field():
    """
    This function parses the game field.

    The input may look like this:

        01234567890123456
    000 .................
    001 .................
    002 .................
    003 .................
    004 .................
    005 .................
    006 .................
    007 ..O..............
    008 ..OOO............
    009 .................
    010 .................
    011 .................
    012 ..............X..
    013 .................
    014 .................
    """
    field_height =  int(parse_field_info()[0])
    field = []
    for _ in range(field_height + 1):
        line = input().lower()
        line = line.split()[-1]
        row = []
        for char in line:
            row.append(char)
        field.append(row)
    debug(f"Field: {field}")
    return field


def parse_figure():
    """
    This function parses the figure.

        The input may look like this:

    Piece 2 2:
    **
    ..
    """
    param = input()
    debug(f"Piece: {param}")
    height = int(param.split()[1])
    figure = []
    for _ in range(height):
        figure.append(input())
    debug(f"Figure: {figure}")
    return figure


def find_availible_moves(player:int):
    """
    This function finds all moves that are allowed by the rules.
    """
    if player == 1:
        my_char,enemy_char = 'o','x'
    else:
        enemy_char, my_char = 'o','x'
    field = parse_field()
    figure = parse_figure()
    moves = []
    for i in range(len(field)):
        row = field[i]
        for j in range(len(row)):
            intersection_with_my_char_found = False
            try:
                for k in range(len(figure)):
                    fig_row = figure[k]
                    for n in range (len(fig_row)):
                        fig_char = fig_row[n]
                        field_char = field[i+k][j+n]
                        if fig_char == my_char:
                            assert field_char != enemy_char
                            if field_char == my_char:
                                intersection_with_my_char_found = True
            except IndexError or AssertionError:
                continue
            if intersection_with_my_char_found:
                moves.append(tuple(i,j))
#TODO
    #return moves

def choose_the_best_move(player:int):
    """
    This function chooses the best move out of the list of possible moves. 
    """
    moves = find_availible_moves()
    debug(f"Availible moves {moves}")
    if moves == -1:
        return -1
#TODO
    # return best


def step(player:int):
    """
    This function performs a step.
    """
    move = None
    parse_field_info()
    move = choose_the_best_move(player)
    if move == -1:
        return -1


def play(player:int):
    """
    This function launches step finction every sptep.
    """
    while True:
        move = step(player)
        if move == -1:
            debug("No moves are availible.")
            print("No moves are availible.")
        print(*move)


def parse_player():
    """
    This function finds out weather the player if 1st of 2nd.
    """
    info = input()
    debug(f"Info about the player: {info}")
    return 1 if "p1 :" in info else 2


def main():
    """
    The main function.
    """
    player = parse_player
    try:
        play(player)
    except EOFError:
        debug("Incorrect input")


if __name__ == "__main__":
    main()