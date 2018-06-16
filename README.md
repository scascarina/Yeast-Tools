# Yeast-Tools
Repository containing yeast-specific tools and scripts  

## Reverse_translate.py
A script that accepts a file containing amino acid sequences (1 per line) in a plain text file and converts them to DNA sequences with each amino acid converted to its most common codon in the yeast translatome.

#### Usage:
From command line, type:  _python Reverse_translate.py [name of your protein sequence file]_.  
Example:  python Reverse_translate.py 'Sup35 protein sequence.txt'

## yeast_gene_name_conversion.py
A script that accepts a file containing a list of yeast genes (either as ORF names or common yeast gene names, with on 1 gene per line) in a plain text file and converts them to the common gene name or ORF name respectively. Most lists of gene names pasted directly into a plain text editor will result in one gene per line. Simply save the file and run the yeast_gene_name_conversion.py script to convert the gene names.  
A WORD OF CAUTION: in rare cases, the common name for a yeast gene is also an alias for a different gene. 

#### Usage:
From command line, type:  _python yeast_gene_name_conversion.py [name of your protein list file]_.  
Example:  python yeast_gene_name_conversion.py 'Transcription Factor Genes.txt'
