import numpy as np
from random import randint
n=5
grid = np.zeros((n,n),dtype=int)
print(grid)
goalVal = 10
Nrange=range(n)
for p in Nrange:
  grid[randint(0,n-1),randint(0,n-1)]=-1
grid[n-1,n-1] = goalVal
print(grid)

start = (0,0)
grid[start] = 1
path=[]
q=[start]
while q:
  x,y = q.pop(0)
  path.append((x,y))
  dir = [[0,1],[1,0],[0,-1],[-1,0]]
  for dx,dy in dir:
    if x+dx in Nrange and y+dy in Nrange and grid[x+dx,y+dy]!= 1 and grid[x+dx,y+dy]!= -1:
        q.append((x+dx,y+dy))
        if grid[x+dx,y+dy] == goalVal:
          q=[]
          path.append((x+dx,y+dy))
          break
        grid[x+dx,y+dy] = 1

  print(grid)
  
print(path)