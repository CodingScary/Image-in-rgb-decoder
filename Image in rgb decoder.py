import os
from tkinter import filedialog
from tkinter import Tk
from PIL import Image

# Open File Explorer to select an image
root = Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

# Load the selected image
img = Image.open(file_path)

# Convert the image to the RGB code
rgb_data = img.convert("RGB").getdata()

# Create paths for the desktop and text file
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop_path, 'rgb_code.txt')

# Save the RGB code to a text file on the desktop
with open(file_path, 'w') as file:
    for pixel in rgb_data:
        file.write(f'{pixel}\n')

# Issue Confirmation
print("Successfully the RGB code has been saved to the desktop.")