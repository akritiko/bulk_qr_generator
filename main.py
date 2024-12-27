import segno
import csv
import os
from PIL import Image
import argparse

# Create output directory if not exists
output_dir = "qr_codes"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


def add_icon_to_qr(qr_code_path, icon_path, output_path):
    """
    Adds an icon to the center of a QR code image.
    """
    qr = Image.open(qr_code_path).convert("RGBA")
    icon = Image.open(icon_path).convert("RGBA")

    # Resize icon to 20% of the QR code size
    qr_width, qr_height = qr.size
    icon_size = int(qr_width * 0.2)
    icon = icon.resize((icon_size, icon_size), Image.LANCZOS)

    # Create a copy of the QR code to add the icon overlay
    qr_with_icon = qr.copy()
    icon_pos = ((qr_width - icon_size) // 2, (qr_height - icon_size) // 2)
    qr_with_icon.paste(icon, icon_pos, icon)
    qr_with_icon.save(output_path, format="PNG")


def generate_single_qr(url, icon_path, file_name):
    """
    Generates a single QR code with optional icon.
    """
    qr_file_path = os.path.join(output_dir, f"{file_name}.png")
    qr = segno.make(url)
    qr.save(qr_file_path, scale=30)

    if icon_path and os.path.exists(icon_path):
        output_path = os.path.join(output_dir, f"{file_name}.png")
        add_icon_to_qr(qr_file_path, icon_path, output_path)

    print(f"QR code '{file_name}.png' created successfully.")


def generate_from_csv(csv_file_path):
    """
    Generates multiple QR codes from a CSV file.
    """
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            url = row['url']
            icon_path = row.get('icon', '').strip()
            file_name = row['file name']
            generate_single_qr(url, icon_path, file_name)

    print("Bulk QR code generation complete.")


def main():
    """
    Command-line interface for QR code generation.
    """
    parser = argparse.ArgumentParser(description="QR Code Generator")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    # Sub-command for single QR code generation
    single_parser = subparsers.add_parser("single", help="Generate a single QR code")
    single_parser.add_argument("--url", required=True, help="The URL for the QR code")
    single_parser.add_argument("--icon", help="Path to the icon image file (optional)")
    single_parser.add_argument("--file_name", required=True, help="Output file name")

    # Sub-command for bulk QR code generation
    bulk_parser = subparsers.add_parser("bulk", help="Generate QR codes from a CSV file")
    bulk_parser.add_argument("--csv_file", required=True, help="Path to the CSV file")

    args = parser.parse_args()

    if args.command == "single":
        generate_single_qr(args.url, args.icon, args.file_name)
    elif args.command == "bulk":
        generate_from_csv(args.csv_file)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
