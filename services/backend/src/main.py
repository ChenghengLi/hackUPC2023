from fastapi import FastAPI, File, UploadFile,Response
from fastapi.middleware.cors import CORSMiddleware  
from src.Summarizer import Summarizer
from src.Reader import Reader
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
    
    return summarizer.summarize(reader.returnPaperContent())

@app.post("/upload")
async def create_upload_file(file: UploadFile = File(...)):
    
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
    # Write the contents of the uploaded file to the temporary file
        tmp.write(file.file.read())
        # Generate the PDF file from the temporary file
        pdf_path = f"{tmp.name}.pdf"
        pdfkit.from_file(tmp.name, pdf_path)
    
    # Return the path to the PDF file for download
    response = Response(content=pdf_path)
    response.headers["Content-Disposition"] = f"attachment; filename={file.filename}.pdf"
    return response
    # Convert the uploaded file to PDF
    pdfkit.from_file(file.filename, 'output.pdf')


    # Return the PDF file

    # Aquí puedes trabajar con el contenido del archivo, por ejemplo, guardarlo en disco
    rd = Reader("src/exempledef.pdf")
    print(rd.returnPaperContent())
    return {"filename": file.filename}
