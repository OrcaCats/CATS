#functionize
import sys
import subprocess
try:
    import platform
except ImportError:
    print('Module platform not found')
def install_pack(dependency):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', dependency])
    print(f'Successfully installed: {dependency}')
# Dependency list
dependencies = ['keras-ocr',     #text recognizer
                'pyautogui',     #screenshoter
                'pynput'         #input listener
                ]
for package in dependencies:
    install_pack(package)
print(f'Platform name: {platform.system()}')

#------------------------------------------------------------------------------------
#inplement check system exception

class screenshot:
    def __init__(self):
        import pyautogui
        import pynput
        self.cords[0, 0, 0, 0]
        self.screenshot
    def logCords(self, cords):
        #listener = 
        
    def shoot(self, cords):
        self.screenshot = pyautogui.screenshot(region=(x, y, w, h))
        
class recog:
    def __init__(self):
        import keras_ocr
        import matplotlib.pyplot as plt
        pipeline = keras_ocr.pipeline.Pipeline()

