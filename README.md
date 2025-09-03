# OCR Image to Text Extraction

## 📌 Overview
This project demonstrates how to extract text from **images (PNG/JPG)** and **PDF documents** using Optical Character Recognition (OCR). It leverages the `pytesseract` library (Python wrapper for Tesseract OCR) and `pdf2image` for handling multi-page PDFs.

## 🚀 Features
- Extracts text from single images (`.png`, `.jpg`)
- Processes multi-page PDFs and extracts text from each page
- Supports custom configuration for **Tesseract OCR** and **Poppler**
- Logs progress and results to the console
- Outputs clean, structured text for further use in NLP or data processing

## 🛠️ Tech Stack
- Python 3.x
- [pytesseract](https://pypi.org/project/pytesseract/)
- [pdf2image](https://pypi.org/project/pdf2image/)
- [Pillow (PIL)](https://pypi.org/project/Pillow/)

## 📂 How It Works
1. Configure file paths in the `USER CONFIG` section:
   - `TESSERACT_CMD` → Path to Tesseract executable
   - `POPPLER_PATH` → Path to Poppler binaries (for PDFs)
   - `IMAGE_PATH` → Local image file
   - `PDF_PATH` → Local PDF file
2. Run the script:
   ```bash
   python image_to_text_extraction.py

![Example Image](https://github.com/Mohamed-Abdullah-Data/image-text-extraction/blob/4b38c9e375894879921df1a3b76d17a4d8d064ce/indented-paragraph.png)

### Example Output
![OCR Output Example](https://github.com/Mohamed-Abdullah-Data/image-text-extraction/blob/4b38c9e375894879921df1a3b76d17a4d8d064ce/OCR%20RESULT.png)
