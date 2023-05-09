from textblob import TextBlob

# Define a sample text
text = """I love this product.
It is the best purchase 
I have ever made."""
text1='I will burn the world'
text2='I hate the world'
#text="hate the world"
# Create a TextBlob object for the text
blob = TextBlob(text2)

# Perform sentiment analysis on the text
sentiment = blob.sentiment.polarity

# Print the sentiment score
print(sentiment)