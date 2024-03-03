#init var definition
dependencies = ['easyocr',     #primary text recognizer
                'keras-ocr',       #secondary text recognizer
                'pyautogui',     #screenshoter  
                'keyboard',      #input listener
                'mouse'
                ]

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
        self.logger = mouseCords()

        #listener = 
        
    def shoot(self, cords):
        self.screenshot = pyautogui.screenshot(region=(x, y, w, h))


#add runtime tracker
class mouseLogger:
    def __init__(self):
        self.running = False
        self.runtimes = 0
    def start(self):
        if not self.running:
            self.running = True
            keyboard.hook(self.onKey)
            keyboard.wait('s')
            self.stop
    def stop(self):
        if self.running:
            self.running = False
            keyboard.unhook_all()
    def onKey(self, e):
        if e.event_type == keyboard.KEY_DOWN and e.name == 'a':
            mouse_position = get_position()
            return mouse_position
            self.runtimes += 1


#primary reader
class recogEasyOCR:
    def __init__(self):
        global easyocr
        import easyocr
        self.reader = easyocr.Reader(['en'])
    def read(self):
        self.result = self.reader.readtext('Screenshot 2024-02-29 211938.png', detail=0)
#secondary reader, used if easyOCR isnt available
class recogKeras:
    def __init__(self): 
        import matplotlib.pyplot as plt
        pipeline = keras_ocr.pipeline.Pipeline()


if __name__=='__main__':
    from ImportTree import importDependencies
    #check dependancyes and install
    #importDependencies(dependencies)

import keyboard as keyboard
from mouse import get_position
logger = mouseLogger()
logger.start()

'''
class mouseCords:
    def __init__(self):
        from pynput import mouse as mouse
        from pynput import keyboard
        self.listener = None
        self.keyListener = keyboard.Listener(on_press=self.onAltQ) #sets up keyboard listener
        self.startMouse()
        #self.keyListener.start()
        pass
    
    def startMouse(self): #different from init because of ctrl of listener. parent classes init
        if self.listener is None:
            self.listener = mouse.Listener()
            print('Listener Started')
            with self.listener as listener:
                listener.join()

    def stopMouse(self):
        if self.listener is not None:
            self.listener.stop()
            self.listener = None #deinits listener function
            print('spywa-- achem listener, stopped')

    def onAltQ(self, key): #detects when alr r is pressed and activates mouse
        try:
            if key.char == 'q' and any([keyboard.Key.ctrl in key_modifiers for key_modifiers in key.modifiers]):
                self.startMouse()
        except AttributeError: #catches non-char keys
            pass

    def onClick(self, x, y, button, pressed):
        if pressed:
            print(f'click at {x}, {y}')
            self.stopMouse()
'''