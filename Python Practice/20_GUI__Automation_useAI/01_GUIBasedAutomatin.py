import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os

# -----------------------------
# GLOBAL VARIABLES
# -----------------------------
input_file = ""
output_folder = ""

# -----------------------------
# FILE BROWSING FUNCTIONS
# -----------------------------
def browse_input():
    global input_file
    input_file = filedialog.askopenfilename(
        filetypes=[("Excel Files", "*.xlsx *.xls")]
    )
    input_path_var.set(input_file)

def browse_output():
    global output_folder
    output_folder = filedialog.askdirectory()
    output_path_var.set(output_folder)

# -----------------------------
# RESET FUNCTIONS
# -----------------------------
def reset_paths():
    global input_file, output_folder
    input_file = ""
    output_folder = ""
    input_path_var.set("")
    output_path_var.set("")

def reset_checkboxes():
    remove_duplicates_var.set(0)
    remove_blank_rows_var.set(0)
    trim_spaces_var.set(0)
    title_case_var.set(0)

# -----------------------------
# DATA CLEANING FUNCTION
# -----------------------------
def clean_data():

    if not input_file or not output_folder:
        messagebox.showwarning(
            "Warning",
            "Please select Input File and Output Folder"
        )
        return

    try:
        df = pd.read_excel(input_file)

        # Remove Duplicate Rows
        if remove_duplicates_var.get():
            df = df.drop_duplicates()

        # Remove Blank Rows
        if remove_blank_rows_var.get():
            df = df.dropna(how="all")

        # Process TEXT Columns Only
        text_cols = df.select_dtypes(include="object").columns

        # Remove Leading/Trailing Spaces
        if trim_spaces_var.get():
            df[text_cols] = df[text_cols].apply(
                lambda col: col.str.strip()
            )

        # Title Case Conversion
        if title_case_var.get():
            df[text_cols] = df[text_cols].apply(
                lambda col: col.str.title()
            )

        # Output File Name
        filename = os.path.basename(input_file)
        output_path = os.path.join(
            output_folder,
            f"Cleaned_{filename}"
        )

        df.to_excel(output_path, index=False)

        messagebox.showinfo(
            "Success",
            f"Data Cleaned Successfully!\nSaved at:\n{output_path}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# -----------------------------
# GUI DESIGN
# -----------------------------
root = tk.Tk()
root.title("Dynamic Data Cleaning Automation")
root.geometry("600x450")

# Paths
input_path_var = tk.StringVar()
output_path_var = tk.StringVar()

# Checkbox Variables
remove_duplicates_var = tk.IntVar()
remove_blank_rows_var = tk.IntVar()
trim_spaces_var = tk.IntVar()
title_case_var = tk.IntVar()

# -----------------------------
# INPUT SECTION
# -----------------------------
tk.Label(root, text="Select Input Excel File").pack(pady=5)

tk.Entry(root, textvariable=input_path_var, width=60).pack()
tk.Button(root, text="Browse Input File",
          command=browse_input).pack(pady=5)

# -----------------------------
# OUTPUT SECTION
# -----------------------------
tk.Label(root, text="Select Output Folder").pack(pady=5)

tk.Entry(root, textvariable=output_path_var, width=60).pack()
tk.Button(root, text="Browse Output Folder",
          command=browse_output).pack(pady=5)

# -----------------------------
# CLEANING OPTIONS
# -----------------------------
tk.Label(root,
         text="Select Data Cleaning Options",
         font=("Arial", 12, "bold")).pack(pady=10)

tk.Checkbutton(root,
               text="Remove Duplicate Rows",
               variable=remove_duplicates_var).pack(anchor="w", padx=50)

tk.Checkbutton(root,
               text="Remove Blank Rows",
               variable=remove_blank_rows_var).pack(anchor="w", padx=50)

tk.Checkbutton(root,
               text="Trim Leading/Trailing Spaces (Text Columns)",
               variable=trim_spaces_var).pack(anchor="w", padx=50)

tk.Checkbutton(root,
               text="Convert Text Columns to Title Case",
               variable=title_case_var).pack(anchor="w", padx=50)

# -----------------------------
# BUTTONS
# -----------------------------
tk.Button(root,
          text="Clean Data",
          bg="green",
          fg="white",
          width=20,
          command=clean_data).pack(pady=15)

tk.Button(root,
          text="Reset Paths",
          width=20,
          command=reset_paths).pack(pady=5)

tk.Button(root,
          text="Reset Checkboxes",
          width=20,
          command=reset_checkboxes).pack(pady=5)

root.mainloop()