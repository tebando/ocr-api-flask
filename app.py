from flask import Flask, request
import pytesseract
from pdf2image import convert_from_bytes

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def ocr_pdf():
    if request.method == "GET":
        return "OCR API is running."

    pdf_data = request.data
    images = convert_from_bytes(pdf_data, first_page=1, last_page=1)
    text = pytesseract.image_to_string(images[0])
    return text
