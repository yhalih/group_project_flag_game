from pygame import *
import time
import soldier


def end(soldier_location, mine_locations):
    body_locations = soldier.soldier_body(soldier_location)
    win = True

    # Finding out if game ended because of win or loss
    for location in body_locations:
        if location in mine_locations:
            win = False

    end_print(win, soldier_location)
    time.sleep(3)
    quit()


def end_print(win, soldier_location):
    if win:
        print("You won!")
    else:
        placement('explosion.png', soldier_location)
        placement('injury', soldier_location)
        print("You lost!")
