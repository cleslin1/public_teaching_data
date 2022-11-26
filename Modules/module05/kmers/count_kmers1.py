"""Code to count DNA trinucleotides and then store them in a Dict and sort them out"""

from utils import generate_random_dna_str, print_trinucleotides


def main():
    """Simple function to call our other functions"""
    dna = generate_random_dna_str(20, 'ACGTNSW')  # get a randome dna sequence of 2000bp
    print(dna)
    quit()
    counts = count_trinucleotides(dna)
    print_trinucleotides(counts, threshold=1000)


def count_kmer(kmer, dna):
    '''
    Counts the number of times a substring mer occurs in the sequence dna (including overlapping occurrences)
    sample use: count_mer("GGG", "AGGGCGGG") => 2
    @param kmer: the k-mer to count
    @param dna: The sequence to explore for kmers
    '''

    kmer_len = len(kmer)
    count = 0
    for i in range(0, len(dna) - kmer_len + 1):
        if kmer == dna[i:i + kmer_len]:
            count = count + 1
    return count


def count_trinucleotides(dna, alphabet='AGCT'):
    """
    Count the trinucleotides in a string
    @param dna: DNA string to count
    @param alphabet: What alphabet to use
    @return: Dict of trinucleotides with the value being the number of times it was found in the DNA String
    """
    counts = {}
    dna = dna.replace(" ", "")
    for base1 in alphabet:
        for base2 in alphabet:
            for base3 in alphabet:
                trinucleotide = base1 + base2 + base3
                number = count_kmer(trinucleotide, dna)
                counts[trinucleotide] = number
    # remove all 0's
    counts = {key: value for key, value in counts.items() if value != 0}
    return counts


def test_code():
    """
    Simple test of the code
    @return: None
    """
    counts = count_trinucleotides("GATTACA")
    expected = {'GAT': 1, 'ATT': 1, 'TTA': 1, 'TAC': 1, 'ACA': 1}
    assert counts == expected


if __name__ == '__main__':
    main()
    test_code()


(BINF6200) cleslin@Chesleys-MacBook-Pro[kmers]$ python3 count_kmers1.py
TTTGGCATACTGACAGATAA
(BINF6200) cleslin@Chesleys-MacBook-Pro[kmers]$ python3 count_kmers1.py
AACGCTCTTACTCCCTGTGT
(BINF6200) cleslin@Chesleys-MacBook-Pro[kmers]$ python3 count_kmers1.py
CGWWGGCNGNGCNAGANTGC
