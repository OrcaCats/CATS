def importDependencies():
    import sys
    import subprocess
    try:
        import platform
    except ImportError as e:
        print(e)
    # Dependency list
    dependencies = ['keras-ocr',     #text recognizer
                    'pyautogui',     #screenshoter  
                    'pynput'         #input listener
                    ]
    for package in dependencies:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', dependency])
        print(f'Successfully installed: {dependency}')
    print(f'Platform name: {platform.system()}')

#-------------------------------------------------------------------------------------------------------------------------------
#inplement check system exception

class screenshot:
    def __init__(self):
        #imports within function for procedural purposes
        global pyautogui
        global pynput
        import pyautogui
        import pynput
        self.cords[0, 0, 0, 0]
        self.screenshot
    def logCords(self, cords):

        #listener = 
        
    def shoot(self, cords):
        self.screenshot = pyautogui.screenshot(region=(x, y, w, h))

class mouseListener:
    def __init__(self):
        pass
    
    def start(self): #different from init because of ctrl of listener. parent classes init
        listener = mouse.Listener()
        print('Listener Started')






#primary reader
class recogEasyOCR:
    def __init__(self):
        global easyocr
        import easyocr
        self.reader = easyocr.Reader(['en'])
    def read(self):
        self.result = self.reader.readtext('Screenshot 2024-02-29 211938.png', detail = 0)
        print(result)

#secondary reader, used if easyOCR isnt available
class recogKeras:
    def __init__(self): 
        import matplotlib.pyplot as plt
        pipeline = keras_ocr.pipeline.Pipeline()

if __name__=='__main__':
    importDependencies()