dna_rna_map = {
    "C": "G",
    "G": "C",
    "T": "A",
    "A": "U"
}

dna = input("DNA: ")
rna = "".join([dna_rna_map[x] for x in dna])

count = 0

i = 0
found = False 
while i < len(rna):
    if not found:
        if rna[i:i+3] == "AUG":
            found = True
            count += 1
            i += 3
        else:
            i += 1
    else:
        if rna[i: i+3] in ['UAA', "UGA", "UAG"]:
            break
        
        count += 1
        i += 3

print(f"{count} Amino acid(s)")