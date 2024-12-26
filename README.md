
# Bulk QR Code Generator

This Python script generates QR codes from URLs listed in a CSV file and overlays custom icons at the center of each QR code. The resulting QR codes are saved as high-resolution PNG files.

## Features

- Generates QR codes from URLs with customizable filenames.
- Allows overlaying an icon image at the center of the QR code.
- Supports high-resolution QR codes (3000x3000 pixels).
- Maintains transparency of the icon and ensures the QR code remains scannable.

---

## Requirements

This project requires Python 3.7 or higher and the following Python libraries:

- **[Segno](https://pypi.org/project/segno/):** For generating QR codes.
- **[Pillow](https://pillow.readthedocs.io):** For handling image processing.

You can install the required libraries using:

```bash
pip install segno pillow
```

---

## File Structure

```plaintext
.
├── input.csv           # CSV file containing URLs, icons, and filenames
├── qr_codes/           # Folder where the generated QR codes are saved
├── qr_generator.py     # Main Python script
├── images/             # Folder containing images for README.md
└── README.md           # Project documentation
```

---

## Usage Instructions

### Step 1: Prepare the Input CSV File
Create a CSV file named `input.csv` (or update the script with your file name). The file should have the following structure:

| url                  | icon          | file name      |
|----------------------|---------------|----------------|
| https://example.com  | icon1.png     | example_qr     |
| https://another.com  | icon2.png     | another_qr     |

- **`url`**: The URL the QR code will link to.
- **`icon`**: File path to the icon image to overlay (must exist in the same directory or provide the full path).
- **`file name`**: Name for the generated QR code PNG file (without extension).

### Step 2: Place the Icon Images
Ensure all icon images referenced in the CSV file exist and are accessible. Icons should ideally be square-shaped for the best results.

### Step 3: Run the Script
Execute the Python script:

```bash
python qr_generator.py
```

### Step 4: Check the Output
The generated QR codes will be saved in a folder named `qr_codes`, located in the same directory as the script. Each QR code will be named according to the `file name` specified in the CSV file.

---

## Example Output

An example of a generated QR code with an icon:

<img src="images/example_qr_code.png" alt="drawing" style="width:200px;"/>

---

## Customization

### Change the QR Code Resolution
The script generates QR codes with a resolution of 3000x3000 pixels by default. You can modify the `scale` parameter in the script to adjust the resolution:

```python
qr.save(qr_file_path, scale=30)  # Default resolution
```

For example:
- `scale=20` generates 2000x2000 pixels.
- `scale=10` generates 1000x1000 pixels.

### Adjust Icon Size
The icon size is set to 20% of the QR code size by default. You can change this by modifying the following line in the `add_icon_to_qr` function:

```python
icon_size = int(qr_width * 0.2)  # Icon size as 20% of QR code size
```

---

## Error Handling

1. **File Not Found**: Ensure the input CSV file and referenced icon files exist in the specified paths.
2. **Invalid Image Format**: Only standard image formats (e.g., PNG, JPEG) are supported for icons.
3. **Invalid CSV Format**: Verify that the CSV file follows the required structure.

---

## Contributing

Contributions to improve this project are welcome! Feel free to fork the repository and submit a pull request with your changes.

---

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this code as you see fit. See the `LICENSE` file for more details.

---

## Acknowledgments

This project uses:
- [Segno](https://pypi.org/project/segno/) for QR code generation.
- [Pillow](https://pillow.readthedocs.io) for image processing.

Special thanks to the contributors and the open-source community for their tools and libraries.

---
