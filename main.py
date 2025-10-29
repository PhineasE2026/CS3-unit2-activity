import pandas as pd
import numpy as np

df = pd.read_csv('movies_metadata_v2.csv', encoding='iso-8859-1').dropna(axis=1, how='all')
print(df.head())
print(df.shape)
print(df.info())

# part B

budget_df = df[df['budget'] > 1000000]
print(budget_df.shape)

budget_lookup = pd.Series(budget_df['budget'].values, index=budget_df['title'])
print(budget_lookup)

condition = (budget_lookup.index >= 'A Bag of Hammers') & (budget_lookup.index <= 'Byzantium')
budget_lookup_A_B = budget_lookup[condition]
print(budget_lookup_A_B)

# part C

movies_by_runtime = pd.Series(df['title'].values, index=df['runtime'])
movies_by_runtime = movies_by_runtime.sort_index()
print(movies_by_runtime.loc[10:180])
print(movies_by_runtime.loc[40].shape)
print(movies_by_runtime.iloc[100])

# part D

df_highly_voted = df[df.vote_count > 20]
df_high_rated = df_highly_voted[df_highly_voted.vote_average > 8]
df_high_rated[['title', 'vote_average', 'vote_count']].head()

my_votes = {
       "Star Wars": 9,
       "Paris is Burning": 8,
       "Dead Poets Society": 7,
       "The Empire Strikes Back": 9.5,
       "The Shining": 8,
       "Return of the Jedi": 8,
       "1941": 8,
       "Forrest Gump": 7.5,
   }

compare_votes = df