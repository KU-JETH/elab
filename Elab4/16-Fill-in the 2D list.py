x = int(input("Enter the number of rows or columns : "))

for i in range(x):
  
  n = []
  for j in range(i+1, x+i+1):
    n.append(str(j).rjust(2))
  
  print(" ".join(n))