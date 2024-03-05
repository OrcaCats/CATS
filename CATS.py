#init var definition
dependencies = ['easyocr',       #primary text recognizer
                'keras-ocr',     #secondary text recognizer
                'pyautogui',     #screenshoter  
                'keyboard',      #input listener
                'mouse',         #mouse locator
                'cv2'
                ]
screenShotName = 'scrshot.png'
devmode = 'Y' #sets the developer mode, y activates developer controls, NO NOT CHANGE

#add runtime tracker
class mouseLogger:
    def __init__(self):
        global get_position
        from mouse import get_position
        global keyboard
        import keyboard as keyboard
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
        print('Press"a" to log screenshot coordinates')
        self.logger = mouseLogger()
        self.logger.start()
        self.cords[0], self.cords[1], self.cords[2], self.cords[3]= self.logger.cords[0][0], self.logger.cords[0][1], self.logger.cords[1][0] - self.logger.cords[0][0], self.logger.cords[1][1] - self.logger.cords[0][1]
        print(f'Read Parameters-- Xpos: {self.cords[0]}| Ypos: {self.cords[1]}| Width: {self.cords[2]}| Height: {self.cords[3]}|')
    def shoot(self):
        self.screenshot = pyautogui.screenshot(region=(self.cords[0], self.cords[1], self.cords[2], self.cords[3]))
        self.screenshot.save(screenShotName)


#primary reader
class recogEasyOCR:
    def __init__(self):
        global easyocr
        import easyocr
        self.reader = easyocr.Reader(['en'])
    def read(self):
        self.result = self.reader.readtext(screenShotName, detail=0)
        self.fullText = '\n'.join(map(str, self.result))
        print(self.result)
        print(self.fullText)
        #for i in self.result: self.fullText + i
        #print(self.fullText)
#secondary reader, used if easyOCR isnt available
class recogKeras:
    def __init__(self, mDetect='craft', mRecog='vgg', download=True): 
        import cv2
        global plt
        import matplotlib.pyplot as plt
        import keras_ocr
        self.pipeline = keras_ocr.pipeline.Pipeline(detector=mDetect, recognizer=mRecog)
        
    def read(self):
        self.img = plt.imread(screenShotName)
        self.prediction_groups = self.pipeline.recognize([self.img])
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.imshow(self.img)
        self.pipeline.draw_annotation(ax, self.prediction_groups[0])
        plt.show()
        recognized_text = [text for _, text in self.prediction_groups[0]]
        print(recognized_text)
        '''
        self.img = keras_ocr.tools.read(screenShotName)
        #image = cv2.resize(image, (800, 800))
        self.prediction_groups = self.pipeline.recognize([image])
        self.extracted = []
        for predictions in self.prediction_groups:
            for textResult in predictions:
                text = textResult[0]
                extracted.append(text)
        resultSTR = '\n'.join(extracted)
        return resultSTR
        '''

def extractFromSceen():
    d = Debug.debug()
    scr = screenshot()
    scr.logCords()
    scr.shoot()    
    reader = recogEasyOCR()
    reader.read()

def main():
    from ImportTree import importDependencies
    global Debug
    import Debug
    #check dependancyes and install
    #importDependencies(dependencies)
    exit = False
    while not exit:
        extractFromSceen()
        exit = True if input('Continue? (Yes/No): ').lower() == 'no' else False
    #reader = recogKeras()
    #print(reader.read()) #effnetb3 for efficientcy, try vgg
    


if __name__=='__main__':
    main()

#aaaaaaaaaaaaaaaaaaaaaaaaaaaa/aaaaaaaaaaaaaaaaaaaa