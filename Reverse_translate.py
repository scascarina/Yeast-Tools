
optimal_codons = {'A' : 'GCT', 'C' : 'TGT', 'D' : 'GAT', 'E' : 'GAA', 'F' : 'TTT',
                'G' : 'GGT', 'H': 'CAT', 'I' : 'ATT', 'K': 'AAA', 'L' : 'TTG',
                'M' : 'ATG', 'N' : 'AAT', 'P' : 'CCA', 'Q' : 'CAA', 'R' : 'AGA',
                'S' : 'TCT', 'T' : 'ACT', 'V' : 'GTT', 'W' : 'TGG', 'Y' : 'TAT'}

def rev_translate(input_file):
    
    h = open(input_file)
    
    dna = ''
    
    for line in h:
        line = line.rstrip()
        for amino_acid in line:
            if amino_acid in optimal_codons:
                dna += optimal_codons[amino_acid]
            else:
                dna += 'nnn'
            
    output_name = input_file[:-4] + '_rev_translated.txt'
    output = open(output_name, 'w')
    output.write(dna)
    
if __name__ == '__main__':
    rev_translate('Nterm Scramble4.txt')