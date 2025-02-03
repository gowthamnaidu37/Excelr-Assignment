import gensim
import nltk
from gensim.utils import simple_preprocess
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# Download necessary NLTK resources
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')

def preprocess_text(text):
    # Tokenization using gensim
    tokens = simple_preprocess(text)
    
    # Stemming using NLTK's PorterStemmer
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in tokens]
    
    # Lemmatization using WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in stemmed_tokens]
    
    # Removing stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in lemmatized_tokens if word not in stop_words]
    
    return " ".join(filtered_tokens)

# Example text input
text = "This is a simple example demonstrating Gensim preprocessing techniques."

# Process the text
processed_text = preprocess_text(text)
print("Processed Text:", processed_text)
