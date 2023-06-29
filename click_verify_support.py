import pyautogui as pt


def verify_click_with_picture(x, y, name, error=None, fallback_x=256, fallback_y=135, confidence=0.8):
    while True:
        pt.moveTo(x, y)
        pt.click()
        if pt.locateOnScreen(name, confidence=confidence) is not None:
            pt.moveTo(fallback_x, fallback_y)
            pt.click()
            return
        if error is not None:
            print(error)


def verify_click_with_no_picture(x, y, name, error=None, fallback_x=256, fallback_y=135, confidence=0.8):
    while True:
        pt.moveTo(x, y)
        pt.click()
        if pt.locateOnScreen(name, confidence=confidence) is None:
            pt.moveTo(fallback_x, fallback_y)
            pt.click()
            return
        if error is not None:
            print(error)
