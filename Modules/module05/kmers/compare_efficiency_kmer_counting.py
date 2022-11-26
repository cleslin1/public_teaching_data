"""Comparing the efficiency of the two ways of counting kmers"""
import time
from utils import generate_random_dna_str
from count_kmers1 import count_trinucleotides
from count_kmers2 import count_kmer


def main():
    """Business Logic"""
    run_code()


def run_code():
    """Simple function to test the timing of each function"""

    for length_dna in [20_000, 200_000, 2_000_000, 20_000_000, 200_000_000]:
        functions = [count_trinucleotides, count_kmer]
        dna = generate_random_dna_str(length_dna, 'ACGT')
        timings = []  # timings[i] holds CPU time for functions[i]

        for function_name in functions:
            start = time.time()
            function_name(dna)  # call the function
            stop = time.time()
            cpu_time = stop - start
            timings.append(cpu_time)
        # print the data
        for cpu_time, function_name in sorted(zip(timings, functions)):  # sort by the first value
            print(f"{function_name.__name__:<9s}: {cpu_time:.4f} s length DNA = {length_dna}")
        print("")


if __name__ == '__main__':
    main()
