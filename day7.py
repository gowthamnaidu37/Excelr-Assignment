# Write a Python program to using NLTK and Spacy
# Convert text to lowercase.
# Remove stopwords using NLTK

import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Load spaCy model (English)
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Tokenize text using NLTK
    words = word_tokenize(text)
    
    # Get NLTK stopwords for English
    stop_words = set(stopwords.words('english'))
    
    # Remove stopwords
    filtered_words = [word for word in words if word not in stop_words]
    
    return " ".join(filtered_words)

# Example usage
input_text = "This is a simple example demonstrating NLTK and spaCy together."
processed_text = preprocess_text(input_text)
print("Processed Text:", processed_text)
