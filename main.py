import pyautogui as pt

import map_data as md
from command_interpreter import CommandInterpreter
import command_manager as cm
from map import Map


def init():
    pt.moveTo(220, 1058)
    #pt.click()
    md.load_maps()
    pt.moveTo(256, 135)
    #pt.click()
    cm.run_menu()




if __name__ == '__main__':
    init()

