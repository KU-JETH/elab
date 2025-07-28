num = input("Enter lucky number : ")
n = int(input("Enter amount of candidates : "))

winner = ""
max_count = 0

for i in range(n):
  myid = input(f"Enter ID card number {i+1}: ")
  count = 0
  for c in myid:
    if c == num:
      count += 1
  
  if count > max_count:
    max_count = count
    winner = myid
  elif count == max_count:
    if sum(list(map(int, myid))) > sum(list(map(int, winner))):
      winner = myid

print("Winner:", winner)