from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware  
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
    return "FDSfsdfghfhgfhgfhddfdfd1111!"

@app.post("/upload")
async def uploadpdf(file: UploadFile = File(...)):
    contents = await file.read()
    # do something with the file contents
    print(contents)
    return {"filename": file.filename}


