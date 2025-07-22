text = input("Enter text: ")
step = int(input("Enter step: "))

x = ""

for t in text:
    if not t.isalpha():
        x += t
        continue 
    
    c = ''
    
    if t.isalpha():
        if t.isupper():
            n = (ord(t) - ord("A") + step) % 26
            c = chr(n + ord("A"))
        else:
            n = (ord(t) - ord("a") + step) % 26
            c = chr(n + ord("a"))
    
    x += c
    
    
print(x)
