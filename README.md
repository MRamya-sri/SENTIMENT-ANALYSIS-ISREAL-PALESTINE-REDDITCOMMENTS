# SENTIMENT-ANALYSIS-ISREAL-PALESTINE-REDDITCOMMENTS

## Table of Contents
[Introduction]

[Features]

[Installation]

[Usage]

[Data Preprocessing]

[Sentiment Analysis]

[Visualizations]

[Results]

[Contributing]

[License]


## Introduction
This project performs sentiment analysis on Reddit comments related to the Israel-Palestine conflict. The goal is to analyze the sentiments expressed in these comments and categorize them as positive, negative, or neutral. The project involves data preprocessing, sentiment analysis using TextBlob, and visualizations to understand the sentiment distribution.
This project performs sentiment analysis on Reddit comments related to the Israel-Palestine conflict. The goal is to analyze the sentiments expressed in these comments and categorize them as positive, negative, or neutral. The project includes data preprocessing, sentiment analysis using TextBlob, and visualizations to provide insights into the sentiment distribution.
The sentiment analysis is followed by a classification step where a logistic regression model is trained to classify the sentiment of the comments. The model's performance metrics indicate the effectiveness of the sentiment classification process.

## Features
1.Data cleaning and preprocessing

2.Sentiment analysis using TextBlob

3.Visualizations of sentiment distribution and other insights

4.Sentiment classification using Logistic Regression

## Data Preprocessing
The data preprocessing steps include:

  -> Removing duplicates and null values
  
  -> Converting text to lowercase and removing punctuation
  
  -> Tokenization, stopword removal, and lemmatization
  
  -> Removing emojis and extra whitespace
  
## Sentiment Analysis
The sentiment analysis process involves:

  -> Using TextBlob to calculate sentiment polarity
  
  -> Categorizing sentiment polarity into positive, negative, and neutral
  
  -> Creating a numeric representation of sentiment for classification

  
## Visualizations
The project includes various visualizations to understand the data and results:

  1. Distribution of comments across different subreddits
  
  2. Pie charts and count plots for sentiment categories
  
  3. Correlation between sentiment and score/text length
  
  4. Histograms and violin plots for score distribution

## Sentiment Analysis Visualization


![download](https://github.com/user-attachments/assets/e7bda7d4-bc05-4635-a918-14f38c466b20)

![download (1)](https://github.com/user-attachments/assets/f1df9719-ea95-4ec7-965c-0cf75e29277c)

## Results
The results of the sentiment analysis and classification are displayed in the notebook.

The logistic regression model used for sentiment classification achieved the following performance metrics:

Accuracy: 84.67%

Precision: 0.8489424433054571

Recall: 0.8466527803411817

F1 Score: 0.846699868369603

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes or enhancements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
