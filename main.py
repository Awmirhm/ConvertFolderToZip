import os
from zipfile import ZipFile
from ttkbootstrap import Window, Frame, Label, Entry, Button, DARK, SUCCESS, INFO, OUTLINE, END
from ttkbootstrap.dialogs import Messagebox
from tkinter.filedialog import askdirectory

# Global
folder_address = None

# Create Window
page = Window(themename="cyborg", title="Convert Folder To Zip", iconphoto="photo\\zip-folder_12217671.png")
page.grid_rowconfigure(0, weight=1)
page.grid_columnconfigure(0, weight=1)
page.geometry(f"{1000}x{600}")
page.minsize(width=1000, height=600)

# Create Frame
frame = Frame(page)
frame.grid_columnconfigure(1, weight=1)
frame.grid(row=0, column=0, sticky="nsew")

# Choice Folder
folder_label = Label(frame, text="Folder Path :")
folder_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

folder_entry = Entry(frame, bootstyle=DARK)
folder_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")


def folder_button_clicked():
    global folder_address
    folder_address = askdirectory()
    folder_entry.insert(0, folder_address)


folder_button = Button(frame, text="Choice your Folder", bootstyle=INFO + OUTLINE, command=folder_button_clicked)
folder_button.grid(row=1, column=1, padx=(0, 10), pady=(10, 10))

# Choice Address For Saving Convert
zip_label = Label(frame, text="Zip Address :")
zip_label.grid(row=2, column=0, padx=(10, 10), pady=(10, 10))

zip_entry = Entry(frame, bootstyle=DARK)
zip_entry.grid(row=2, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")


# Convert Folder To Zip
def convert_zip_button_clicked():
    global folder_address
    zip_convert = zip_entry.get()
    if not folder_address:
        Messagebox.show_error(title="Error", message="PLease Choice your Folder")
    else:
        if not zip_convert.endswith(".zip"):
            Messagebox.show_error(title="Error", message=f"Your Address Invalid\nEX : {folder_address}.zip")
        else:
            with ZipFile(zip_convert, mode="w") as zip_file:
                for directory, directories, files in os.walk(folder_address):
                    for file in files:
                        full_path = os.path.join(directory, file)
                        relative_path = os.path.relpath(full_path, folder_address)
                        zip_file.write(full_path, relative_path)
            Messagebox.ok(title="Save", message="Your folder has been successfully converted to zip")


convert_zip_button = Button(frame, text="Convert To Zip", bootstyle=SUCCESS + OUTLINE,
                            command=convert_zip_button_clicked)
convert_zip_button.grid(row=3, column=1, padx=(0, 10), pady=(10, 10))

page.mainloop()
