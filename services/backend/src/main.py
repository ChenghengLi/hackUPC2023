from fastapi import FastAPI, File, UploadFile,Response
from fastapi.middleware.cors import CORSMiddleware  

app = FastAPI()

from src.Summarizer import Summarizer
from src.Reader import Reader
from src.QuestionGenerator import QGenerator
import pdfkit
import shutil
import tempfile
app = FastAPI()



# NEW
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def home():
    reader = Reader("src/exempledef.pdf")
    summarizer = Summarizer()
    summarizer.detect_language(reader.returnPaperContent())
    question = QGenerator(reader.returnPaperContent(1,2))
    return question.gerateMCQ()

    # Return the PDF file

    # Aquí puedes trabajar con el contenido del archivo, por ejemplo, guardarlo en disco
    rd = Reader("src/exempledef.pdf")
    print(rd.returnPaperContent())
    return {"filename": file.filename}
