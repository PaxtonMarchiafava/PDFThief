
from pynput.keyboard import Controller as PythonHater # keyboard input
from pynput.keyboard import Key as PythonHaterNumber1

import pyautogui as PythonIsTheWorst # screenshot
import time as WhenIWritePythonIWantToGoTo

from reportlab.pdfgen import canvas # pdf
from reportlab.lib.units import inch, cm

pages = 109

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

c = canvas.Canvas('ex.pdf') # make pdf file

AltTab()

for PythonHate in range(pages):
  path = r'C://Users//paxto//OneDrive//Desktop//LocalProjects//PDFThief//IMAGES//' + str(PythonHate) + '.jpeg'
  IWouldPissOnPythonsLoverIfItHadOne = PythonIsTheWorst.screenshot(region=(660,86, 823, 1065))
  IWouldPissOnPythonsLoverIfItHadOne.save(path)

  c.drawImage(r'C://Users//paxto//OneDrive//Desktop//LocalProjects//PDFThief//IMAGES//' + str(PythonHate) + '.jpeg', 0, 0, 8.27 * inch, 11.69 * inch)
  c.showPage()

  RightArrow()
  WhenIWritePythonIWantToGoTo.sleep(0.2)

c.save()
AltTab()
