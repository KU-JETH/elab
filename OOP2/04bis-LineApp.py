from 

# โค้ด
x1  = int(input("Enter x1 : "))
y1  = int(input("Enter y1 : "))
x2  = int(input("Enter x2 : "))
y2  = int(input("Enter y2 : "))

print(f"value of x1 on this line is {x1:.3f}")
print(f"value of x2 on this line is {x2:.3f}")
print(f"value of y1 on this line is {y1:.3f}")
print(f"value of y2 on this line is {y2:.3f}")

line = Line(x1, y1, x2, y2)

print("==========")
print("Check x and y are on this line ?")
x  = int(input("Enter x : "))
y  = int(input("Enter y : "))

is_contain = line.contains(x, y)
print(f"x = {x:.3f} and y = {y:.3f} are{'' if is_contain else ' not'} on this line")
print(f"Distance between startPoint and endPoint is {line.get_distance():.3f}")
print("==========")

print("Find value of y that gives( x , y ) on this line")
x  = int(input("Enter x : "))
y = line.get_y(x)
print(f"value of y is {y:.3f}")
is_contain = line.contains(x, y)
print(f"( x , y ) = ( {x:.3f} , {y:.3f} ){'' if is_contain else ' is not'} on this line")