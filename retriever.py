from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def retrieve_relevant_docs(question, index, documents, top_k=5):
    """
    Retrieve the most relevant documents based on the question.
    """
    vectorizer, tfidf_matrix = index
    question_vec = vectorizer.transform([question])
    similarities = cosine_similarity(question_vec, tfidf_matrix).flatten()
    top_indices = np.argsort(similarities)[-top_k:][::-1]
    relevant_docs = [documents[i] for i in top_indices]
    return relevant_docs
