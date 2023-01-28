"""Two ways to do reverse compliment 1). Using Method chaining 2). Using a loop"""
import time
import random


def main():
    """Business Logic"""
    test_code()
    run_code()


def rev_comp1(dna):
    """
    Using Method chaining for reverse complement DNA
    @param dna: Dna string
    @return: reverse Complement
    """
    rev_dna = dna[::-1].upper()  # rev. dna and every character upper
    rev_comp_dna = rev_dna.replace("A", "t").replace("C", "g"). \
        replace("T", "a").replace("G", "c").upper()
    return rev_comp_dna


def rev_comp2(dna):
    """
    Using Loop to reverse complement DNA
    @param dna: Dna string
    @return: reverese Complement
    """
    comp_dna = ''
    sub_nt = ''
    for nucleotide in dna:
        if nucleotide == 'A':
            sub_nt = 'T'
        elif nucleotide == 'T':
            sub_nt = 'A'
        elif nucleotide == 'C':
            sub_nt = 'G'
        elif nucleotide == 'G':
            sub_nt = 'C'
        else:
            print('input letter is not a DNA base')
        comp_dna = comp_dna + sub_nt

    revcomp_dna = comp_dna[::-1]
    return revcomp_dna


def run_code():
    """Simple function to test the timing of each function"""
    dna = generate_random_dna_str(5_000_000, 'ACGT')
    functions = [rev_comp1, rev_comp2]
    timings = []  # timings[i] holds CPU time for functions[i]

    for function_name in functions:
        start = time.time()
        for _ in range(0, 10):
            function_name(dna)  # call the function
        stop = time.time()
        cpu_time = stop - start
        timings.append(cpu_time)
    # print the data
    for cpu_time, function_name in sorted(zip(timings, functions)):  # sort by the first value
        print(f"{function_name.__name__:<9s}: {cpu_time:.4f} s")


def generate_random_dna_str(num, alphabet='AGCT'):
    """
    Return a random DNA sequenced
    @param num: Length of the DNA string
    @param alphabet: Alphabet to use
    @return: string
    """
    return ''.join([random.choice(alphabet) for i in range(num)])


def test_code():
    """Test the functions work"""
    dna = 'ATGCAGCTGTGTTACGCGAT'
    rev_comp_dna = 'ATCGCGTAACACAGCTGCAT'

    rev_com_dna_to_test = rev_comp1(dna)
    assert rev_comp_dna == rev_com_dna_to_test, "rev_comp1 did not work"

    rev_com_dna_to_test = rev_comp2(dna)
    assert rev_comp_dna == rev_com_dna_to_test, "rev_comp2 did not work"


if __name__ == '__main__':
    main()
