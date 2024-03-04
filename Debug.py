#dbg_Counter = 0
#debugStep = 10
#def debug(text, pointer=''):
#    global dbg_Counter
#    dbg_Counter +=1
#    return_LineCount = dbg_Counter % debugStep
#    if pointer == 'Y':
#        print(text + str(return_LineCount)) if return_LineCount else print(text)
#    else:
#        return_LineCount = dbg_Counter % debugStep
#        None if return_LineCount else print('Pass ' + str(dbg_Counter))


# Dear Traveler, I wish that this finds you well on your programming and debugging journey. 
# While you're here, may the electroBuddha bless you with infinitely optimizes runtimes and easy-to-spot bugs.
# Sincere appriciation for dropping by and checking out the code, 
# Godspeed, traveler!
#
#--Tensor6 (Micah)
#                           _
#                        _ooOoo_
#                       o8888888o
#                       88" . "88
#                       (| -_- |)
#                       O\  =  /O
#                    ____/`---'\____
#                  .'  \\|     |//  `.
#                 /  \\|||  :  |||//  \
#                /  _||||| -:- |||||_  \
#                |   | \\\  -  /'| |   |
#                | \_|  `\`---'//  |_/ |
#                \  .-\__ `-. -'__/-.  /
#              ___`. .'  /--.--\  `. .'___
#           ."" '<  `.___\_<|>_/___.' _> \"".
#          | | :  `- \`. ;`. _/; .'/ /  .' ; |
#          \  \ `-.   \_\_`. _.'_/_/  -' _.' /
#===========`-.`___`-.__\ \___  /__.-'_.'_.-'================
#                        `=--=-'                    







class debug:
    def __init__(self, debugStep=1):
        self.debugStep = debugStep
        self.dbg_Counter = 0

    def debug(self, text, pointer=''):
        self.dbg_Counter +=1
        self.return_LineCount = self.dbg_Counter % self.debugStep
        if pointer == 'Y':
            print(f'value: |{text}| at counter: |{str(self.dbg_Counter)}|') if self.return_LineCount == 0 else print(text)
        else:
            print('Pass ' + str(self.dbg_Counter))