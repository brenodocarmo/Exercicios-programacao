def proteins(strand):
    fat = 3
    list_proteins = [strand[ind: ind + 3] for ind in range(0, len(strand), fat)]
    
    protein_codon = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP", 
        "UGA": "STOP",
    }

    result = []

    for codo in list_proteins:
        veri = protein_codon[codo]
        if veri == "STOP":
            break
        else:
            result.append(veri)

    return result
