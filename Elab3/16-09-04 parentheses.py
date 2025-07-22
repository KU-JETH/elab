paren_map = {
    ")" : "(",
    "}" : "{",
    "]" : "["
}

stack = []
x = input("input: ")

for c in x:
    if c in paren_map.keys():
        x = stack.pop(-1)
        if x != paren_map[c]:
            print('invalid parentheses')
            break
    elif c in paren_map.values():
        stack.append(c)
    
else:
    if stack:
        print('invalid parentheses')
    else:
        print("valid parentheses")