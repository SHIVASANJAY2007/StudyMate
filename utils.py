# Helper functions here

def clean_text(text):
    """
    Clean the input text by removing extra whitespace and normalizing.
    """
    if not text:
        return ""
    # Remove extra whitespace and strip
    cleaned = ' '.join(text.split())
    return cleaned
def split_text_into_chunks(text, chunk_size=1000):
    """
    Split the text into chunks of specified size.
    """
    if not text:
        return []
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        if chunk:  # Avoid empty chunks
            chunks.append(chunk)
    return chunks
