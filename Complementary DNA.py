def DNA_strand(dna):
    # code here
    dic = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    dna_side = ''
    for i in dna:
        dna_side += dic[i]

    return dna_side

dna = input("Enter DNA")
print(DNA_strand(dna))