
# if a page is horizontal, it is stretched and saved as vertical ( going to fix )
# unreadable code because I hate python ( not going to fix )
# makes the assumption that the page is white and does not have a crazy aspect ratio ( not going to fix )

import time as WhenIWritePythonIWantToGoTo
import math as PantsToThe

from pynput.keyboard import Controller as PythonHater # keyboard input
from pynput.keyboard import Key as PythonHaterNumber1

import pyautogui as PythonIsTheWorst # screenshot

from reportlab.pdfgen import canvas as PythonHateFromCanada # pdf
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch, cm

import ctypes # get screen size
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

name = 'esp' # name of the generated pdf file
pages = 18 # number of pages in the pdf we are stealing

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
  Home()
  WhenIWritePythonIWantToGoTo.sleep(0.5)

def sum(s):
  sum = 0
  for i in s:
    sum += i
  return sum

def GetPageDimensions(page):
  x, y, w, l = 0, 0, screensize[0] - 100, screensize[1]

  flag = 0
  while (flag < ((screensize[1] / 2) * 0.5)): # find left x coordinate of the page
    flag = 0
    for i in range(PantsToThe.floor(screensize[1] / 2)):
      if sum(page.getpixel((x, i * 2))) < sum(page.getpixel((x + 1, i * 2 ))):
        flag += 1
    x += 1
    
    if x > (screensize[0] / 2):
      print('no left side edge found')
      x = 0
      break


  flag = 0
  while (flag < ((screensize[1] / 2) * 0.5)): # find right x coordinate of the page
    flag = 0
    for i in range(PantsToThe.floor(screensize[1] / 2)):
      if (sum(page.getpixel((w, i * 2))) < sum(page.getpixel((w - 1, i * 2 )))) and (sum(page.getpixel((w - 1, i * 2 ))) > 245 * 3):
        flag += 1
    w -= 1

    if w < (screensize[0] / 2):
      print('no right side edge found')
      w = screensize[0] - x
      break
  w = w - x # width of page expected. This converts far right coordiante to width of page


  flag = 0
  while (flag < ((screensize[0] / 2) * 0.33)): # find top y coordinate of the page
    flag = 0
    for i in range(PantsToThe.floor(screensize[0] / 2)):
      if (sum(page.getpixel((i * 2, y))) < sum(page.getpixel((i * 2, y + 1)))) and (sum(page.getpixel((i * 2, y + 1))) > 245 * 3):
        flag += 1
    y += 1
    
    if y > (screensize[1] / 2):
      print('no top side edge found')
      y = 0
      break


  flag = 0
  l = y + 300
  while (flag < 28):
    flag = 0
    for i in range(15):
      if sum(page.getpixel((x + i, l))) > sum(page.getpixel((x + i, l + 1))): # left side
        flag += 1
      if sum(page.getpixel((w - i, l))) > sum(page.getpixel((w - i, l + 1))): # right side
        flag += 1
      if (flag < ((i * 2) - 2)): # early break condition
        break
    l += 1
  l -= y

  # print('dimensions:', x, y, w, l)
  return (x, y, w, l)



OdioElPython = PythonHateFromCanada.Canvas('PDFThief/Complete/' + name + '.pdf') # make pdf file

AltTab()

prepareDoc()

for PythonHate in range(pages):
  path = r'C://Users//paxto//OneDrive//Desktop//LocalProjects//PDFThief//IMAGES//' + str(PythonHate) + '.png'
  IWouldPissOnPythonsLoverIfItHadOne = PythonIsTheWorst.screenshot()

  x, y, w, l = GetPageDimensions(IWouldPissOnPythonsLoverIfItHadOne)
  IWouldPissOnPythonsLoverIfItHadOne = PythonIsTheWorst.screenshot(region=(x, y, w, l))
  
  IWouldPissOnPythonsLoverIfItHadOne.save(path) # should change this to not save every page as an image
  
  if w < l: # if horizontal
    OdioElPython.setPageSize((8.27 * inch, 11.69 * inch))
    OdioElPython.drawImage(path, 0, 0, 8.27 * inch, 11.69 * inch) # change to path
  else:
    OdioElPython.setPageSize((11.69 * inch, 8.27 * inch))
    OdioElPython.drawImage(path, 0, 0, 11.69 * inch, 8.27 * inch) # change to path

  OdioElPython.showPage()

  RightArrow()
  WhenIWritePythonIWantToGoTo.sleep(0.05) # doesn't work without this

OdioElPython.save()
AltTab()
