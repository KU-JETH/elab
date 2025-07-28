direction = input("Direction to flip square (V/H): ")
size = int(input("Input size of square: "))

m = []
for _ in range(size):
  m.append(input().split())

if direction == "V":
  m = m[::-1]
elif direction == "H":
  for i, row in enumerate(m):
    m[i] = row[::-1]

print("After flip:")

for row in m:
  print(" ".join(row))