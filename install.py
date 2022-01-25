import sys
import subprocess

def __init__():
    try:
        import selenium
        import PyQt5
    except:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'selenium'])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pyqt5'])
        return False
    return True
    
