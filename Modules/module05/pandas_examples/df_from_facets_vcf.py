"""
Show an example of opening a VCF file from FACETS and transform it into a Pandas VCF file
"""
import argparse
import io
import pandas as pd


def main() -> None:
    """Business Logic to show some Pandas functions"""
    args = get_cli_args()
    facets_df = return_df_from_vcf_file(facets_vcf_file=args.facets_vcf_file)
    # filter the df where SVTYPE is 'DUP'
    facets_df_filtered = facets_df[facets_df['SVTYPE'] == 'DUP']
    # filter the df where SVTYPE is 'DUP' and CHROM == 14
    facets_df_filtered2 = facets_df[(facets_df['SVTYPE'] == 'DUP') & (facets_df['CHROM'] == '14')]
    # print out the full df
    facets_df.to_csv("facets_vcf.tsv", sep='\t', header=True)
    # print out the filtered data frames
    facets_df_filtered.to_csv("facets_vcf_filtered.tsv", sep='\t', header=True)
    facets_df_filtered2.to_csv("facets_df_filtered2.tsv", sep='\t', header=True)
    # print out the head
    print(facets_df_filtered.head())


def return_df_from_vcf_file(facets_vcf_file: str = None) -> pd.DataFrame:
    """
    @param facets_vcf_file: string of the VCF file_name open
    @return: Return a pandas data frame of the VCF, with discrete elements for the INFO column
    """
    vcf_df = read_vcf(facets_vcf_file=facets_vcf_file)
    # Parse out the INFO column and create a new data frame that will be merged
    # Browsing a Series is much faster that iterating across the rows of a dataframe.
    vcf_df_updated = pd.DataFrame([dict([x.split('=') for x in t.split(';')])
                                   for t in vcf_df['INFO']],
                                  index=vcf_df['ID']).reset_index()
    # two data frames should be the same, so just join on ID for the VCF output, since this is unique for one
    # Facets VCF file_name
    assert len(vcf_df) == len(vcf_df_updated)
    final_df = pd.merge(vcf_df, vcf_df_updated, on='ID')
    return final_df


def read_vcf(facets_vcf_file: str = None) -> pd.DataFrame:
    """
    @param facets_vcf_file: string of the VCF file_name open
    @return: Return a data frame of the VCF, INFO column is not discrete at this point
    """
    with open(facets_vcf_file, 'r') as in_fh:
        lines = [l for l in in_fh if not l.startswith('##')]
    return pd.read_csv(
        io.StringIO(''.join(lines)),
        dtype={'#CHROM': str, 'POS': int, 'ID': str, 'REF': str, 'ALT': str,
               'QUAL': str, 'FILTER': str, 'INFO': str},
        sep='\t'
    ).rename(columns={'#CHROM': 'CHROM'})


def get_cli_args():
    """
    void: get_cli_args()
    Takes: no arguments
    Returns: instance of argparse arguments
    """
    parser = argparse.ArgumentParser(description='Open a FACETS VCF file and turn it into a Pandas DataFrame')
    parser.add_argument('--facets_vcf_file',
                        dest='facets_vcf_file',
                        type=str, help='FACETS VCF file_name',
                        required=True)
    return parser.parse_args()


if __name__ == "__main__":
    main()
