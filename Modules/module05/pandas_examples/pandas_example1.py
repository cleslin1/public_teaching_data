import pandas as pd

my_list = [1, 3, 6, 10, 15]
data = pd.Series(my_list)
#print(data)

data = pd.Series(my_list, index=['alpha', 'beta', 'gamma', 'delta', 'epsilon'])
#print(data)

#print(data['delta'])

map_dict = {'ENST': 'RNA', 'ENSG': 'gene', 'ENSP': 'protein'}
data = pd.Series(map_dict)
#print(data)

map_dict = {'ENST': 'RNA', 'ENSG': 'gene', 'ENSP': 'protein'}
count_dict = {'ENST': 3300, 'ENSG': 18435, 'ENSP': 12034}

df = pd.DataFrame({'mapping': map_dict, 'counts': count_dict})
#print(df)

#print(df.index)
#print(df.columns)

print(df['counts'])
print(df.counts)
