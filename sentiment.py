from textblob import TextBlob

# Define a sample text to analyze
text = "This movie was great, I really enjoyed it!"

# Create a TextBlob object and analyze the sentiment
blob = TextBlob(text)
polarity = blob.sentiment.polarity
subjectivity = blob.sentiment.subjectivity

# Print the results
print("Polarity: ", polarity)
print("Subjectivity: ", subjectivity)

# Define another sample text to analyze
text2 = "This movie was terrible, I hated it!"

# Create another TextBlob object and analyze the sentiment
blob2 = TextBlob(text2)
polarity2 = blob2.sentiment.polarity
subjectivity2 = blob2.sentiment.subjectivity

# Print the results
print("Polarity: ", polarity2)
print("Subjectivity: ", subjectivity2)

