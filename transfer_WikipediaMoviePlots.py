import pandas as pd

# Read the CSV file, keep only the Plot column and only the first 1933 rows of data
# df = pd.read_csv("wiki_movie_plots_deduped.csv")
# df = df.iloc[:1933][['Plot']]
df = pd.read_csv('Wikipedia Movie Plots/wiki_movie_plots_deduped.csv', usecols=['Plot'], nrows=1933)

# Remove line breaks from each Plot data
# df.replace("\n", "", regex=True, inplace=True)
# print(len(df))
# print(df.head())
df['Plot'] = df['Plot'].str.replace('\r', '').str.replace('\n', '')

# Write data to txt file
with open('Wikipedia Movie Plots/test/movie_plots.txt', 'w', encoding='utf-8') as f:
    for plot in df['Plot']:
        f.write(plot + '\n')