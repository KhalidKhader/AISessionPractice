import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Define some example texts to analyze
texts = ['This is a great day!', 
         'I feel so happy today.', 
         'This is the worst day ever.',
         'I am so sad right now.']

# Analyze each text and print the results
for text in texts:
    scores = analyzer.polarity_scores(text)
    print(text)
    print('Positive Score:', scores['pos'])
    print('Negative Score:', scores['neg'])
    print('Neutral Score:', scores['neu'])
    print('Overall Sentiment:', scores['compound'])


