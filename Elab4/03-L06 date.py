def is_leap_year(year) -> bool:
    if year % 400 == 0 or (year % 4 == 0 and y % 100 != 0):
        return True
    return False

d = int(input("d: "))
m = int(input("m: "))
y = int(input("y: "))

days = 0
for i in range(1, m):
    if i in [1, 3, 5, 7, 8, 10, 12]:
        days += 31
    elif i == 2:
        if is_leap_year(y):
            days += 29
        else:
            days += 28
    else:
        days += 30

days += d

print(days)