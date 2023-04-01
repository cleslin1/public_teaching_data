"""
Standalone python module to show how pandas can be used to consume a VCF file from FACETS
"""

import argparse
import io
import pandas as pd


def main() -> None:
    """
    Business logic
    @return: None
    """

    args = get_cli_args()
    # get the data frame from the facets output
    df = get_facets_vcf_df(facets_vcf_file=args.facets_vcf_file)
    # update for loh level events in a list of genes
    update_gene_cols(df=df, svtype_list=['LOH', 'DUP-LOH', 'HEMIZYG'], column_name="loh_positive",
                     genes=get_loh_genes())
    # update for deletion level events in a list of genes
    update_gene_cols(df=df, svtype_list=['DEL'], column_name="loss_positive",
                     genes=get_del_genes())  # no 'DUP-LOH, 'LOH', 'HEMIZYG'
    # output the results
    df.to_excel("test.xlsx")


def get_loh_genes() -> list:
    """
    Just a list of genes known to be important in LOH
    list came from
    https://aacrjournals.org/clincancerres/article/28/7/1412/682202/Pan-cancer-Analysis-of-Homologous-Recombination
    :return: list of genes
    """

    return ['ATM', 'ATR', 'ATRX', 'BAP1', 'BARD1', 'BRCA1', 'BRCA2', 'BRIP1', 'CHEK1', 'CHEK2', 'MRE11', 'NBN',
            'PALB2', 'RAD51B', 'RAD51C', 'RAD51D']


def get_del_genes() -> list:
    """
    Just a list of genes known to be important when there's deletions
    :return: list of genes
    """

    return ['BRCA1', 'BRCA2', 'PTEN', 'RB1', 'TP53']


def update_gene_cols(df: pd.DataFrame = None, svtype_list: list = None,
                     column_name: str = None, genes: list = None) -> None:
    """
    Update the data frame with new columns if there was a match to certain genes
    @param df: DataFrame to check
    @param svtype_list: structural variant type to look for
    @param column_name: column name for the dataframe
    @param genes: list of genes to look for
    @return: None
    """
    for gene in genes:
        df[f'{gene}_{column_name}'] = \
            df.apply(lambda x, y=gene: is_gene_positive(row=x, gene=y,
                                                        svtype_list=svtype_list), axis=1)


def is_gene_positive(row: pd.Series = None, gene: str = None, svtype_list: list = None) -> bool:
    """
    Is the Pandas series contain a gene was event of the type SVTYPE passed in
    :param row: Pandas series
    :param gene: Gene to search for
    :return: Bool
    """
    return bool(gene in row['CNV_ANN'] and row['SVTYPE'] in svtype_list)


def get_facets_vcf_df(facets_vcf_file: str = None) -> pd.DataFrame:
    """
    :param facets_vcf_file: string of the VCF file open
    :return: Return a pandas data frame of the VCF, with discrete elements for the INFO column
    """
    vcf_df = _read_dataset_and_get_pandas_df(col_vals=_get_columns_from_facets_vcf(),
                                             file_name=facets_vcf_file,
                                             ignore_line_starts_with='##')
    # Parse out the INFO column and create a new data frame that will be merged
    # Browsing a Series is much faster that iterating across the rows of a dataframe.
    vcf_df_updated = pd.DataFrame([dict([x.split('=') for x in t.split(';')])
                                   for t in vcf_df['INFO']], index=vcf_df['ID']).reset_index()

    # update these three columns to numeric types
    for k, v in {'SVLEN': int, 'CNLR_MEDIAN': float, 'NHET': int}.items():
        # pylint: disable=unsubscriptable-object
        # pylint: disable=unsupported-assignment-operation
        vcf_df_updated[k] = vcf_df_updated[k].astype(v)

    # two data frames should be the same, so just join on ID for the VCF output, since this is unique for one
    # Facets VCF file
    assert len(vcf_df) == len(vcf_df_updated), "data frames were not the same size, and should be"
    final_df = pd.merge(vcf_df, vcf_df_updated, on='ID')

    return final_df


def _get_columns_from_facets_vcf() -> dict:
    """
    :return: dictionary columns (keys) with types (values) from a VCF file for FACETS
    """

    col_vals = {
        "#CHROM": str,
        "POS": int,
        "ID": str,
        "REF": str,
        "ALT": str,
        "QUAL": str,
        "FILTER": str,
        "INFO": str
    }
    return col_vals


def _read_dataset_and_get_pandas_df(col_vals: dict = None, file_name: str = None, keep_default_na: bool = True,
                                    ignore_line_starts_with: str = "#") -> pd.DataFrame:
    """
    :param col_vals: Dictionary of column names and types
    :param file_name: File to open
    :param keep_default_na: Boolean to keep the NAs or covert them via Pandas
    :param ignore_line_starts_with: What character to ignore, default #
    Input:  The column values as a dictionary with the key = to the column, and the value = type, e.g. int, str, etc
    Output: pandas data frame
    """

    with open(file_name, 'r', encoding="utf8") as infh:
        lines = [lines for lines in infh if not lines.startswith(ignore_line_starts_with)]  # ignore comments
    # get the dataframe
    df = pd.read_table(
        # A text stream using an in-memory text buffer. It inherits TextIOBase.
        io.StringIO(''.join(lines)),
        usecols=list(col_vals.keys()),
        dtype=col_vals,  # pass in the dictionary of key values, key is the column, key is the type, e.g. int, float...
        keep_default_na=keep_default_na,
        sep='\t'
    )
    return df


def get_cli_args() -> argparse:
    """
    Get the argparse instance
    Takes: no arguments
    :return: instance of argparse arguments
    """

    parser = argparse.ArgumentParser(description="This caller will take a VCF from FACETS and calculate the "
                                                 "genome-level LOH metrics")
    parser.add_argument('--facets_vcf_file',
                        dest='facets_vcf_file',
                        type=str,
                        help='VCF file from FACETS output.  Used to calculate the genome-level metrics for LOH',
                        required=True)

    return parser.parse_args()


if __name__ == '__main__':
    main()
