strings = input("Enter a string: ").split()

vowels = []
con = []

for s in strings:
    for c in s:
        if not c.isalpha():
          continue
      
        c = c.lower()
        if c in vowels or c in con:
            continue
        
        if c in ['a', 'e', 'i', 'o', 'u']:
            vowels.append(c)
        else:
            con.append(c)

print("Unique vowels: ", vowels)
print("Unique consonants: ", con)