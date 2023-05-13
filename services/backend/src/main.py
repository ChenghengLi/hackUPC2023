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


reader = None
sumerizer = None

@app.get("/data/")
def getQuestions():
    output = dict()
    summarizer = Summarizer()
    summarizer.detect_language(reader.returnPaperContent())
    i = 0
    for i in range(0, reader.pages() + 1, 2):
        sum = summarizer.detect_language(reader.returnPaperContent(i, i + 2))
        question = QGenerator(reader.returnPaperContent(i, i + 2))
        dict[i] = {"sum": sum, "question": question.gerateMCQ()}
        i += 1
    return "prueba" #JSONResponse(output)

    # Return the PDF file

@app.post("/upload/")
async def create_upload_file(pdf_file: UploadFile = File(...)):
    with pdf_file.file as file:
        pdf = pdfplumber.open(file).pages
        reader = Reader()
        reader.setPaperContent(pdf)
        print(reader.returnPaperContent())

