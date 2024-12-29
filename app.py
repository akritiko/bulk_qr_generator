from flask import Flask, request, render_template, send_from_directory, redirect, url_for
from werkzeug.utils import secure_filename
from urllib.parse import quote
import os
import zipfile
from main import generate_single_qr, generate_from_csv

app = Flask(__name__)

# Configure upload and output folders
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_single', methods=['POST'])
def generate_single():
    url = request.form['url']
    file_name = request.form['file_name']
    icon_file = request.files.get('icon')

    icon_path = None
    if icon_file:
        icon_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(icon_file.filename))
        icon_file.save(icon_path)

    try:
        generate_single_qr(url, icon_path, file_name)
        qr_path = os.path.join(app.config['OUTPUT_FOLDER'], f"{file_name}.png")
        return render_template(
            'success.html',
            message="Your QR code has been generated successfully.",
            download_url=url_for('download_file', filename=f"{file_name}.png")
        )
    except Exception as e:
        return f"Error: {str(e)}", 400

@app.route('/generate_bulk', methods=['POST'])
def generate_bulk():
    csv_file = request.files.get('csv_file')
    if not csv_file:
        return "No CSV file provided", 400

    csv_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(csv_file.filename))
    csv_file.save(csv_path)

    try:
        # Extract file names from the CSV
        qr_files = extract_filenames_from_csv(csv_path)
        generate_from_csv(csv_path)

        # Create a ZIP containing only the relevant QR codes
        zip_file_path = create_zip(OUTPUT_FOLDER, app.config['OUTPUT_FOLDER'], 'qr_codes.zip', qr_files)
        return render_template(
            'success.html',
            message="Your QR codes have been generated successfully.",
            download_url=url_for('download_file', filename='qr_codes.zip')
        )
    except Exception as e:
        return f"Error: {str(e)}", 400

@app.route('/download/<filename>')
def download_file(filename):
    """
    Serve a file for download.
    """
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename, as_attachment=True)

def create_zip(source_folder, output_folder, zip_name, file_list):
    """
    Compress specified files in the source folder into a single zip file.
    """
    zip_path = os.path.join(output_folder, zip_name)
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file_name in file_list:
            file_path = os.path.join(source_folder, file_name)
            if os.path.exists(file_path):
                zipf.write(file_path, file_name)  # Use file_name as archive name
    return zip_path

def extract_filenames_from_csv(csv_path):
    """
    Extract the file names of QR codes to be generated from the CSV.
    """
    import csv
    file_names = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            file_names.append(f"{row['file name']}.png")
    return file_names

if __name__ == '__main__':
    app.run(debug=True)
