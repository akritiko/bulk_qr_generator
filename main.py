import segno
import csv
import os
from PIL import Image

# Create directory to store QR codes
output_dir = "qr_codes"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


def add_icon_to_qr(qr_code_path, icon_path, output_path):
    """
    Adds an icon to the center of a QR code image.

    Parameters:
    ----------
    qr_code_path : str
        The file path of the QR code image.
    icon_path : str
        The file path of the icon image to overlay.
    output_path : str
        The file path to save the QR code with the icon overlay.

    This function takes an existing QR code image and overlays an icon
    at the center of the QR code. The icon's size is resized to 20% of
    the QR code's width to ensure it fits properly while retaining the QR
    code's scannability. Transparency in the icon is preserved.
    """
    # Open the QR code image and convert it to RGBA mode
    qr = Image.open(qr_code_path).convert("RGBA")

    # Open the icon image and convert it to RGBA mode
    icon = Image.open(icon_path).convert("RGBA")

    # Resize the icon to 20% of the QR code size
    qr_width, qr_height = qr.size
    icon_size = int(qr_width * 0.2)
    icon = icon.resize((icon_size, icon_size), Image.LANCZOS)

    # Create a copy of the QR code to add the icon overlay
    qr_with_icon = qr.copy()
    icon_pos = ((qr_width - icon_size) // 2, (qr_height - icon_size) // 2)

    # Overlay the icon on the QR code
    qr_with_icon.paste(icon, icon_pos, icon)

    # Save the final QR code image with the icon
    qr_with_icon.save(output_path, format="PNG")


# Read the input CSV file and generate QR codes
input_csv = "input.csv"  # Path to the input CSV file containing QR code data
with open(input_csv, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Extract values from each row
        url = row['url']  # The URL for the QR code
        icon_path = row['icon']  # Path to the icon to overlay
        file_name = row['file name']  # Desired output file name

        # Generate the QR code and save it as a temporary file
        qr = segno.make(url)
        qr_file_path = os.path.join(output_dir, f"{file_name}.png")
        qr.save(qr_file_path, scale=30)  # Scale factor creates 3000x3000 px image

        # Add the icon to the QR code if the icon file exists
        if os.path.exists(icon_path):
            output_path = os.path.join(output_dir, f"{file_name}.png")
            add_icon_to_qr(qr_file_path, icon_path, output_path)
            # Optionally remove the plain QR code file after adding the icon
            # os.remove(qr_file_path)

print(f"QR codes saved in '{output_dir}' folder.")
