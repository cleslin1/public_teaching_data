"""
Compare two FASTA files for kmer jaccard similarity (index) and containment
Using Code we've learned through the semester
"""
import argparse
import sys
from typing import TextIO

from count_kmers2 import count_kmer


def main():
    """Business Logic"""
    args = get_cli_args()
    infile1, infile2 = args.infile1, args.infile2

    fh_in1 = get_filehandle(file=infile1, mode="r")
    # get the two lists of data
    _, seqs1 = get_fasta_lists(fh_in1)

    fh_in2 = get_filehandle(file=infile2, mode="r")
    # get the two lists of data
    _, seqs2 = get_fasta_lists(fh_in2)

    for kmer_len in range(5, 11, 1):
        counts1 = count_kmer(seqs1[0], kmer_len=kmer_len).keys()
        print("Got counts for FASTA set 1")
        counts2 = count_kmer(seqs2[0], kmer_len=kmer_len).keys()
        print("Got counts for FASTA set 2")

        print(f"kmer_len: {kmer_len}, "
              f"jaccard_similarity: {jaccard_similarity(container1=counts1, container2=counts2)}")
        print(f"kmer_len: {kmer_len}, "
              f"jaccard_containment: {jaccard_containment(container1=counts1, container2=counts2)}")

    fh_in1.close()
    fh_in2.close()


def jaccard_similarity(container1: list = None, container2: list = None) -> float:
    """
    Given any two collections of k-mers, we can calculate similarity
    using the union functionality in Python
    The Jaccard  similarity coefficient (or Jaccard Index), is a statistic used for gauging the similarity and
    diversity of sample sets
    @param container1: list of kmers1
    @param container2: list of kmer2
    @return: flot
    """
    container1 = set(container1)
    container2 = set(container2)

    intersection = len(container1.intersection(container2))
    union = len(container1.union(container2))

    return intersection / union


def jaccard_containment(container1: list = None, container2: list = None) -> float:
    """
    Given any two collections of k-mers, we can calculate
     containment using the intersection functionality in Python.
    @param container1: list of kmers1
    @param container2: list of kmer2
    @return: flot
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
