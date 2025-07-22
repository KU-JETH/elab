file = input("File name: ")
data = open(file).read().splitlines()
data = [[int(n) if n.isdigit() else n for n in row.split()] for row in data]

table = {}

for row in data:
    name = row[0]
    score = 0
    row = sorted(row[1:], reverse=True)[1:-1]
    for s in row:
        score += s
    
    if score in table.keys():
        table[score].append(name)
    else:
        table[score] = [name]

table = sorted(table.items(), key=lambda x: x[0], reverse=True)

top_score, top_students = table[0]
print(top_score)

for student in top_students:
    print(student)