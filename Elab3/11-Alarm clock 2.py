def print_time():
    global hours, mins
    print(f"{str(hours).rjust(2, '0')}:{str(mins).rjust(2, '0')}")

def add_time():
    global hours, mins
    
    mins += 1
    
    if mins >= 60:
        mins -= 60
        hours += 1
        if hours >= 24:
            hours -= 24
    
    return hours, mins

hours, mins = [int(x) for x in input("Input current time: ").split(':')]
nap = int(input("Input nap time: "))
snooze = int(input("Input snooze time: "))

print("Nap time starts.")
for _ in range(nap):
    hours, mins = add_time()
    print_time()

while True:
    x = input("Alarm rings. Dismiss or Snooze: ")
    
    if x == "Dismiss":
        break
    
    if x == "Snooze":
        for _ in range(snooze):
            add_time()
            print_time()
