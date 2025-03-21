from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import pdfplumber


class File_to_Text_input(BaseModel):
    """Input schema for MyCustomTool."""
    filepath: str = Field(..., description="O caminho para o documento ou URL de um site do qual será extraído o texto")

class File_to_Text(BaseTool):
    name: str = "Conversor de Documentos em textos"
    description: str = (
        "Útil para extrair dados de documentos ou sites em vários formatos (PDF, CSV, TXT, HTML)"
    )
    args_schema: Type[BaseModel] = File_to_Text_input

    def _run(self, filepath: str) -> str:
        #Fazer a leitura do arquivo usando o docling
        with pdfplumber.open(filepath) as pdf:
            text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
            print(text)
        return text