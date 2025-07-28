mylist = list(map(int,input().split()))

while True:
    menu, x = input().split()
    x = int(x)

    if menu == "A":
        mylist.append(x)
    elif menu == "S":
        print(mylist[x])
    elif menu == "R":
        mylist.pop(x)
    elif menu == "E" and x == 0:
        break

if mylist:
    print(" ".join(list(map(str, mylist))))