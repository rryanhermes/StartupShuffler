import cv2
import easyocr
import re

# Initialize EasyOCR reader with English language support
reader = easyocr.Reader(['en'])

# Load the video
video_path = '/Users/ryanhermes/Desktop/Screen Recording 2024-09-29 at 10.06.49 PMcopy 2 (online-video-cutter.com).mp4'
cap = cv2.VideoCapture(video_path)

# List to store the detected URLs
detected_urls = []

# Function to preprocess image for better OCR
def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply adaptive thresholding to improve contrast
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 11, 2)
    return thresh

# Function to validate if detected text resembles a URL
def is_valid_url(text):
    # Basic regex pattern for URL-like text
    pattern = r"(www\.|http|https|\.com|\.io|\.ai|\.net)"
    return re.search(pattern, text, re.IGNORECASE) is not None

# Process frames
frame_interval = 60  # Process every 60th frame
frame_number = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Process every 60th frame
    if frame_number % frame_interval == 0:
        # Crop to the region where URLs are likely located
        # (adjust coordinates based on your video layout)
        height, width, _ = frame.shape
        url_region = frame[int(height*0.1):int(height*0.9), int(width*0.3):int(width*0.7)]
        
        # Preprocess the cropped image
        processed_image = preprocess_image(url_region)
        
        # Perform OCR
        result = reader.readtext(processed_image)
        
        # Extract and validate URLs from OCR result
        for detection in result:
            text = detection[1]
            if is_valid_url(text):
                # Clean up the URL text
                cleaned_text = re.sub(r"[^a-zA-Z0-9\.\-\/]", "", text)
                detected_urls.append(cleaned_text)
            print(cleaned_text)
    
    frame_number += 1

# Release video capture object
cap.release()

# Print all unique detected URLs
for url in set(detected_urls):
    print(url)
