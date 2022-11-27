import pandas as pd
df = pd.read_json('human_EGFR_variants.json')
print(df)


print(df['source'].unique())