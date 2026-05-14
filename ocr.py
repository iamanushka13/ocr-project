import cv2
import pytesseract

def extract_text(image_path):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found!")
        return ""

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)

    return text