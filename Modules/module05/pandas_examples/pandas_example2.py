"""this is a small sample of a list of performances of the two multiple aligners
mafftx and raf. The values represent, in order: method, dataset, average pairwise identity, structural pairwise score,
structural conservation index, reference structural conservation index, and how many sequences were in the dataset
You don't need to understand all these numbers"""

import pandas as pd

biglist = [['mafftx', '5_8S_rRNA', '75', 0.775230007077, 0.7154, 68, 10],
           ['mafftx', '5_8S_rRNA', '76', 0.801566951567, 0.5849, 67, 10],
           ['raf', 'yybP-ykoY', '47', 0.25886864813, 0.8660, 68, 7],
           ['raf', 'yybP-ykoY', '47', 0.273654916512, 0.9000, 74, 7]]

cols = ['method', 'dataset', 'APSI', 'SPS', 'SCI', 'refSCI', 'k']
my_df = pd.DataFrame(biglist, columns=cols)
#print(my_df)
#print("")

#df.index=['first_index', 'second_index', 'another_index', ...]
#df.columns=['measure1', 'measure3', 'measure4', ...]
#print(my_df)

# assume a DataFrame called df

#print(my_df.T)  # returns the transpose of the DataFrame
#print(my_df.dtypes)  # it's plural
#print(my_df.shape)  # like a NumPy array, returns the DataFrame's dimensions
#print(my_df.iloc)  # integer-location indexing
#print(my_df.loc)  # label-location indexing


#print(my_df)
my_df.index=['first', 'second', 'third', 'fourth']
#print("\n")
#print(my_df)

#print(my_df.iloc[1:3])
#print("\n")
#print(my_df.loc['second':'fourth'])


# we can select a portion of the df straight away
#print(my_df.loc['second':'fourth', 'SPS':'SCI'])
#print("\n")
# we can combine them if you have mixed information
#print(my_df.iloc[1:3].loc[:, 'SPS'])

bool_idx = my_df["SCI"] > 0.7
#print(bool_idx)
#print("\n")
#print(my_df[bool_idx])

#print(my_df.info())
#print("\n")
#print(my_df.describe())
#my_df.to_csv("biological_data.tsv", sep='\t', index=False, header=True)


my_df2 = pd.read_csv('biological_data.tsv', delimiter="\t")
print(my_df2)
print("\n")
print(my_df2.info())
