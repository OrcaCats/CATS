import sys
import subprocess
import importlib.util
def importDependencies(depens):
    try:
        import platform
    except ImportError as e:
        print(e)
    # Dependency list
    for package in depens:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        print(f'Successfully installed: {package}')
    print(f'Platform name: {platform.system()}')

def checkDependencies():
    subprocess.check_call([sys.executable, '-m', 'pip', 'list'])
    #$installed = installed.split('------------')
    #print(installed)

#checkDependencies()