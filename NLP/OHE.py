from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Sample corpus (list of sentences)
corpus = ["I love NLP", "NLP is amazing", "I love learning"]

# Split each sentence into words
words = set([word for sentence in corpus for word in sentence.split()])

# Create a word-to-index mapping
word_to_index = {word: idx for idx, word in enumerate(words)}

# One-hot encoding for each word in the corpus
def one_hot_encode(word, word_to_index):
    one_hot_vector = np.zeros(len(word_to_index))
    one_hot_vector[word_to_index[word]] = 1
    return one_hot_vector

# Example of one-hot encoding for the word 'NLP'

for word1 in words:
    print(f"One-hot encoding for {word1}:\n{one_hot_encode(word1, word_to_index)}")