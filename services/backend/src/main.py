from fastapi import FastAPI, File, UploadFile,Response
from fastapi.middleware.cors import CORSMiddleware  

from src.Summarizer import Summarizer
from src.Reader import Reader
from src.QuestionGenerator import QGenerator
import pdfplumber
from fastapi.responses import JSONResponse


app = FastAPI()

origins = [
    "https://frontend-chenghengli.cloud.okteto.net/",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


reader = Reader("src/exempledef.pdf")

@app.get("/data/")
async def getQuestions():
    reader = Reader("src/exempledef.pdf")
    summarizer = Summarizer()
    summarizer.detect_language(reader.returnPaperContent())
    question = QGenerator(reader.returnPaperContent(1,2))
    return "prueba" #JSONResponse(content=question.gerateMCQ())

    # Return the PDF file

@app.post("/upload/")
async def create_upload_file(pdf_file: UploadFile = File(...)):
    with pdf_file.file as file:
        pdf = pdfplumber.load(file)
        pages = pdf.pages
        for page in pages:
            text = page.extract_text()
            print(text)
