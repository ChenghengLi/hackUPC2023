from fastapi import FastAPI, File, UploadFile,Response
from fastapi.middleware.cors import CORSMiddleware  

from src.Summarizer import Summarizer
from src.Reader import Reader
from src.QuestionGenerator import QGenerator
import pdfplumber
from fastapi.responses import JSONResponse


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://frontend-chenghengli.cloud.okteto.net"],  # https://frontend-chenghengli.cloud.okteto.net   http://localhost:8080
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



@app.post("/upload/")
async def create_upload_file(pdf_file: UploadFile = File(...)):

    with pdf_file.file as file:
        pdf = pdfplumber.open(file).pages
        Reader.paperContent = pdf
        for i in range(len(pdf)):
            Reader.text +=pdf[i].extract_text()
            Reader.text += "\n"
    return {"file": pdf_file}

