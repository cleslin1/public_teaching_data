"""Example to show regular expressions"""
import re


def main():
    """Business Logic"""
    print_unigene_data_data(file='TGM1.unigene')


def print_unigene_data_data(file=None):  # noqa: C901  this if for flake8 ignoring
    """
    @param file:  a fh_in and parses with regular expression
    @return: None
    """
    reg_exps = _get_compiled_regex()
    # go over lines and store
    with open(file, "r") as in_fh:
        for line in in_fh:
            line = line.rstrip()
            # go over the regular expressions that might match
            for key, reg_exp in reg_exps.items():
                # match single key-value values below here:
                match = reg_exp.match(line)
                if match:
                    print(f"{key}: {match.group(1)}")


def _get_compiled_regex():
    """
    You can speed up your searches and matches by 'compiling' the regex,
    Note the keyword compile.  This just return a dictionary of those compiled matches.
    What's nice about having them in a dictionary, you have all regular expressions all in one place, and then
    you can look up a given regular expression by a key when you come the need for it when parsing
    @return: Complex nested data structure of the data
    """

    return {
        'CHROMOSOME': re.compile(r'^CHROMOSOME\s+(.*)$'),
        'CYTOBAND': re.compile(r'^CYTOBAND\s+(.*)$'),
        'GENE': re.compile(r'^GENE\s+(.*)$'),
        'GENE_ID': re.compile(r'^GENE_ID\s+(.*)$'),
        'HOMOL': re.compile(r'^HOMOL\s+(.*)$'),
        'ID': re.compile(r'^ID\s+(.*)$'),
        'LOCUSLINK': re.compile(r'^LOCUSLINK\s+(.*)$'),
        'TITLE': re.compile(r'^TITLE\s+(.*)$'),
        # extra processing was needed for these three keys
        'PROTSIM': re.compile(r'^PROTSIM\s+(.*)$'),
        'SEQUENCE': re.compile(r'^SEQUENCE\s+(.*)$'),
        'EXPRESS': re.compile(r'^EXPRESS\s+(.*)$'),
    }


def _match_to_generic_key(line=None, reg_exps=None, dictionary_2_return=None):
    """
    Just update the dictionary_2_return if there was a match to one of the keys
    @param line: New line to parse
    @param reg_exps: The Dictionary of regular expression
    @param dictionary_2_return: The reference to the list to store
    @return: None
    """
    # looop through and do the rest of these simpler mathces
    for key, reg_exp in reg_exps.items():
        # match single key-value values below here:
        match = reg_exp.match(line)
        if match:
            dictionary_2_return[key] = match.group(1)


if __name__ == '__main__':
    main()
