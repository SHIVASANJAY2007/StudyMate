from transformers import pipeline
import os

def generate_answer(question, context):
    """
    Generate an answer to the question based on the context using Hugging Face transformers.
    """
    # Load a pre-trained question-answering model
    qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
    
    # Use the pipeline to answer the question
    result = qa_pipeline(question=question, context=context)
    return result['answer']
