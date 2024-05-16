import pytesseract
from PIL import Image

# Set the path to the Tesseract executable (change this as needed)
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

def ocr_scan(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Perform OCR on the image
        text = pytesseract.image_to_string(img)
        return text.strip()

# Example usage
image_path = 'data\data_jpg\input6.jpg'
result = ocr_scan(image_path)
print("Detected Text:")
print(result)
