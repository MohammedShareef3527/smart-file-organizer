import customtkinter as ctk

# -----------------------------
# App Settings
# -----------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Smart File Organizer Pro")
app.geometry("1400x800")
app.minsize(1200, 700)
# -----------------------------
# Main Container
# -----------------------------
main = ctk.CTkFrame(app, fg_color="#1f1f1f")
main.pack(fill="both", expand=True)
# -----------------------------
# Sidebar
# -----------------------------
sidebar = ctk.CTkFrame(
    main,
    width=230,
    corner_radius=0,
    fg_color="#252526"
)

sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)
logo = ctk.CTkLabel(
    sidebar,
    text="📂",
    font=("Arial", 42)
)

logo.pack(pady=(30, 10))

title = ctk.CTkLabel(
    sidebar,
    text="Smart File\nOrganizer",
    font=("Arial", 22, "bold"),
    justify="center"
)

title.pack()
buttons = [
    "🏠 Dashboard",
    "📂 Browse Folder",
    "⚡ Organize",
    "📜 Activity",
    "⚙ Settings",
    "ℹ About"
]

for item in buttons:
    btn = ctk.CTkButton(
        sidebar,
        text=item,
        height=45,
        anchor="w"
    )
    btn.pack(fill="x", padx=15, pady=6)
    app.mainloop() 