# http://www.crazygames.com/game/white-tile-2-don-t-tap-it
import numpy as np
import cv2 as cv
import win32api, win32con
from PIL import ImageGrab

# Viewport = 360x360 (approx)
co_ords=[]
def test_coords():
	'''
	Draw the points on a blank canvas
	Save the points to "co_ords"
	'''
	# blank = np.zeros((360, 360), dtype='uint8')
	for i in range(45, 360, 90):
		for j in range(45 ,360, 90):
			co_ords.append((i,j))
	# 		cv.rectangle(blank, (i,j), (i+2,j+2), 255, -2)
	# cv.imshow("blank", blank)
	# cv.waitKey(0)

test_coords()

def click(x,y,last_click):
	if((x,y)==last_click): return
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

last_click = (-1, -1)
while(1):
	img = ImageGrab.grab(bbox=(640, 300, 640+360, 300+360)) # Take a screenshot
	img_np = np.array(img)
	frame = cv.cvtColor(img_np, cv.COLOR_BGR2GRAY)
	for (i, j) in co_ords:
		if(frame[i, j])==0:
			click(640+j-180, 300+i-90, last_click)
			last_click = (640+j-180, 300+i-90)
			cv.waitKey(70)
	# cv.imshow("frame", frame)
