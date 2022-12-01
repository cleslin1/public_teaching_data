"""Code to count DNA trinucleotides and then store them in a Dict and sort them out"""
from utils import generate_random_dna_str, print_trinucleotides


def main() -> None:
    """Simple function to call our other functions"""
    dna = generate_random_dna_str(200_000_000, 'ACGT')  # get a random dna sequence of 2000bp
    counts = count_kmer(dna)
    print_trinucleotides(counts, threshold=1000)


def count_kmer(dna: str, kmer_len: int = 3) -> dict:
    '''
    Count the number of kmers that occur in the sequence dna (including overlapping occurrences)
    @param dna: The sequence to explore for kmers
    @param kmer_len: Int of the kmer size
    @return: Dict of kmers with the value being the number of times it was found in the DNA String
    '''

    kmers = {}
    for i in range(0, len(dna) - kmer_len + 1):
        kmer = dna[i:i + kmer_len]
        kmers[kmer] = kmers.get(kmer, 0) + 1
    return kmers


def test_code() -> None:
    """
    Simple test of the code
    @return: None
    """
    counts = count_kmer('GATTACATT', kmer_len=3)
    expected = {'ACA': 1, 'ATT': 2, 'GAT': 1, 'CAT': 1, 'TAC': 1, 'TTA': 1}
    assert counts == expected

    counts = count_kmer('GATTACA', kmer_len=4)
    expected = {'GATT': 1, 'ATTA': 1, 'TTAC': 1, 'TACA': 1}
    assert counts == expected


if __name__ == '__main__':
    main()
    test_code()
