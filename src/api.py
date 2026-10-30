from io import BytesIO

from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.responses import Response
from pypdf.errors import PdfReadError

from process import process_pdf

app = FastAPI(title="InPost Label Fixer")


@app.post("/process")
def process(file: UploadFile):
    output = BytesIO()
    try:
        process_pdf(file.file, output)
    except PdfReadError:
        raise HTTPException(status_code=400, detail="Uploaded file is not a valid PDF")

    return Response(
        content=output.getvalue(),
        media_type="application/pdf",
        headers={"Content-Disposition": 'attachment; filename="label.pdf"'},
    )
