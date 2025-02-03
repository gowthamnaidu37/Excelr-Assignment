# Write a Python script that:
# 1. Tokenizes a sample paragraph into words and sentences.

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Download necessary NLTK resources
nltk.download('punkt')

def tokenize_text(text):
    # Tokenize into sentences
    sentences = sent_tokenize(text)
    
    # Tokenize into words
    words = word_tokenize(text)
    
    return sentences, words

# Example text input
text = "This is a simple example. It demonstrates tokenization using NLTK."

# Process the text
sentences, words = tokenize_text(text)
print("Sentences:", sentences)
print("Words:", words)
