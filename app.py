import streamlit as st
import numpy as np
import cv2
from PIL import Image
import os

# Install required packages using pip
os.system('pip install pytesseract')
os.system('apt-get update && apt-get install -y tesseract-ocr')
import pytesseract

def load_image(image_file):
    """Load an image file and convert it to an OpenCV image"""
    img = Image.open(image_file)
    return np.array(img)

def process_image(image):
    """Process image with OCR and draw boxes around detected text"""
    # Convert image to RGB if it's not
    if len(image.shape) == 2:  # Grayscale
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    elif image.shape[2] == 4:  # RGBA
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    
    # Make a copy for drawing
    display_image = image.copy()
    
    try:
        # Get bounding boxes
        results = pytesseract.image_to_boxes(image)
        
        # Get image dimensions
        ih, iw = image.shape[:2]
        
        detected_text = []
        
        # Draw boxes and text
        for box in results.splitlines():
            box = box.split(' ')
            if len(box) >= 5:
                char, x, y, w, h = box[0], int(box[1]), int(box[2]), int(box[3]), int(box[4])
                
                # Draw rectangle
                cv2.rectangle(display_image, (x, ih-y), (w, ih-h), (0, 255, 0), 2)
                # Put text
                cv2.putText(display_image, char, (x, ih-h), 
                           cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
                detected_text.append(char)
        
        return display_image, ''.join(detected_text)
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None, None

def main():
    st.title("OCR Text Detection App")
    
    st.write("""
    Upload an image to detect and extract text using OCR.
    The app will highlight detected characters and show the extracted text.
    """)
    
    image_file = st.file_uploader("Upload Image", type=['jpg', 'jpeg', 'png'])
    
    if image_file is not None:
        try:
            # Display original image
            image = load_image(image_file)
            st.subheader("Original Image")
            st.image(image, channels="RGB")
            
            if st.button("Detect Text"):
                with st.spinner("Processing image..."):
                    # Process the image
                    result_image, detected_text = process_image(image)
                    
                    if result_image is not None:
                        # Display processed image
                        st.subheader("Processed Image")
                        st.image(result_image, channels="RGB")
                        
                        # Display detected text
                        st.subheader("Detected Text")
                        if detected_text:
                            st.text(detected_text)
                        else:
                            st.warning("No text was detected in the image.")
                    
        except Exception as e:
            st.error(f"Error processing image: {str(e)}")

if __name__ == "__main__":
    main()
