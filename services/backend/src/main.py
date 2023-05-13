from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  

from src.Summarizer import Summarizer
from src.Reader import Reader
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
    
    return summarizer.summarize(reader.returnPaperContent())


