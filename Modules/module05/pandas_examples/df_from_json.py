import pandas as pd
df = pd.read_json('human_EGFR_variants.json')
print(f"Size of the df, {len(df)}")
print(df.head())

# print out all unique values
print(df['source'].unique())

# print out all unique values
print(df['consequence_type'].unique())

# print out examples from the df where consequence_type == stop_lost
print(df[df['consequence_type'] == 'stop_lost'])