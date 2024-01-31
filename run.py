import tkinter as tk
from tkinter import filedialog
from PIL import Image
import pytesseract
import os
import glob

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

    # Save all extracted texts in 'total.txt'
    with open(total_file_path, 'w') as file:
        file.writelines(total_text)

# Run the main function
process_images_in_folder()
