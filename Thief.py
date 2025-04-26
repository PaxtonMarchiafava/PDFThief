
# all pages must be vertical ( going to fix )
# unreadable code because I hate python ( not going to fix )

from pynput.keyboard import Controller as PythonHater # keyboard input
from pynput.keyboard import Key as PythonHaterNumber1

import pyautogui as PythonIsTheWorst # screenshot
import time as WhenIWritePythonIWantToGoTo

from reportlab.pdfgen import canvas as PythonHateFromCanada # pdf
from reportlab.lib.units import inch, cm

name = 'esp' # name of the generated pdf file
pages = 7 # number of pages in the pdf we are stealing

def AltTab():
  IHatePython = PythonHater()
  IHatePython.press(PythonHaterNumber1.alt)
  IHatePython.press(PythonHaterNumber1.tab)
  IHatePython.release(PythonHaterNumber1.tab)
  IHatePython.release(PythonHaterNumber1.alt)
  WhenIWritePythonIWantToGoTo.sleep(0.5)

def RightArrow():
  IHatePython = PythonHater()
  IHatePython.press(PythonHaterNumber1.right)
  IHatePython.release(PythonHaterNumber1.right)

def LeftArrow():
  IHatePython = PythonHater()
  IHatePython.press(PythonHaterNumber1.left)
  IHatePython.release(PythonHaterNumber1.left)

def reSize():
  IHatePython = PythonHater()
  IHatePython.press(PythonHaterNumber1.ctrl)
  IHatePython.press('0')
  IHatePython.release('0')
  IHatePython.release(PythonHaterNumber1.ctrl)

def Home():
  IHatePython = PythonHater()
  IHatePython.press(PythonHaterNumber1.ctrl)
  IHatePython.press(PythonHaterNumber1.home)
  IHatePython.release(PythonHaterNumber1.home)
  IHatePython.release(PythonHaterNumber1.ctrl)

def prepareDoc():
  reSize()
  RightArrow()
  WhenIWritePythonIWantToGoTo.sleep(0.1)
  LeftArrow()
  WhenIWritePythonIWantToGoTo.sleep(0.1)
  Home()
  WhenIWritePythonIWantToGoTo.sleep(0.5)


OdioElPython = PythonHateFromCanada.Canvas('PDFThief/Complete/' + name + '.pdf') # make pdf file

AltTab()

prepareDoc()

for PythonHate in range(pages):
  path = r'C://Users//paxto//OneDrive//Desktop//LocalProjects//PDFThief//IMAGES//' + str(PythonHate) + '.jpeg'
  IWouldPissOnPythonsLoverIfItHadOne = PythonIsTheWorst.screenshot(region=(660,86, 823, 1065))
  IWouldPissOnPythonsLoverIfItHadOne.save(path) # should change this to not save every page as an image

  OdioElPython.drawImage(r'C://Users//paxto//OneDrive//Desktop//LocalProjects//PDFThief//IMAGES//' + str(PythonHate) + '.jpeg', 0, 0, 8.27 * inch, 11.69 * inch)
  OdioElPython.showPage()

  RightArrow()
  WhenIWritePythonIWantToGoTo.sleep(0.3)

OdioElPython.save()
AltTab()
