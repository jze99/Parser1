import tkinter as tk
from tkinter import filedialog
from XMLparser import xml_parser
from upload import *

def open_xml_file(event):
    file_path = filedialog.askopenfilename(filetypes=(("XML files", "*.xml"), ("All files", "*.*")))
    first_entry.delete(0, tk.END)
    first_entry.insert(0, file_path)

def open_file_or_directory(event):
    if radio_var.get() == "file":
        file_path = filedialog.askopenfilename(filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*")))
    else:
        file_path = filedialog.askdirectory()
        
    second_entry.delete(0, tk.END)
    second_entry.insert(0, file_path)

def empty_method():
    if first_entry.get() != "" and second_entry.get() != "" :
            empty_button.config(state=tk.DISABLED)
            if xml_parser.Parsing(pathXML=first_entry.get()) == True:
                if radio_var.get() == "file":
                    if uploadPath(file_path= second_entry.get(), directory_file="") == True:
                        empty_button.config(state=tk.NORMAL)
                if radio_var.get() != "file":
                    if uploadPath(file_path= "", directory_file=second_entry.get()) == True:
                        empty_button.config(state=tk.NORMAL)
    

def radio_changed():
    if radio_var.get() == "file":
        second_label.config(text="Выбранный файл XLSX:")
    else:
        second_label.config(text="Выбранная директория:")

root = tk.Tk()
root.title("Parser1")

font = ("Arial", 12)
root.configure(bg="#B85C38")
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

first_label = tk.Label(root, text="Выбранный файл XML:", font=font)
first_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

first_entry = tk.Entry(root, font=font)
first_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
first_entry.bind("<Button-1>", open_xml_file)

second_label = tk.Label(root, text="Выбранный файл XLSX:", font=font)
second_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

second_entry = tk.Entry(root, font=font)
second_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
second_entry.bind("<Button-1>", open_file_or_directory)

radio_var = tk.StringVar(value="file")

radio_file = tk.Radiobutton(root, text="Выбрать файл XLSX", variable=radio_var, value="file", command=radio_changed, font=font)
radio_file.grid(row=2, column=0, padx=10, pady=10, sticky="w")

radio_dir = tk.Radiobutton(root, text="Выбрать директорию", variable=radio_var, value="directory", command=radio_changed, font=font)
radio_dir.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# Добавим кнопку в правый верхний угол
empty_button = tk.Button(root, text="->", command=empty_method, font=font)
empty_button.grid(row=3, column=1, padx=10, pady=10, sticky="ne")

root.mainloop()