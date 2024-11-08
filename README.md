# OCR Text Detection App

This is a simple Optical Character Recognition (OCR) web app built with **Streamlit** and **OpenCV** that allows users to upload images and detect text within them. The app highlights detected text characters in the uploaded image and displays the extracted text below the image.

## Features

- Upload an image (`.jpg`, `.jpeg`, or `.png`).
- Detect text within the image and draw bounding boxes around each detected character.
- Display both the processed image with highlights and the extracted text.

## Requirements

- **Python 3.x**
- Required packages are installed within the script using `pip`.

## Setup

To run this app, you need to have **Streamlit**, **OpenCV**, **Pillow**, and **pytesseract** installed.

1. Clone or download this repository.

2. Navigate to the project directory.

3. Run the following commands to install the dependencies (if not installed already):

    ```bash
    pip install streamlit numpy opencv-python-headless pillow pytesseract
    ```

4. Ensure **Tesseract OCR** is installed on your system. The app installs it using:

    ```bash
    apt-get update && apt-get install -y tesseract-ocr
    ```

## How to Use

1. Start the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Upload an image file (`.jpg`, `.jpeg`, or `.png`) in the provided upload area.

3. Click **"Detect Text"** to process the image. 

4. The app will display:
   - The original image.
   - The processed image with bounding boxes around detected characters.
   - The detected text in the output section.

## Code Overview

- `load_image(image_file)`: Loads and converts an uploaded image into a format suitable for processing.
- `process_image(image)`: Detects text using Tesseract OCR, draws bounding boxes around each detected character, and extracts text.
- `main()`: The main function for the Streamlit app, which sets up the UI and triggers the image processing.

## Screenshots

### Input Image
![image](https://github.com/user-attachments/assets/c24e8d55-a74e-4a0d-ad2f-ceda702e6f86)

![image](https://github.com/user-attachments/assets/826e5cfc-50d4-4be5-a04e-ee836420355f)



### Output - Processed Image with Detected Text
![image](https://github.com/user-attachments/assets/f436cd74-2189-4f29-a479-14bd1b3dcdf0)


## Acknowledgements

- **[Streamlit](https://streamlit.io/)** - For building interactive data apps.
- **[OpenCV](https://opencv.org/)** - For image processing.
- **[Tesseract OCR](https://github.com/tesseract-ocr/tesseract)** - For text detection.

## License

This project is licensed under the MIT License.
