x = int(input("Input number of words: "))

counter = {}

for _ in range(x):
    word = input()
    
    if word[0] in counter.keys():
        counter[word[0]].append(word)
    else:
        counter[word[0]] = [word]

counter = sorted(counter.items(), key=lambda x: len(x[1]))
pop_char, words = counter[-1]

print(f"The popular character is {pop_char}.")
print(f"The character is used in {len(words)} words.")
for w in words:
    print(w)