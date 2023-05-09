import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Define the data
data = {'items': ['apple', 'banana', 'orange', 'pear', 'grape'],
        'descriptions': ['red and juicy', 'yellow and sweet', 
        'orange and citrusy', 'green and crunchy', 'purple and tart']}
df = pd.DataFrame(data)

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Vectorize the item descriptions
vectors = vectorizer.fit_transform(df['descriptions'])

# Compute the cosine similarities between item vectors
similarities = cosine_similarity(vectors)

# Define the item to recommend similar items for
item_index = 0

# Get the indices of the top 3 most similar items
similar_item_indices = similarities[item_index].argsort()[:-4:-1]

# Print the recommended items
print('For item "{}", recommended similar items are:'.format(df['items'][item_index]))
for i in similar_item_indices[1:]:
    print('- {}'.format(df['items'][i]))



