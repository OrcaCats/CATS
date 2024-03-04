#init var definition
dependencies = ['easyocr',     #primary text recognizer
                'keras-ocr',       #secondary text recognizer
                'pyautogui',     #screenshoter  
                'keyboard',      #input listener
                'mouse'
                ]



#add runtime tracker
class mouseLogger:
    def __init__(self):
        self.running = False
        self.runtimes = 0
        self.cords = []
    def start(self):
        if not self.running:
            self.running = True
            keyboard.hook(self.onKey)
            #keyboard.wait('s')
            while self.runtimes < 2: #stops after 2 cords
                pass
            self.stop()
    def stop(self):
        if self.running:
            self.running = False
            keyboard.unhook_all()
    def onKey(self, e):
        if e.event_type == keyboard.KEY_DOWN and e.name == 'a':
            mouse_position = get_position()
            #print(mouse_position)   #debug
            self.cords.append(mouse_position) 
            self.runtimes += 1



class screenshot:
    def __init__(self):
        #imports within function for procedural purposes
        global pyautogui
        global pynput
        import pyautogui
        import pynput
        self.cords = [0, 0, 0, 0]
    def logCords(self):
        print('a')
        self.logger = mouseLogger()
        self.logger.start()
        self.cords[0], self.cords[1], self.cords[2], self.cords[3]= self.logger.cords[0][0], self.logger.cords[0][1], self.logger.cords[1][0] - self.logger.cords[0][0], self.logger.cords[1][1] - self.logger.cords[0][1]
        d.debug(self.cords[1], 'N')
        print(f'Xpos: {self.cords[0]}| Ypos: {self.cords[1]}| Width: {self.cords[2]}| Height: {self.cords[3]}|')
    def shoot(self):
        self.screenshot = pyautogui.screenshot(region=(self.cords[0], self.cords[1], self.cords[2], self.cords[3]))
        self.screenshot.save('scrshot.png')


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
    import keyboard as keyboard
    from mouse import get_position
    import Debug
    #check dependancyes and install
    #importDependencies(dependencies)
    d = Debug.debug()
    scr = screenshot()
    scr.logCords()
    scr.shoot()

#aaaaaaaaaaaaaaaa