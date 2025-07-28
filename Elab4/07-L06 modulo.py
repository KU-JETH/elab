res = []

n = int(input("N: "))
m = int(input("M: "))

for i in range(n):
  x = int(input(f"Input number {i+1}: "))
  y = x % m
  
  if y not in res:
    res.append(y)
  
print(len(res))