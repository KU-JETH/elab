x = input("Enter your sentence: ").split()

table = {}
for word in x:
    c = word[0].lower()
    
    if c in table.keys():
        old = table[c]
        if len(word) > len(old):
            table[c] = word
    else:
        table[c] = word

for c, word in table.items():
    print(f"{c.upper()}: {word}")