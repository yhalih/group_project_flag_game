from pygame import *
import random
from consts import *
import soldier

def creating_empty_board():
    empty_board = display.set_mode(PIXEL_ROWS, PIXEL_COLS)
    return empty_board


def placement(board, item_, wanted_place):
    pic_item= image.load(f'C:\\Users\\jbt\\Desktop\\python\\group_project_flag_game\\bin\\{item_}').convert()
    board.blit(pic_item, wanted_place)
    return board


def random_bush_bomb(repeted_item, board, bomb_bush_num= BUSH_BOMB_NUM):
    places_list=[]
    flag_and_start=[soldier.soldier_legs, soldier.soldier_body]
    while len(places_list)<bomb_bush_num:
        rand_x=
        rand_y=
        rand_tup= (rand_x, rand_y)
        if rand_tup


