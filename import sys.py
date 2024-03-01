#dependancy import
import sys
import subprocess

def installPack(depens):
    for i, j in enumerate(depens):
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', j])
        return f'installed {i+1} packages'
#dependancy list
dependancies = ['torch']
print(installPack(dependancies))
#------------------------------------------------------------------------------------

#