import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\MLS\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image
def contenuText(chemin):
    text=""
    for ch in chemin :
        img = Image.open(ch)
        text = text + tess.image_to_string(img)+"."
    return text