from PIL import Image
from pytesseract import pytesseract
import cv2

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"E:\textextractorfromimage\jfkjf.jpg"

# Load the image using OpenCV
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Save the preprocessed image
preprocessed_image_path = r"E:\textextractorfromimage\preprocessed_image.jpg"
cv2.imwrite(preprocessed_image_path, binary)

# Open the preprocessed image with PIL
img = Image.open(preprocessed_image_path)

pytesseract.tesseract_cmd = path_to_tesseract

# Use Tesseract with custom configuration
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img, config=custom_config)

# Correct common OCR errors
corrected_text = text.replace("|", "I").replace("deh", "John")
print(corrected_text[:-1])
