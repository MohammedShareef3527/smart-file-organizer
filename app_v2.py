import customtkinter as ctk
from tkinter import filedialog, messagebox
from organizer import organize_folder
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Smart File Organizer Pro")
app.geometry("1000x700")

selected_folder = ""

# -----------------------------
# Functions
# -----------------------------
def browse_folder():
    global selected_folder
    folder = filedialog.askdirectory()
    if folder:
        selected_folder = folder
        folder_label.configure(text=folder)
        status.configure(text="🟢 Folder Selected")
        textbox.insert("end", f"Selected: {folder}\n")
        textbox.see("end")

def run_organizer():
    if not selected_folder:
        messagebox.showwarning("No Folder", "Please select a folder first.")
        return
    threading.Thread(target=organize_task, daemon=True).start()

def organize_task():
    app.after(0, lambda: (
        progress.set(0.2),
        status.configure(text="🟡 Organizing...")
    ))
    try:
        statistics, activity = organize_folder(selected_folder)

        def update_ui():
            progress.set(1)
            status.configure(text="✅ Organization Complete")

            images_label.configure(text=f"🖼 Images : {statistics['Images']}")
            pdfs_label.configure(text=f"📄 PDFs : {statistics['PDFs']}")
            docs_label.configure(text=f"📝 Documents : {statistics['Documents']}")
            videos_label.configure(text=f"🎥 Videos : {statistics['Videos']}")
            audio_label.configure(text=f"🎵 Audio : {statistics['Audio']}")
            archives_label.configure(text=f"🗜 Archives : {statistics['Archives']}")
            others_label.configure(text=f"📁 Others : {statistics['Others']}")

            textbox.delete("1.0", "end")
            textbox.insert("end", "Organization Complete!\n\n")
            for line in activity:
                textbox.insert("end", line + "\n")
            textbox.see("end")
        app.after(0, update_ui)
    except Exception as e:
        app.after(0, lambda: messagebox.showerror("Error", str(e)))

# -----------------------------
# Main Container
# -----------------------------
main = ctk.CTkFrame(app, corner_radius=15)
main.pack(fill="both", expand=True, padx=20, pady=20)

header = ctk.CTkFrame(main, corner_radius=15)
header.pack(fill="x", pady=(10,20))
ctk.CTkLabel(header,text="📂 Smart File Organizer Pro",font=("Arial",34,"bold")).pack(pady=20)

folder_frame = ctk.CTkFrame(main, corner_radius=15)
folder_frame.pack(fill="x", pady=10)
ctk.CTkLabel(folder_frame,text="📁 Selected Folder",font=("Arial",18,"bold")).pack(pady=(10,5))
folder_label = ctk.CTkLabel(folder_frame,text="No Folder Selected",font=("Arial",15))
folder_label.pack(pady=(0,15))

dashboard = ctk.CTkFrame(main, fg_color="transparent")
dashboard.pack(fill="both", expand=True, pady=10)

stats = ctk.CTkFrame(dashboard, width=250, corner_radius=15)
stats.pack(side="left", fill="both", padx=(0,10), expand=True)
ctk.CTkLabel(stats,text="📊 Statistics",font=("Arial",20,"bold")).pack(pady=15)

images_label = ctk.CTkLabel(stats,text="🖼 Images : 0",font=("Arial",16)); images_label.pack(pady=5)
pdfs_label = ctk.CTkLabel(stats,text="📄 PDFs : 0",font=("Arial",16)); pdfs_label.pack(pady=5)
docs_label = ctk.CTkLabel(stats,text="📝 Documents : 0",font=("Arial",16)); docs_label.pack(pady=5)
videos_label = ctk.CTkLabel(stats,text="🎥 Videos : 0",font=("Arial",16)); videos_label.pack(pady=5)
audio_label = ctk.CTkLabel(stats,text="🎵 Audio : 0",font=("Arial",16)); audio_label.pack(pady=5)
archives_label = ctk.CTkLabel(stats,text="🗜 Archives : 0",font=("Arial",16)); archives_label.pack(pady=5)
others_label = ctk.CTkLabel(stats,text="📁 Others : 0",font=("Arial",16)); others_label.pack(pady=5)

log = ctk.CTkFrame(dashboard, corner_radius=15)
log.pack(side="left", fill="both", expand=True)
ctk.CTkLabel(log,text="📝 Activity Log",font=("Arial",20,"bold")).pack(pady=15)
textbox = ctk.CTkTextbox(log,width=400,height=250)
textbox.pack(padx=15,pady=10)
textbox.insert("end","Application Started...\n")

ctk.CTkLabel(main,text="Progress",font=("Arial",18,"bold")).pack(pady=(10,5))
progress = ctk.CTkProgressBar(main)
progress.pack(fill="x", padx=20)
progress.set(0)

button_frame = ctk.CTkFrame(main, fg_color="transparent")
button_frame.pack(pady=20)

browse_btn = ctk.CTkButton(button_frame,text="📂 Browse Folder",width=180,command=browse_folder)
browse_btn.pack(side="left", padx=10)

organize_btn = ctk.CTkButton(button_frame,text="⚡ Organize Files",width=180,command=run_organizer)
organize_btn.pack(side="left", padx=10)

status = ctk.CTkLabel(main,text="🟢 Ready",font=("Arial",18))
status.pack(pady=10)

app.mainloop()
