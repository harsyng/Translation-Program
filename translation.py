# Codon to Amino Acid mapping dictionary
codon_table = {
    'ATA': 'Ile', 'ATC': 'Ile', 'ATT': 'Ile', 'ATG': 'Met',
    'ACA': 'Thr', 'ACC': 'Thr', 'ACG': 'Thr', 'ACT': 'Thr',
    'AAC': 'Asn', 'AAT': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
    'AGC': 'Ser', 'AGT': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
    'CTA': 'Leu', 'CTC': 'Leu', 'CTG': 'Leu', 'CTT': 'Leu',
    'CCA': 'Pro', 'CCC': 'Pro', 'CCG': 'Pro', 'CCT': 'Pro',
    'CAC': 'His', 'CAT': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
    'CGA': 'Arg', 'CGC': 'Arg', 'CGG': 'Arg', 'CGT': 'Arg',
    'GTA': 'Val', 'GTC': 'Val', 'GTG': 'Val', 'GTT': 'Val',
    'GCA': 'Ala', 'GCC': 'Ala', 'GCG': 'Ala', 'GCT': 'Ala',
    'GAC': 'Asp', 'GAT': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
    'GGA': 'Gly', 'GGC': 'Gly', 'GGG': 'Gly', 'GGT': 'Gly',
    'TCA': 'Ser', 'TCC': 'Ser', 'TCG': 'Ser', 'TCT': 'Ser',
    'TTC': 'Phe', 'TTT': 'Phe', 'TTA': 'Leu', 'TTG': 'Leu',
    'TAC': 'Tyr', 'TAT': 'Tyr', 'TAA': 'Stop', 'TAG': 'Stop',
    'TGC': 'Cys', 'TGT': 'Cys', 'TGA': 'Stop', 'TGG': 'Trp',
}

def translate_dna_sequence(dna_sequence):
    proteins = []
    dna_sequence = dna_sequence.upper()
    reversed_dna_sequence = dna_sequence[::-1]

    # Forward reading frames
    for frame in range(3):
        protein = ''
        for i in range(frame, len(dna_sequence), 3):
            codon = dna_sequence[i:i+3]
            if codon in codon_table:
                amino_acid = codon_table[codon]
                if amino_acid == 'Stop':
                    break
                protein += amino_acid + '-'
        proteins.append(protein.rstrip('-'))

    # Reverse reading frames
    for frame in range(3):
        protein = ''
        for i in range(frame, len(reversed_dna_sequence), 3):
            codon = reversed_dna_sequence[i:i+3]
            if codon in codon_table:
                amino_acid = codon_table[codon]
                if amino_acid == 'Stop':
                    break
                protein += amino_acid + '-'
        proteins.append(protein.rstrip('-'))

    return proteins


# Ask the user for DNA sequence input
dna_sequence = input("Enter the DNA sequence: ")

# Translate the DNA sequence into protein products
protein_products = translate_dna_sequence(dna_sequence)

# Print the protein products in all 6 frames
print("In the first reading frame (after appropriate deletion) the protein is read as :", protein_products[0])
print("In the second reading frame (after appropriate deletion) the protein is read as :", protein_products[1])
print("In the third reading frame (after appropriate deletion) the protein is read as :", protein_products[2])
print("In the fourth reading frame (after appropriate deletion) the protein is read as :", protein_products[3])
print("In the fifth reading frame (after appropriate deletion) the protein is read as :", protein_products[4])
print("In the sixth reading frame (after appropriate deletion) the protein is read as :", protein_products[5])
