ls = list(map(int, input().split()))

while True:
  x, y = map(int, input().split())
  
  # -x + len(ls) => last element x th
  if x < 0:
    x += len(ls)
  if y < 0:
    y += len(ls)
  
  if (x >= len(ls) or x < 0) and (y >= len(ls) or y < 0):
    print("x and y Bad Input")
    continue
  if x >= len(ls) or x < 0:
    print("x Bad Input")
    continue
  if y >= len(ls) or y < 0:
    print("y Bad Input")
    continue
  
  if x > y:
    break
  
  print(sum(ls[x:y+1]))