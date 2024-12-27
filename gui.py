import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from main2 import generate_single_qr, generate_from_csv

def create_single_qr():
    """
    GUI logic for creating a single QR code.
    """
    url = url_entry.get().strip()
    icon_path = icon_var.get()
    file_name = file_name_entry.get().strip()

    if not url or not file_name:
        messagebox.showerror("Error", "URL and file name are required.")
        return

    try:
        generate_single_qr(url, icon_path, file_name)
        messagebox.showinfo("Success", f"QR code '{file_name}.png' created successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate QR code. {str(e)}")

def create_multiple_qrs():
    """
    GUI logic for creating multiple QR codes from a CSV file.
    """
    csv_file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if not csv_file_path:
        return

    try:
        generate_from_csv(csv_file_path)
        messagebox.showinfo("Success", "QR codes generated successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate QR codes. {str(e)}")

# Main GUI window
root = tk.Tk()
root.title("QR Code Generator")

# Tab control
tab_control = ttk.Notebook(root)
single_tab = ttk.Frame(tab_control)
batch_tab = ttk.Frame(tab_control)

tab_control.add(single_tab, text="Single QR Code")
tab_control.add(batch_tab, text="Batch QR Codes")
tab_control.pack(expand=1, fill="both")

# Single QR Code Tab
tk.Label(single_tab, text="URL:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
url_entry = tk.Entry(single_tab, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(single_tab, text="Icon Path:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
icon_var = tk.StringVar()
icon_button = tk.Button(single_tab, text="Browse", command=lambda: icon_var.set(filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])))
icon_button.grid(row=1, column=2, padx=5, pady=5)

icon_label = tk.Label(single_tab, textvariable=icon_var, width=40, anchor="w")
icon_label.grid(row=1, column=1, padx=5, pady=5)

tk.Label(single_tab, text="File Name:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
file_name_entry = tk.Entry(single_tab, width=50)
file_name_entry.grid(row=2, column=1, padx=5, pady=5)

generate_button = tk.Button(single_tab, text="Generate QR Code", command=create_single_qr)
generate_button.grid(row=3, column=0, columnspan=3, pady=10)

# Batch QR Codes Tab
batch_label = tk.Label(batch_tab, text="Generate multiple QR codes from a CSV file.")
batch_label.pack(pady=10)

batch_button = tk.Button(batch_tab, text="Select CSV File and Generate", command=create_multiple_qrs)
batch_button.pack(pady=20)

# Start GUI loop
root.mainloop()
