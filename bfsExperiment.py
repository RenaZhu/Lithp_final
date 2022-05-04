import numpy as np
from random import randint
import cv2 as cv
import time

for i in range(100):
  start_time = time.time()
  img = np.matrix(cv.imread("Brewery.png",cv.IMREAD_GRAYSCALE))
  img[img<255] = 0

  start = (600, 700)
  goal = (50,100)


  grid = img

  w, h = img.shape[:2]
  XRange = range(w)
  YRange = range(h)

  # BFS Section
  grid[start] = 1
  path=[]
  q=[start]
  while q:
    x,y = q.pop(0)
    path.append((x,y))
    dir = [[0,20],[20,0],[0,-20],[-20,0]]
    for dx,dy in dir:
      if x+dx in XRange and y+dy in YRange and grid[x+dx,y+dy]!= 1 and grid[x+dx,y+dy]!= 0:
          q.append((x+dx,y+dy))
          if (x+dx,y+dy) == goal:
            q=[]
            path.append((x+dx,y+dy))
            break
          grid[x+dx,y+dy] = 1
  print("--- %s seconds ---" % (time.time() - start_time))