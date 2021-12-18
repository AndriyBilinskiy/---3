#!/usr/bin/env python
# -*- coding: utf-8 -*-
from logging import DEBUG, debug, getLogger
import logging

getLogger().setLevel(DEBUG)
logging.basicConfig(filename="test.log",level = logging.DEBUG, 
format='%(asctime)s:%(funcName)s:%(message)s')

class BreakLoop( Exception ):
    pass

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
    debug("Field:")
    for _ in range(field_height + 1):
        line = input().lower()
        line = line.split()[-1]
        row = []
        for char in line:
            row.append(char)
        field.append(row)
        debug(row)
    
    return field[1:]


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
    debug("Figure:")
    for _ in range(height):
        row  = input()
        lst = []
        for i in row:
            lst.append(i)
        figure.append(lst)
        debug(lst)
    
    return figure


def find_availible_moves(player:int, field, figure):
    """
    This function finds all moves that are allowed by the rules.
    """
    debug(player)
    if player == 1:
        my_char,enemy_char = 'o','x'
    else:
        enemy_char, my_char = 'o','x'
    debug(my_char)
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
                        if fig_char == '*':
                            if field_char == enemy_char:
                                raise BreakLoop
                            if field_char == my_char:
                                if not intersection_with_my_char_found:
                                    intersection_with_my_char_found = True
                                else:
                                    raise BreakLoop
            except BreakLoop:
                continue
            except IndexError:
                continue
            if intersection_with_my_char_found:
                moves.append((i,j))
    debug(f"Availible moves {moves}")
    return moves

def choose_the_best_move(player:int):
    """
    This function chooses the best move out of the list of possible moves. 
    It does it by finding the aproximate closest move to the enemy.
    """
    if player == 1:
        enemy_char = 'x'
    else:
        enemy_char = 'o'
    field = parse_field()
    figure = parse_figure()
    moves = find_availible_moves(player, field, figure)
    num_of_stars = 0
    y_sum = 0
    x_sum = 0
    for i in range(len(figure)):
        row = figure[i]
        for j in range(len(row)):
            if row[j] == '*':
                num_of_stars += 1
                y_sum += i
                x_sum += j
    y_center = y_sum / num_of_stars
    x_center = x_sum / num_of_stars
    if len(moves) == 0:
        return -1 
    distances = []
    for move in moves:
        move_y = move[0] + y_center
        move_x = move[1] + x_center
        distance_to_enemy = 0
        for i in range(len(field)):
            row = field[i]
            for j in range(len(row)):
                if row[j] == enemy_char:
                    distance_to_enemy += abs(move_y - i) + abs(move_x - j)
        distances.append((move, distance_to_enemy))
    debug(distances)
    return min(distances, key = lambda x: x[1])[0]


def step(player:int):
    """
    This function performs a step.
    """
    move = choose_the_best_move(player)
    if move == -1:
        return -1
    return move

def play(player:int):
    """
    This function launches step finction every sptep.
    """
    while True:
        move = step(player)
        debug(move)
        if move == -1:
            debug("No moves are availible.")
            move = (0,0)
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
    player = parse_player()
    try:
        play(player)
    except EOFError:
        debug("Incorrect input")


if __name__ == "__main__":
    main()
