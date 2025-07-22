text = input("Text: ")
substring = input("Substring: ")

i = 0
x = ""

while i < len(text):
    
    if text[i] == substring[0]:
        if text[i:i + len(substring)] == substring:
            x += f"[{substring}]"
            i += len(substring)
            continue
    
    x += text[i]
    i += 1

if "[" in x:
    print(x)
else:
    print("Not found")
