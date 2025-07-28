n = int(input())
print('.'*n)
center = n // 2 + 1

for i in range(1, center):
  x = "."
  space = " " * (i - 1)
  
  if i == center - 1:
    x += space + "." + space
  else:
    bigspace = (n-2-(i*2)) * " "
    x += space + "." + bigspace + "." + space
  
  x += "."
  print(x)

for i in range(center-1, 1, -1):
  x = "."
  space = " " * (i-2)
  bigspace = (n-(i*2)) * " "
  
  x += space + "." + bigspace + "." + space
  x += "."
  
  print(x)

print('.'*n)