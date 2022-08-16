import os
import time
import psutil
import cv2
import pyscreenshot as ImageGrab
import keyboard

from parse_cmd import getCmdArgs

class Game():
    def __init__(self):
        self.path = getCmdArgs()['input']
        self.save_data_path = getCmdArgs()['output']
        self.pid = None

    def launch(self):
        os.startfile(self.path)
        self.pid = self.get_pid()

    def exit(self):
        if self.pid:
            p = psutil.Process(self.pid)
            p.terminate()
        else:
            return 'no pid found'

    def get_pid(self):
        for process in psutil.process_iter():
            if process.name() == game.path.split('\\')[-1]:
                return process.pid
        return None

    def load_check(self):
        check = False
        while True:
            img = ImageGrab.grab()
            img.save(self.save_data_path + '/main_scene_after_loading.png')
            image = cv2.imread(self.save_data_path + '/main_scene_after_loading.png')
            (r, g, b) = image[370, 170]
            (r1, g1, b1) = image[170, 370]
            (r2, g2, b2) = image[470, 770]
            (r3, g3, b3) = image[750, 750]
            if (r, g, b) == (255, 255, 255) and \
                    (r1, g1, b1) == (0, 0, 0) and \
                    (r2, g2, b2) == (0, 0, 0) and \
                    (r3, g3, b3) == (0, 0, 0):
                if not check:
                    check = True
                continue
            if check:
                break

    def moving(self):
        time.sleep(4)
        keyboard.press("ENTER")
        time.sleep(0.1)
        keyboard.release("ENTER")
        time.sleep(0.1)
        keyboard.press("ENTER")
        time.sleep(0.1)
        keyboard.release("ENTER")
        time.sleep(0.3)
        keyboard.press("N")
        time.sleep(0.7)
        keyboard.release("N")
        time.sleep(0.3)
        keyboard.press('W')
        time.sleep(17)
        keyboard.release('W')

    def finish_scene(self):
        img = ImageGrab.grab()
        img.save(self.save_data_path + '/finish_scene.png')
        time.sleep(0.3)

if __name__ == '__main__':
    game = Game()
    game.launch()
    game.load_check()
    game.moving()
    game.finish_scene()
    game.exit()

