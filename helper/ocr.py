import pytesseract
from PIL import Image

# Use OCR to retrieve text
def getOCR(document):
    image = Image.open(document)
    text = pytesseract.image_to_string(image)
    return text

