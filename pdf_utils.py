import PyPDF2
import io

def extract_text_from_pdf(uploaded_file):
    """
    Extract text from an uploaded PDF file.
    """
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text
