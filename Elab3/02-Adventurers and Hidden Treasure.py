password = input("ป้อนรหัสลับ: ")

total = 0
i = 0
while i < len(password):
    if not password[i].isdigit():
        i += 1
        continue
    
    x = password[i]
    i += 1
    while i < len(password) and password[i].isdigit():
        x += password[i]
        i += 1
    
    total += int(x)
        
print("ผลลัพธ์:", total)