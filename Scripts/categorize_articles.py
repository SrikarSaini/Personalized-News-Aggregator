import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import pandas as pd

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
punctuation = set(string.punctuation)

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word not in stop_words and word not in punctuation]
    return tokens

def categorize_article(text):
    if isinstance(text, str):
        tokens = preprocess_text(text)
        print(f"Tokenized Text: {tokens}")
        
        tech_keywords = {'technology', 'tech', 'ai', 'artificial', 'intelligence', 'computers', 'science', 'software'}
        sports_keywords = {'sport', 'game', 'football', 'cricket', 'basketball', 'tennis', 'athletics'}
        politics_keywords = {'politics', 'government', 'election', 'minister', 'congress', 'president', 'parliament'}
        
        if any(word in tokens for word in tech_keywords):
            print("Category: Technology")
            return "Technology"
        elif any(word in tokens for word in sports_keywords):
            print("Category: Sports")
            return "Sports"
        elif any(word in tokens for word in politics_keywords):
            print("Category: Politics")
            return "Politics"
        else:
            print("Category: General")
            return "General"
    else:
        print("Invalid summary, skipping.")
        return "Unknown"

articles_df = pd.read_csv('news_articles.csv')
articles_df['Category'] = articles_df['summary'].apply(categorize_article)
articles_df.to_csv('news_articles.csv', index=False)

print("Categorization complete!")
