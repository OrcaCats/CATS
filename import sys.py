#dependancy import
import sys
import subprocess
def installPack(depens):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', depens])
#dependancy list
dependancies = ['keras-ocr']
#print(installPack(dependancies))
for pack in dependancies:
    installPack(pack)
#------------------------------------------------------------------------------------
