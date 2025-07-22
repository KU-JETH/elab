def is_chain(prev_word, word):
    count = 0
    
    for a, b in zip(prev_word, word):
        if a != b:
            count += 1
            if count >= 3:
                return False
    
    return True 

words = input("Text: ").split()

chain = 0
max_length = 0
prev_word = ''

current_chain = []

for word in words:
    if not prev_word:
        current_chain = [word]
        prev_word = word
        chain += 1
        continue
    
    if is_chain(prev_word, word):
        current_chain.append(word)
    else:
        if len(current_chain) > max_length:
            max_length = len(current_chain)
        
        chain += 1
        current_chain = [word]
    
    prev_word = word

if current_chain:
    if len(current_chain) > max_length:
        max_length = len(current_chain)

print(f"{chain} Chain(s). Maximum length is {max_length} word(s).")
