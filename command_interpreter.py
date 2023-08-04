import map_data as md
from map import Map
import pyautogui as pt


class CommandInterpreter:

    def __init__(self, commands):
        self.commands = commands        #[(Map.harvest, 0), (Map.harvest, 1)]
        self.previous_map = -1
        self.current_command = None

    def run(self):
        pt.moveTo(220, 1058)
        pt.click()
        pt.moveTo(256, 135)
        pt.click()
        for command in self.commands:
            self.current_command = command
            self.execute()

    def execute(self):
        if self.previous_map != self.current_command[1]:
            self.navigate()
        self.current_command[0](md.maps[self.current_command[1]], *self.current_command[2:])

    def navigate(self):
        if self.previous_map != -1:
            md.maps[self.previous_map].exit()
        md.maps[self.current_command[1]].enter()
        self.previous_map = self.current_command[1]
