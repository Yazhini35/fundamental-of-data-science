import pandas as pd
from collections import Counter
import re

# Sample data: DataFrame containing customer reviews
data = {
    'review_id': [1, 2, 3, 4, 5],
    'review_text': [
        'The product is great, I love it!',
        'Excellent quality and very durable.',
        'Not worth the money, very disappointed.',
        'Great product, will buy again.',
        'The quality is okay, not as expected.'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Function to preprocess and tokenize text
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation and numbers
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenize by splitting on whitespace
    words = text.split()
    return words

# Preprocess and tokenize all reviews
all_words = []
for review in df['review_text']:
    all_words.extend(preprocess_text(review))

# Calculate the frequency distribution of words
word_freq = Counter(all_words)

# Display the frequency distribution
print("Frequency distribution of words:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
