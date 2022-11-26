"""Code to count DNA trinucleotides and then store them in a Dict and sort them out"""
from utils import generate_random_dna_str, print_trinucleotides


def main():
    """Simple function to call our other functions"""
    dna = generate_random_dna_str(200000, 'ACGT')  # get a randome dna sequence of 2000bp
    counts = count_kmer(dna)
    print_trinucleotides(counts, threshold=1000)


def count_kmer(dna, kmer_len=3):
    '''
    Count the number of kmers that occur in the sequence dna (including overlapping occurrences)
    sample use: count_mer("GGG", "AGGGCGGG") => 2
    @param dna: The sequence to explore for kmers
    @parm kmer_len: Int of the kmer size
    '''

    kmers = {}
    for i in range(0, len(dna) - kmer_len + 1):
        kmer = dna[i:i + kmer_len]
        kmers[kmer] = kmers.get(kmer, 0) + 1
    return kmers


def test_code():
    """
    Simple test of the code
    @return: None
    """
    counts = count_kmer('GATTACA', kmer_len=3)
    expected = {'GAT': 1, 'ATT': 1, 'TTA': 1, 'TAC': 1, 'ACA': 1}
    assert counts == expected

    counts = count_kmer('GATTACA', kmer_len=4)
    print(counts)
    expected = {'GATT': 1, 'ATTA': 1, 'TTAC': 1, 'TACA': 1}
    assert counts == expected


if __name__ == '__main__':
    main()
    test_code()
