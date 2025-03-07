from docling.document_converter import DocumentConverter
import pdfplumber

 #Fazer a leitura do arquivo usando o docling
def extract(filepath):  
    converter = DocumentConverter()
    process = converter.convert(filepath)
    text = process.document.export_to_text()
    return print(text)


def extract_text_with_pdfplumber(filepath):
    with pdfplumber.open(filepath) as pdf:
        text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
        print(text)


path = r"D:\Data Science\CrewAi\Finance AI Project\finance_ai_control\files\Controle_familiar - 2024 - 2024.pdf"
extract_text_with_pdfplumber(path)