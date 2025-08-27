money = int(input("Input amount : "))

banks = [1000, 500, 100, 50, 20]
coins = [10, 5, 2, 1]

for v in banks:
  bank = BankNote(v)
  amount = money // bank.value
  money -= bank.value * amount
  if amount: print(f"You get {amount} of {bank}")
  
for v in coins:
  coin = Coin(v)
  amount = money // coin.value
  money -= coin.value * amount
  if amount: print(f"You get {amount} of {coin}")