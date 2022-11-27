"""Comparing the efficiency of the two ways of counting kmers"""
import time
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from utils import generate_random_dna_str
from count_kmers1 import count_trinucleotides
from count_kmers2 import count_kmer


def main():
    """Business Logic"""
    run_code()


def run_code():
    """Simple function to test the timing of each function"""
    # using these values in mlutiple places, so create variables for them
    version1 = "count_trinucleotides"
    version2 = "count_kmer"
    length = "length"
    seconds = "seconds"
    cols = "algorithm"
    # create a dataframe
    # pylint: disable=C0103
    df = pd.DataFrame(columns=[length, version1, version2])
    # Go over each size for the DNA sequence
    for length_dna in [20_000, 200_000, 2_000_000, 20_000_000, 200_000_000]:
        functions = {version1: count_trinucleotides, version2: count_kmer}
        # get the random dna sequence
        dna = generate_random_dna_str(length_dna, 'ACGT')
        # store a timings dictionary that will be converted to a data frame
        timings_dict = {length: length_dna}
        # go over all functions
        for key, function_name in functions.items():
            start = time.time()
            function_name(dna)  # call the function
            stop = time.time()
            cpu_time = stop - start
            timings_dict[key] = cpu_time

        # create a temporary dataframe
        df_temp = pd.DataFrame([{length: timings_dict[length],
                                 version1: timings_dict[version1],
                                 version2: timings_dict[version2]}
                                ])
        # concatenate the dataframes
        df = pd.concat([df, df_temp], ignore_index=True)
    print(df)
    #       length  count_trinucleotides  count_kmer
    # 0      20000              0.123880    0.003020
    # 1     200000              1.010743    0.031198
    # 2    2000000             10.190115    0.300088
    # 3   20000000            101.798687    3.031521
    # 4  200000000           1016.560528   30.536488
    # melt the data frame so the above df now looks like this so we can plot a single column
    dfm = df.melt(length, var_name=cols, value_name=seconds)
    print(dfm)
    #       length             algorithm      seconds
    # 0      20000  count_trinucleotides     0.123880
    # 1     200000  count_trinucleotides     1.010743
    # 2    2000000  count_trinucleotides    10.190115
    # 3   20000000  count_trinucleotides   101.798687
    # 4  200000000  count_trinucleotides  1016.560528
    # 5      20000            count_kmer     0.003020
    # 6     200000            count_kmer     0.031198
    # 7    2000000            count_kmer     0.300088
    # 8   20000000            count_kmer     3.031521
    # 9  200000000            count_kmer    30.536488

    # plot it, and use the hue as "algorithm", this is why the melt was necessary
    sns.catplot(x=length, y=seconds, data=dfm, hue=cols, kind='point')
    # save it
    plt.savefig('output.png')
    # print out the dataframe
    df.to_csv("timings.tsv", sep='\t', index=False, header=True)


if __name__ == '__main__':
    main()
