from utils.pip_install import install_pip
import os

os.chdir(os.pardir)
liste = list()
liste.append(os.getcwd())
liste.append("requirements.txt")
dizin = os.sep.join(liste)

with open(dizin,"r") as dosya:
   for satir in dosya:
        install_pip(satir.rstrip("/n"))
        
from main import *
