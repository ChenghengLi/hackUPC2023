from fastapi import FastAPI, File, UploadFile,Response
from fastapi.middleware.cors import CORSMiddleware  

from src.Summarizer import Summarizer
from src.Reader import Reader
from src.QuestionGenerator import QGenerator


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




@app.get("/")
def home():
    reader = Reader("src/exempledef.pdf")
    summarizer = Summarizer()
    summarizer.detect_language(reader.returnPaperContent())
    question = QGenerator(reader.returnPaperContent(1,2))
    return question.gerateMCQ()

    # Return the PDF file

@app.post("/upload/")
async def create_upload_file(file: FormData):
    await file.read()
    print("receabed file")
    return {"filename" : file.filename}
