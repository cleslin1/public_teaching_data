"""
Compare two FASTA files for kmer jaccard index and containment
Using Code we've learned through the semester
"""
import argparse
import sys
from typing import TextIO

from count_kmers2 import count_kmer


def main():
    """
    Business Logic
    Assumptions here:  Each FASTA file provided at the command line only has 1 sequence in it, since only the first
    sequence in the file will be analyzed
    """
    args = get_cli_args()
    infile1, infile2 = args.infile1, args.infile2

    fh_in1 = get_filehandle(file=infile1, mode="r")
    # get the two lists of data for the first file
    _, seqs1 = get_fasta_lists(fh_in1)

    fh_in2 = get_filehandle(file=infile2, mode="r")
    # get the two lists of data for the second file
    _, seqs2 = get_fasta_lists(fh_in2)

    fh_in1.close()
    fh_in2.close()

    compare_genomes(seq1=seqs1[0], seq2=seqs2[0])


def compare_genomes(seq1: str, seq2: str) -> None:
    """
    Go over each FASTA sequence and compare them using kmers
    @param seq1: DNA seq1
    @param seq2: DNA seq2
    @return: None
    """
    print(seq1)
    # go over different kmer lengths and find the jaccard index and jaccard containment
    for kmer_len in range(2, 31, 1):
        # get the counts
        counts1 = count_kmer(seq1, kmer_len=kmer_len).keys()  # get all k-mers
        counts2 = count_kmer(seq2, kmer_len=kmer_len).keys()  # get all k-mers

        # print out the jaccard index
        print(f"kmer_len: {kmer_len}, "
              f"jaccard_index: {jaccard_index(container1=counts1, container2=counts2)}")
        # print out the jaccard containment
        print(f"kmer_len: {kmer_len}, "
              f"jaccard_containment: {jaccard_containment(container1=counts1, container2=counts2)}")


def jaccard_index(container1: list, container2: list) -> float:
    """
    Given any two collections of k-mers, we can calculate Jaccard Index using the union functionality in Python
    The Jaccard index, is a statistic used for gauging the similarity and diversity of sample sets

    Here the similarity of two sets is found by comparing the relative size of the intersection over the union
    (Broder, 1997). For two non-empty finite sets A and B, the Jaccard index is defined as:
    J(A,B) = |A∩B| / |A∪B|
    Hence, 0 ≤ J(A,B) ≤ 1 with larger values indicating more overlap.

    @param container1: list of kmers1
    @param container2: list of kmer2
    @return: float
    """
    container1 = set(container1)
    container2 = set(container2)

    intersection = len(container1.intersection(container2))
    union = len(container1.union(container2))

    return intersection / union


def jaccard_containment(container1: list, container2: list) -> float:
    """
    Given any two collections of k-mers, we can calculate containment using the intersection functionality in Python.

    Similarly, the containment index (CI) of A in B (with A non-empty) measures the relative size of the intersection
    over the size of A: C(A,B) = |A∩B| / |A|
    So 0 ≤ C(A,B) ≤ 1 with larger values indicating that more content of A resides in B.

    @param container1: list of kmers1
    @param container2: list of kmer2
    @return: float
    """
    container1 = set(container1)
    container2 = set(container2)

    intersection = len(container1.intersection(container2))

    return intersection / len(container1)


def get_filehandle(file: str = None, mode: str = None) -> TextIO:
    """
    filehandle : get_filehandle(infile, "r")
    Takes : 2 arguments fh_in name and mode i.e. what is needed to be done with
    this fh_in. This function opens the fh_in based on the mode passed in
    the argument and returns filehandle.
    @param file: The fh_in to open for the mode
    @param mode: They way to open the fh_in, e.g. reading, writing, etc
    @return: filehandle
    """

    try:
        fobj = open(file, mode)
        return fobj
    except OSError:
        print(f"IOError: Could not open the fh_in: {file} for type '{mode}'", file=sys.stderr)
        raise
    except ValueError:
        print(f"ValueError: Could not open the fh_in: {file} for type '{mode}'", file=sys.stderr)
        raise


def get_fasta_lists(fh_in: TextIO = None) -> (list, list):
    """
    list, list: get_fasta_lists(fh_in)
    Takes : 1 arguments i.e. infile object. This functions opens the fh_in
    and splits the header and sequence into corresponding list and returns them.
    @param fh_in: A open filehand for reading
    @return: Two list of headers, list of sequences
    """

    header_list = []
    seq_list = []
    current_seq = ''  # always initialize variables in python.

    for line in fh_in:
        # matched a new record
        if line[0] == ">":
            header_list.append(line[1:].rstrip('\n'))
            if current_seq != '':
                seq_list.append(current_seq)  # add on the data if there was sequence data
            current_seq = ''  # reset the variable
        else:
            current_seq += line.rstrip('\n')

    if current_seq:
        seq_list.append(current_seq)

    # where the lists the same size?
    _verify_lists(header_list=header_list, seq_list=seq_list)

    return header_list, seq_list


def _verify_lists(header_list: list = None, seq_list: list = None) -> bool:
    """
    True : _verify_lists(header_list, seq_list)
    Takes : 2 arguments i.e. Header list and Seq list. Returns nothing if the
    size of the two lists are same and exists otherwise.
    @param header_list: List of headers for the fasta fh_in
    @param seq_list: List of sequences for the fasta fh_in
    @return: Boolean, True or exists the program
    """
    size1 = len(header_list)
    size2 = len(seq_list)
    if size1 != size2:
        sys.exit("Header and Sequence lists are different in size\n" +
                 "Did you provide a FASTA formatted fh_in?")
    else:
        return True


def get_cli_args() -> argparse.Namespace:
    """
    Just get the command line options using argparse
    @return: Instance of argparse arguments
    """

    parser = argparse.ArgumentParser(description='Provide a FASTA fh_in to generate kmer comparision')

    parser.add_argument('--infile1', dest='infile1',
                        type=str, help='Path to FASTA file 1 to open', required=True)

    parser.add_argument('--infile2', dest='infile2',
                        type=str, help='Path to FASTA file 2 to open', required=True)

    return parser.parse_args()


if __name__ == '__main__':

    main()
