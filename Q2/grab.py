# เเนะนำ counter นับว่าเเต่ละเลขมีกี่ตัว
counter = {}

inp = list(map(int, input().split()))
for n in inp:
  counter[n] = 1 + counter.get(n, 0)
counter = dict(sorted(counter.items(), key=lambda x: x[0], reverse=True))

max_p = int(input())

car = 0

# Using two pointer p1 and p2
for p1 in counter.keys():
  if not counter[p1]:
    continue
  
  while counter[p1]:
    current = p1
    counter[p1] -= 1
    p2 = p1
    
    while current < max_p and p2 > 0:
      if p2 not in counter.keys() or not counter[p2]:
        p2 -=1 
        continue
      
      if current + p2 <= max_p:
        current += p2
        counter[p2] -= 1
      else:
        p2 -= 1
    
    car += 1

print(car)