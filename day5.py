# 5) python program to calculate the frequency of the word in a given text. print the words and their corresponding counts
from collections import Counter

def word_frequency(text):
    
    text = text.lower()
    
    
    text = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in text)
    
    
    words = text.split()
    
    
    word_counts = Counter(words)
    
    
    for word, count in word_counts.items():
        print(f"{word}: {count}")


sample_text = "This is a sample text. This text is just a sample."


word_frequency(sample_text)
