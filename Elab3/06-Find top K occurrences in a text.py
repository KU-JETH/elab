### มีมาให้เเล้ว
def getMultilinesInput():
    text = ""
    while True:
        line = input()
        if not line:
            break
        text += line + ' '
    return text
###

print("Parse a long paragraph (or text) below, following an ENTER as needed:")
texts = getMultilinesInput().split()

counter = {}
for t in texts:
    counter[t.lower()] = 1 + counter.get(t.lower(), 0)

k = int(input("Top K rank: "))

counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)

freq_dict = {} # dict list

for word, count in counter:
    if count in freq_dict.keys():
        freq_dict[count].append(word)
    else:
        freq_dict[count] = [word]

for count, words in list(freq_dict.items())[:k]:
    x = []
    for w in words:
        x.append(f"{w}: {count}")
    
    print(", ".join(x))