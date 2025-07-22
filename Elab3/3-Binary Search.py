ls = [int(n) for n in input("ข้อมูล: ").split(', ')]
target = int(input("ค่าที่ต้องการหา: "))

s = 0
e = len(ls) - 1

count = 0

while s <= e:
    count += 1
    mid = (e - s) // 2 + s
    
    if ls[mid] == target:
        break
    elif ls[mid] > target:
        e = mid - 1
    elif ls[mid] < target:
        s = mid + 1
print("จำนวนครั้งที่ค้นหา:", count)