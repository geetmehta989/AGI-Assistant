import pytesseract
from PIL import Image
import os

def extract_text_from_image(image_path="screenshot.png"):
    """Extract text from image using OCR"""
    try:
        if not os.path.exists(image_path):
            print(f"Error: Image file '{image_path}' not found")
            return "Error: Screenshot not found"
        
        # Load image
        img = Image.open(image_path)
        
        # Extract text using pytesseract
        text = pytesseract.image_to_string(img)
        
        # Clean up the text (remove extra whitespace)
        text = ' '.join(text.split())
        
        if text:
            print(f"✓ OCR text extraction successful")
            return text
        else:
            print("No text detected in screenshot")
            return "No text detected"
            
    except Exception as e:
        print(f"Error during OCR extraction: {e}")
        return f"Error: {e}"

