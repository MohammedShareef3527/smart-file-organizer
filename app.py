import customtkinter as ctk
from tkinter import filedialog
from organizer import organize_folder

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("Smart File Organizer Pro")

app.geometry("800x600")

header_frame = ctk.CTkFrame(
    app,
    corner_radius=15
)

header_frame.pack(
    fill="x",
    padx=20,
    pady=20
)

selected_folder = ""


def browse_folder():

    global selected_folder

    folder = filedialog.askdirectory()

    if folder:
        selected_folder = folder
        folder_label.configure(text=folder)


def organize():

    if selected_folder == "":
        status_label.configure(
            text="⚠ Please select a folder first!"
        )
        return

    moved = organize_folder(selected_folder)

    status_label.configure(
        text=f"✅ Successfully organized {moved} files!"
    )


title = ctk.CTkLabel(
    header_frame,
    text="📂 Smart File Organizer Pro",
    font=("Arial", 30, "bold")
)

title.pack(pady=25)

folder_label = ctk.CTkLabel(
    app,
    text="No Folder Selected",
    font=("Arial", 16)
)

folder_label.pack(pady=15)

browse_btn = ctk.CTkButton(
    app,
    text="Browse Folder",
    command=browse_folder,
    width=220,
    height=45
)

browse_btn.pack(pady=10)

organize_btn = ctk.CTkButton(
    app,
    text="Organize Files",
    command=organize,
    width=220,
    height=45,
    fg_color="green"
)

organize_btn.pack(pady=20)

status_label = ctk.CTkLabel(
    app,
    text="Ready",
    font=("Arial", 18)
)

status_label.pack(pady=30)

app.mainloop()