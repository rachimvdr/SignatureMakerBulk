import os
import random
from PIL import Image, ImageDraw, ImageFont

# Create a directory to store the signature images
output_dir = "signatures"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Signature parameters
names = [
    "Rika Purnama",
    "Evi Lestari",
    "Lia Suryani",
    "Coman Labis",
    "Jaiz Mahbubuddin",
    "Rayhan Aqil",
    "Nazir Qamar",
    "Haniyah Qanitah",
    "Ulfat Khalidah",
    "Ayu Anggraini",
    "Sari Anggraeni",
    "Ratih Susanti",
    "Zafirah Lalita",
    "Lamira Zainab",
    "Eka Wijaya",
    "Maulana Nugraha",
    "Ratna Kusuma",
    "Nailah Kanissa",
    "Thiflah Miqdamah",
    "Riana Anggraeni",
    "Zahra Daninsy Benazy",
    "Tasmirah Iftinan",
    "Zafran Atif",
    "Laela Safiyyah",
    "Ezaz Safiy",
    "Wira Pratama",
    "Tahiyyah Samiyah",
    "Daris Moazzam",
    "Iwan Hidayat",
    "Adlan Witha",
    "Rendy Prasetyo",
    "Eko Prasetyo",
    "Siti Mulyani",
    "Rina Cahyani",
    "Wira Setiawan",
    "Zhafiratul Muna",
    "Walidah Dzahiyah",
    "Hendrikus Prasetyo",
    "Qadhi Aun",
    "Yusuf Wibowo",
    "Ahmad Pratama",
    "Dicky Suharto",
    "Zahra Almaira Rahmani",
    "Dewi Permata",
    "Kenan El Amin",
    "Najib Ikram",
    "Yasmin Nafeeza",
    "Zahra Daninsy Benazy",
    "Arya Ramadhan",
    "Aldi Nugraha"
]  # Add more names as needed
num_signatures_per_name = 5  # Number of variations per name
font_path = r"C:\Users\Administrator\AppData\Local\Microsoft\Windows\Fonts\Creattion Demo.otf"  # Replace with the path to a cursive-style font
image_size = (400, 200)

# Function to generate a random signature
def generate_signature(name, font_size=50):  # Set a fixed font size
    # Create a blank image with a transparent background
    image = Image.new("RGBA", image_size, (0, 0, 0, 0))  # Use 'RGBA' for transparency
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype(font_path, font_size)
    except Exception as e:
        print(f"Font at {font_path} could not be loaded. Error: {e}")
        return None

    # Calculate text size using textbbox
    bbox = draw.textbbox((0, 0), name, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

    # Calculate x and y positions to center the text
    x = (image_size[0] - text_width) // 2
    y = (image_size[1] - text_height) // 2

    # Set text color to black
    color = (0, 0, 0)  # Black color

    # Draw the text
    draw.text((x, y), name, fill=color, font=font)

    return image

# Generate the signatures
for name in names:
    signature_image = generate_signature(name, font_size=50)
    if signature_image:
        filename = f"{output_dir}/{name.replace(' ', '_')}.png"  # Remove the index for single signature
        signature_image.save(filename)
        print(f"Saved signature: {filename}")