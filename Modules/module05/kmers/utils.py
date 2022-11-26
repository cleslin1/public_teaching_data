"""Utility module for counting kmers"""
import random
from operator import itemgetter


def generate_random_dna_str(num, alphabet='AGCT'):
    """
    Return a random DNA sequenced
    @param num: Length of the DNA string
    @param alphabet: Alphabet to use
    @return: string
    """
    return ''.join([random.choice(alphabet) for i in range(num)])


def print_trinucleotides(counts, threshold=1):
    """
    Print out the dictionary sorted by value and then by key using itemgetter
    @param counts: Dictionary of triplets
    @param threshold: Use this threshold to ignore values smaller when printing
    @return: None
    """
    # use itemgetter to sorty by the key and then the value
    for key, value in sorted(counts.items(), key=itemgetter(1, 0), reverse=True):
        if value >= threshold:
            print(key, value)
