"""Simple comparison showing an alternative to the triple nested for loop"""
from itertools import product


def main():
    """Business Logic"""
    trinucleotides1 = trinucleotides_v1()
    trinucleotides2 = trinucleotides_v2()
    assert trinucleotides1 == trinucleotides2

def trinucleotides_v1(alphabet='AGCT'):
    """
    Count the trinucleotides in a string
    @param alphabet: What alphabet to use
    @return: Dict of trinucleotides
    """
    counts = {}
    for base1 in alphabet:
        for base2 in alphabet:
            for base3 in alphabet:
                trinucleotide = base1 + base2 + base3
                counts[trinucleotide] = 1
    return counts

def trinucleotides_v2(alphabet='AGCT'):
    """
    Count the trinucleotides in a string
    @param alphabet: What alphabet to use
    @return: Dict of trinucleotides
    """
    counts = {}
    for trinucleotide in (str.join("", nts) for nts in product(alphabet, alphabet, alphabet)):
        counts[trinucleotide] = 1
    return counts


if __name__ == '__main__':
    main()
