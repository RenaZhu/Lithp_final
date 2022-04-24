import numpy as np
from random import randint
import cv2 as cv


img = np.matrix(cv.imread("MAP.png",cv.IMREAD_GRAYSCALE))
img[img<255] = 0

start = (735, 842)
goal = (260,814)


grid = img

h, w = img.shape[:2]


# Create matrix section
# with open("Matrix.txt","w") as f:
#   for line in img:
#     for el in np.nditer(line):
#       f.write(f"{el} ")
#     f.write('\n')

# BFS Section
grid[start] = 1
path=[]
q=[start]
f = open("log.txt", "w")
while q:
  x,y = q.pop(0)
  path.append((x,y))
  dir = [[0,1],[1,0],[0,-1],[-1,0]]
  for dx,dy in dir:
    if grid[x+dx,y+dy]!= 1 and grid[x+dx,y+dy]!= 0:
        f.write(f"{len(path)},{(x,y)}")
        q.append((x+dx,y+dy))
        if (x+dx,y+dy) == goal:
          q=[]
          path.append((x+dx,y+dy))
          break
        grid[x+dx,y+dy] = 1
f.close()
  
f = open("path.txt", "w")
f.write(f"{path}")
f.close()