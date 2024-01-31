import tkinter as tk
from tkinter import filedialog
from PIL import Image
import pytesseract
import os
import glob

# Install:
# https://github.com/UB-Mannheim/tesseract
# https://tesseract-ocr.github.io/tessdoc/Installation.html
# https://tesseract-ocr.github.io/tessdoc/Downloads.html
# https://sourceforge.net/projects/tesseract-ocr-alt/files/
# https://sourceforge.net/projects/tesseract-ocr-alt/files/tesseract-ocr-setup-3.02.02.exe/download
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Use your actual installation path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# Function to perform OCR on an image and save the text
def ocr_on_image(image_path, output_path):
    try:
        # Open the image
        img = Image.open(image_path)
        # Perform OCR
        text = pytesseract.image_to_string(img)
        # Write the extracted text
        with open(output_path, 'w') as file:
            file.write(text)
        return text
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return ""

# Main function to process all images in the selected folder
def process_images_in_folder():
    # Set up a Tkinter dialog window
    root = tk.Tk()
    root.withdraw()

    # Ask the user to select a folder
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return

    # Print the selected folder path for verification
    print("Selected folder:", folder_path)

    # Prepare to write all text to a single file
    total_text = []
    total_file_path = os.path.join(folder_path, 'total.txt')

    # Define a list of image file extensions
    image_extensions = ['png', 'jpg', 'jpeg', 'bmp', 'gif', 'tiff']

    # Iterate over all image files in the folder
    for extension in image_extensions:
        for image_path in glob.glob(os.path.join(folder_path, f'*.{extension}')):
            print("Processing:", image_path)  # Print the path of each image being processed
            # Construct the output file path
            base_name = os.path.splitext(os.path.basename(image_path))[0]
            output_path = os.path.join(folder_path, f"{base_name}_ocr.txt")
            
            # Perform OCR and save the text
            text = ocr_on_image(image_path, output_path)
            total_text.append(text)

    # When opening the file for writing, specify the encoding as UTF-8
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)

# Run the main function
process_images_in_folder()
