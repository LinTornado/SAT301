import pandas as pd

# Load the Excel file into a pandas DataFrame
df = pd.read_excel('CNN-DailyMail News/test.xlsx', nrows=1933)

# Extract the 'article' and 'highlights' columns
articles = df['article']
highlights = df['highlights']

articles = articles.str.replace('\r', '').str.replace('\n', '')
highlights = highlights.str.replace('\r', '').str.replace('\n', '')

# Write the article to a text file
with open('CNN-DailyMail News/test/article.txt', 'w', encoding='utf-8') as f:
    for article in articles:
        f.write(str(article) + '\n')

# Write the highlights to a text file
with open('CNN-DailyMail News/test/title_filtered.txt', 'w', encoding='utf-8') as f:
    for highlight in highlights:
        f.write(str(highlight) + '\n')