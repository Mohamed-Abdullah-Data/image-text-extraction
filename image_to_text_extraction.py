"""
OCR Script for Images and PDFs using Tesseract
Author: Your Name
Description:
    - Extracts text from PNG/JPG images or multi-page PDFs
    - Uses pytesseract + pdf2image
    - Logs process to console
"""

import logging
from typing import Optional
from pathlib import Path
from PIL import Image
import pytesseract
from pdf2image import convert_from_path

# -------------------
# USER CONFIG
# -------------------
# Adjust these paths to match your local installation/files
TESSERACT_CMD: Optional[str] = r"C:\Users\addam\Tesseract-OCR\tesseract.exe"
POPPLER_PATH: Optional[str] = r"C:\Users\addam\Poppler\Release-25.07.0-0\poppler-25.07.0\Library\bin"
  # e.g. r"C:/poppler/bin"
IMAGE_PATH: Optional[str] = "C://Users//addam//Downloads//indented-paragraph.png"    # e.g. r"C:/Users/you/Desktop/screenshot.png"
PDF_PATH: Optional[str] = None # e.g. r"C:/Users/you/Desktop/document.pdf"

# -------------------
# Logging setup
# -------------------
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# -------------------
# OCR functions
# -------------------
def ocr_image(image_path: str) -> str:
    """Extract text from a single image file."""
    logger.info("Opening image: %s", image_path)
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text.strip()

def ocr_pdf(pdf_path: str, poppler_path: Optional[str] = None) -> str:
    """Extract text from a multi-page PDF using OCR."""
    logger.info("Converting PDF to images: %s", pdf_path)
    pages = convert_from_path(pdf_path, dpi=300, poppler_path=poppler_path)
    if not pages:
        logger.warning("No pages found in PDF.")
        return ""

    all_text = []
    for i, page in enumerate(pages, start=1):
        logger.info("Processing page %d/%d", i, len(pages))
        text = pytesseract.image_to_string(page)
        all_text.append(f"--- Page {i} ---\n{text.strip()}")

    return "\n\n".join(all_text)

# -------------------
# Main Execution
# -------------------
if __name__ == "__main__":
    # Point pytesseract to tesseract.exe if needed
    if TESSERACT_CMD:
        pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

    extracted_text = ""

    if IMAGE_PATH:
        extracted_text = ocr_image(IMAGE_PATH)
    elif PDF_PATH:
        extracted_text = ocr_pdf(PDF_PATH, poppler_path=POPPLER_PATH)
    else:
        logger.error("No IMAGE_PATH or PDF_PATH specified. Please set one in USER CONFIG.")

    if extracted_text:
        print("\n--- OCR RESULT ---\n")
        print(extracted_text)
