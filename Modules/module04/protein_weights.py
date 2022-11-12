"""Module to show how to sort a dictionary that has a tuple for it values"""


def main():
    """Business Logic"""
    aa_values = get_amino_acid_dict()
    # print out the values
    _ = [print(key, value) for key, value in aa_values.items()]
    print("\n\n")


    # sort the dictionary by the weight of the amino acid.  When you have a list or a tuple
    # you have to use lambda to be nice an concise, b/c here you can print by the 3 index
    for key in sorted(aa_values.keys(), key=lambda x: aa_values[x][3], reverse=True):
        print(key, aa_values[key])


def get_protein_weights():
    """
    Return the Molecular weight of the amino acids
    @return: Dictionary of weights
    Data from:
    https://github.com/biopython/biopython/blob/master/Bio/Data/IUPACData.py
    """
    return {
        "A": 89.0932,
        "C": 121.1582,
        "D": 133.1027,
        "E": 147.1293,
        "F": 165.1891,
        "G": 75.0666,
        "H": 155.1546,
        "I": 131.1729,
        "K": 146.1876,
        "L": 131.1729,
        "M": 149.2113,
        "N": 132.1179,
        "P": 115.1305,
        "Q": 146.1445,
        "R": 174.201,
        "S": 105.0926,
        "T": 119.1192,
        "V": 117.1463,
        "W": 204.2252,
        "Y": 181.1885,
    }


def get_amino_acid_dict():
    """
    Return a Dictionary of amino acid data:
        Key = Single letter amino acid
        Value = Tuple(Single_letter, Three_letter, Name, Molecular Weight)
    Data from:
    http://aria.pasteur.fr/example-files/modified-residues/aria-files/AminoAcid.py/view
    @return: Dictionary of data
    """

    amino_acid = {
        'A': ('A', 'ALA', 'alanine'),
        'R': ('R', 'ARG', 'arginine'),
        'N': ('N', 'ASN', 'asparagine'),
        'D': ('D', 'ASP', 'aspartic acid'),
        'C': ('C', 'CYS', 'cysteine'),
        'Q': ('Q', 'GLN', 'glutamine'),
        'E': ('E', 'GLU', 'glutamic acid'),
        'G': ('G', 'GLY', 'glycine'),
        'H': ('H', 'HIS', 'histidine'),
        'I': ('I', 'ILE', 'isoleucine'),
        'L': ('L', 'LEU', 'leucine'),
        'K': ('K', 'LYS', 'lysine'),
        'M': ('M', 'MET', 'methionine'),
        'F': ('F', 'PHE', 'phenylalanine'),
        'P': ('P', 'PRO', 'proline'),
        'S': ('S', 'SER', 'serine'),
        'T': ('T', 'THR', 'threonine'),
        'W': ('W', 'TRP', 'tryptophan'),
        'Y': ('Y', 'TYR', 'tyrosine'),
        'V': ('V', 'VAL', 'valine'),
    }
    # get the weights
    weights = get_protein_weights()
    # go over and add the weights to the tuple.  You need to add a 1 element tuple
    return {key: value + (weights[key],) for key, value in amino_acid.items()}


if __name__ == '__main__':
    main()
