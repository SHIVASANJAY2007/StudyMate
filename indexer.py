from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os

def create_index(documents, index_path='index.pkl'):
    """
    Create a TF-IDF index from the documents.
    """
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)
    index = (vectorizer, tfidf_matrix)
    with open(index_path, 'wb') as f:
        pickle.dump(index, f)
    return index

def load_index(index_path='index.pkl'):
    """
    Load the TF-IDF index from file.
    """
    if os.path.exists(index_path):
        with open(index_path, 'rb') as f:
            index = pickle.load(f)
        return index
    else:
        return None

def index_documents(documents, index_path='index.pkl'):
    """
    Index the documents and save to file.
    """
    return create_index(documents, index_path)
