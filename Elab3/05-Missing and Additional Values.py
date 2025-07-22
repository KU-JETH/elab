ls1 = eval(input("Input list1: "))
ls2 = eval(input("Input list2: "))

x1 = [e for e in ls1 if e not in ls2]
x2 = [e for e in ls2 if e not in ls1]

print("Missing values in list1 =", x2)
print("Additional values in list1 =", x1)
print("Missing values in list2 =", x1)
print("Additional values in list2 =", x2)