import pyautogui as pt
import time
import click_verify_support as cv


class Map:
    def __init__(self, name, map_access, access, water=None, sub_access=None, escape=None):
        self.name = name
        self.map = map_access
        self.access = access
        self.water = water
        self.sub_access = sub_access
        self.escape = escape
        self.tiles = []
        self.load_tiles()

    def load_tiles(self):
        file = open(self.name + ".txt", 'r')
        f = file.readlines()
        for line in f:
            list = line.strip().split(',')
            self.tiles += [(int(list[0]), int(list[1]))]

    def watering(self, iterator=None):
        tiles_iter = iter(self.tiles)
        if iterator is not None:
            tiles_iter = iterator
        for tile in tiles_iter:
            pt.moveTo(tile[0], tile[1])
            pt.click()
            try:
                position1 = pt.locateOnScreen('water.png', confidence=0.8)
                pt.moveTo(position1[0] + 25, position1[1] + 25)
                time.sleep(0.1)
                try:
                    position2 = pt.locateOnScreen('water_lightning.png', confidence=0.8)
                    pt.moveTo(position2[0] + 25, position2[1] + 25)
                    pt.click()
                    for tile in tiles_iter:
                        pt.moveTo(tile[0], tile[1])
                        pt.click()
                        if pt.locateOnScreen('water_1.png', confidence=0.9) is not None or pt.locateOnScreen(
                                'out_of.png', confidence=0.8) is not None:
                            if pt.locateOnScreen('out_of.png', confidence=0.8) is not None:
                                pt.moveTo(960, 870)
                                pt.click()
                            self.refill_water()
                            self.watering(tiles_iter)
                    return
                except:
                    print("No lightning water image found")
                    pt.moveTo(1626, 955)
                    pt.click()
            except:
                print("No water image found")
                pt.moveTo(1626, 955)
                pt.click()

    def sowing(self, number):
        if number > 7 or number < 0:
            raise Exception('Sowing number must be between 0 and 7!')
        for tile in self.tiles:
            pt.moveTo(tile[0], tile[1])
            pt.click()
            try:
                position1 = pt.locateOnScreen('sowing.png', confidence=0.8)
                pt.moveTo(position1[0] + 25, position1[1] + 25)
                time.sleep(0.1)
                try:
                    position2 = pt.locateOnScreen('sowing_lightning.png', confidence=0.8)
                    pt.moveTo(position2[0] + 25, position2[1] + 25)
                    pt.click()
                    time.sleep(0.1)
                    try:
                        position3 = pt.locateOnScreen('sowing_select.png', confidence=0.8)
                        pt.moveTo(position3[0] + 100 + number * 85, position3[1] + 100)
                        pt.click()
                        self.sweep()
                        return
                    except:
                        print("No sowing select found")
                        pt.moveTo(1626, 955)
                        pt.click()
                except:
                    print("No lightning sowing image found")
                    pt.moveTo(1626, 955)
                    pt.click()
            except:
                print("No sowing image found")
                pt.moveTo(1626, 955)
                pt.click()

    def refill_water(self):
        cv.verify_click_with_picture(self.water[0], self.water[1], 'storage.png', "Storage not found")
        cv.verify_click_with_picture(840, 880, 'water_buy.png', "Water buy option not found")
        cv.verify_click_with_picture(1000, 870, 'storage.png', "Water buy was not successful")
        cv.verify_click_with_no_picture(1460, 240, 'storage.png', "Exit from storage was not successful")

    def sweep(self):
        for tile in self.tiles:
            pt.moveTo(tile[0], tile[1])
            pt.click()

    def harvest(self):
        for tile in self.tiles:
            pt.moveTo(tile[0], tile[1])
            pt.click()
            position = pt.locateOnScreen('in.png', confidence=0.8)
            if position is not None:
                pt.moveTo(position[0] + 25, position[1] + 25)
                pt.click()
            else:
                print("No image found")
                pt.moveTo(1626, 955)
                pt.click()

    def harvest_and_feed(self):
        for tile in self.tiles:
            pt.moveTo(tile[0], tile[1])
            pt.click()
            position = pt.locateOnScreen('in.png', confidence=0.8)
            position2 = pt.locateOnScreen('fertilizer.png', confidence=0.8)
            position3 = pt.locateOnScreen('feed.png', confidence=0.8)
            if position is not None:
                pt.moveTo(position[0] + 25, position[1] + 25)
                pt.click()
            elif position2 is not None:
                pt.moveTo(position2[0] + 25, position2[1] + 25)
                pt.click()
            elif position3 is not None:
                pt.moveTo(position3[0] + 25, position3[1] + 25)
                pt.click()
                self.check_and_exit_mill()
            else:
                print("No image found")
                pt.moveTo(1626, 955)
                pt.click()

    def check_and_exit_mill(self):
        if pt.locateOnScreen('mill.png', confidence=0.8) is not None:
            cv.verify_click_with_picture(1435, 230, 'mill.png', "Mill not found")
            cv.verify_click_with_no_picture(1535, 220, 'mill.png', "Mill not found")

    def exit(self):
        while True:
            pt.moveTo(self.map[0], self.map[1])
            pt.click()
            if pt.locateOnScreen('enter_confirm.png', confidence=0.8) is None:
                pt.moveTo(256, 135)
                pt.click()
                break
            print("Exit was not successful")
        if self.escape != None:
            while True:
                pt.moveTo(self.escape[0], self.escape[1])
                pt.click()
                if pt.locateOnScreen('exit_confirm.png', confidence=0.8) is not None:
                    pt.moveTo(256, 135)
                    pt.click()
                    break
                print("Exit was not successful")

    def enter(self):
        if self.sub_access != None:
            while True:
                pt.moveTo(self.sub_access[0], self.sub_access[1])
                pt.click()
                if pt.locateOnScreen('baha_enter_confirm.png', confidence=0.8) is not None or pt.locateOnScreen(
                        'baha_enter_confirm.png', confidence=0.8) is not None:
                    pt.moveTo(1626, 955)
                    pt.click()
                    break
                print("Sub access was not successful")

        while True:
            pt.moveTo(self.access[0], self.access[1])
            pt.click()
            if pt.locateOnScreen('enter_confirm.png', confidence=0.8) is not None:
                pt.moveTo(1626, 955)
                pt.click()
                break
            print("Access was not successful")
