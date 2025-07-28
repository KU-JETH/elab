def is_complete(string):
  counter = []
  
  for c in string:
    if not c.isalpha():
      continue
    
    c = c.lower()
    if c not in counter:
      counter.append(c)
  
  if len(counter) == 26:
    return True
  else:
    return False

ls1 = eval(input("String set1: "))
ls2 = eval(input("String set2: "))

res = []

for a in ls1:
  for b in ls2:
    s = a+b
    if is_complete(s):
      res.append(s)

print(f"Output: {len(res)}")
print("The total complete pairs that are forming are:")
for r in res:
  print("", r)