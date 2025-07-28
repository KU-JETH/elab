# Can use list instead of dict 
counter = {1: 0, 2: 0, 3: 0}

car = 0

ls = list(map(int, input().split()))

# 4
for x in ls:
  if x == 4:
    car += 1
  else:
    counter[x] += 1

# 2-2
pair_count = counter.get(2) // 2
counter[2] -= pair_count * 2
car += pair_count

# 2-1
while counter[2] >= 1 and counter[1] >= 2:
  car += 1
  counter[2] -= 1
  counter[1] -= 2

# 3-1
while counter[3] >= 1 and counter[1] >= 1:
  car += 1
  counter[3] -= 1
  counter[1] -= 1


# When there is no 1 but remain 2 and 3
car += counter[2]
car += counter[3]

# When there is only 1 left
if counter[1] > 0:
  car += counter[1] // 4
  if counter[1] % 4 != 0:
    car += 1

print(car)