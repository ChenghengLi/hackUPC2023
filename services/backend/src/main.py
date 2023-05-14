from fastapi import FastAPI, File, UploadFile,Response
from fastapi.middleware.cors import CORSMiddleware  

from src.Summarizer import Summarizer
from src.Reader import Reader
from src.QuestionGenerator import QGenerator
import pdfplumber
from fastapi.responses import JSONResponse
import io

import nltk

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')

app = FastAPI()

origins = [
    "https://frontend-chenghengli.cloud.okteto.net",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/data/")
def getQuestions():
    output = dict()
    summarizer = Summarizer()
    sum = summarizer.summarize(Reader.text)
    question = QGenerator(sum)
    output["topic"] = sum
    output["question"] = question.gerateMCQ()
    print(output)
    Reader.text = ""
    return JSONResponse(output)
    '''
    output = dict()
    i = 0
    for i in range(0, reader.pages() + 1, 2):
        text = reader.returnPaperContent(i, i + 2)
        print(text)
        sum = summarizer.summarize(reader.returnPaperContent(i, i + 2))
        question = QGenerator(reader.returnPaperContent(i, i + 2))
        dict[i] = {"sum": sum, "question": question.gerateMCQ()}
        i += 1
    '''


@app.post("/upload/")
async def create_upload_file(pdf_file: UploadFile = File(...)):

    with pdf_file.file as file:
        pdf = pdfplumber.open(file).pages
        Reader.paperContent = pdf
        for i in range(len(pdf)):
            Reader.text +=pdf[i].extract_text()
            Reader.text += "\n"
    return {"file": pdf_file}

