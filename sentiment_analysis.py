# -*- coding: utf-8 -*-
"""sentiment-analysis

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UncVoAfuNVQ8-bDPBS9LoLc_FnImRouP
"""

from google.colab import drive

drive.mount('/content/drive')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('/content/drive/MyDrive/pls_isl_conflict_comments.csv')

df.head()

df.tail()

df.shape

df.columns

df.duplicated().sum()

df.isnull().sum()

df.info()

df.describe()

df.nunique()

object_columns = df.select_dtypes(include=['object']).columns
print("Object type columns:")
print(object_columns)

numerical_columns = df.select_dtypes(include=['int', 'float']).columns
print("\nNumerical type columns:")
print(numerical_columns)

df['subreddit'].unique()

df['subreddit'].value_counts()

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(15, 6))
sns.countplot(data=df, x='subreddit', palette='hls')
plt.xticks(rotation=-45)
plt.show()

# Count the occurrences of each subreddit in the DataFrame
subreddit_counts = df['subreddit'].value_counts()

#create a pie chart

plt.figure(figsize = (10,10))
plt.pie(subreddit_counts, labels = subreddit_counts.index, autopct = '%1.1f%%', startangle=140)
plt.title('Subreddit Distribution')
plt.axis('equal')
plt.show()

plt.figure(figsize=(15,6))
sns.distplot(df['score'], kde = True, bins = 5)
plt.show()

plt.figure(figsize=(15,6))
sns.violinplot(data = df, x='score', palette = 'hls')
plt.show()

df_new = df.copy()

df_new.head()

# convert the text to lowercase and remove leading and trailing whitespace, and it will return the cleaned text.
def clean_text(text):
    text = text.lower()
    return text.strip()

df_new['self_text'] = df_new['self_text'].apply(lambda x: clean_text(x))

df_new.head()

import string
string.punctuation

def remove_punctuation(text):
  punctuationfree = "".join([i for i in text if i not in string.punctuation])
  return punctuationfree

df_new['self_text']= df_new['self_text'].apply(lambda x:remove_punctuation(x))

df_new.head()

import re

def tokenization(text):
  tokens = re.split(r'\W+', text)
  return tokens

df_new['self_text']= df_new['self_text'].apply(lambda x: tokenization(x))

df_new.head()

import nltk

nltk.download('vader_lexicon')
nltk.download('stopwords')

stopwords = nltk.corpus.stopwords.words('english')

def remove_stopwords(text):
  output = " ".join(i for i in text if i not in stopwords)
  return output

df_new['self_text'] = df_new['self_text'].apply(lambda x: remove_stopwords(x))

from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()

def lemmatizer(text):
    lemm_text = "".join([wordnet_lemmatizer.lemmatize(word) for word in text])
    return lemm_text

import nltk
nltk.download('wordnet')

df_new['self_text']=df_new['self_text'].apply(lambda x:lemmatizer(x))

def remove_emojis(data):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    return re.sub(emoji_pattern, '', data)

df_new['self_text'] = df_new['self_text'].apply(lambda x: remove_emojis(x))

df_new['self_text'] = df_new['self_text'].apply(lambda x:re.sub(r'\s+[a-zA-Z]\s+', '', x))

df_new['self_text'] = df_new['self_text'].apply(lambda x:re.sub(r'\s+', ' ', x, flags=re.I))

df_new.head()

from textblob import TextBlob

df_new['sentiment'] = df_new['self_text'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

df_new.head()

sentiment_correlation = df_new[['score', 'sentiment']].corr()
print('Correlation between "score" and "sentiment":')
print(sentiment_correlation)

average_score_per_subreddit = df_new.groupby('subreddit')['score'].mean()
print('Average score per subreddit:')
print(average_score_per_subreddit)

df_new['created_time'] = pd.to_datetime(df_new['created_time'])

df_new.head()

df_new['text_length'] = df_new['self_text'].apply(len)

df_new.head(2)

length_correlation = df_new[['score', 'text_length']].corr()
print('Correlation between "score" and text "length":')
print(length_correlation)

from collections import Counter

plt.figure(figsize=(15,6))
plt.hist(df_new['text_length'], bins=30, edgecolor='black')
plt.xlabel('Text Length')
plt.ylabel('Frequency')
plt.title('Histogram of Text Length')
plt.show()

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation as LDA

text_data = df_new['self_text'].astype(str)

text_data

vectorizer = CountVectorizer(max_df=0.85, stop_words='english')
text_vectorized = vectorizer.fit_transform(text_data)

num_topics = 5
lda = LDA(n_components=num_topics, random_state=42)
lda.fit(text_vectorized)

def categorize_sentiment(polarity):
    if polarity > 0.05:
        return 'Positive'
    elif polarity < -0.05:
        return 'Negative'
    else:
        return 'Neutral'

df_new['sentiment_category'] = df_new['sentiment'].apply(categorize_sentiment)

df_new.head()

df_new['sentiment_category'].unique()

df_new['sentiment_category'].value_counts()

plt.figure(figsize=(15,6))
sns.countplot(data = df_new, x='sentiment_category', palette = 'hls')
plt.show()

# Group the data by sentiment category and count the number of occurrences
sentiment_counts = df_new['sentiment_category'].value_counts()

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Sentiment Category Distribution')
plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.

plt.show()

def map_sentiment_to_numeric(sentiment_category):
    if sentiment_category == 'Positive':
        return 1
    elif sentiment_category == 'Negative':
        return -1
    else:
        return 0

df_new['sentiment_numeric'] = df_new['sentiment_category'].apply(map_sentiment_to_numeric)

df3 = df_new[['self_text', 'sentiment_numeric']]

df3.head()

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import precision_recall_fscore_support
from sklearn.feature_extraction.text import TfidfVectorizer

X = df_new['self_text']
y = df_new['sentiment_numeric']

tfidf_vectorizer = TfidfVectorizer(max_features=5000)
X_tfidf = tfidf_vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression

lr_classifier = LogisticRegression()
lr_classifier.fit(X_train, y_train)

y_pred = lr_classifier.predict(X_test)
lr_accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", lr_accuracy)

precision, recall, f1, _ = precision_recall_fscore_support(y_test, y_pred, average='weighted')
print('Precision:', precision)
print('Recall:', recall)
print('F1 Score:', f1)


