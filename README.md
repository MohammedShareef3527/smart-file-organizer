<div align="center">

# Smart File Organizer

**A desktop app that sorts a messy folder into tidy category folders in one click.**

![Python](https://img.shields.io/badge/Python-0d1117?style=flat-square&logo=python&logoColor=3776AB)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-1f6feb?style=flat-square&labelColor=0d1117)
![Platform](https://img.shields.io/badge/platform-desktop-1f6feb?style=flat-square&labelColor=0d1117)

</div>

---

## Overview

Smart File Organizer is a Python desktop application with a dark-themed GUI. You pick a folder, press **Organize Files**, and every file in it is moved into a folder for its type: Images, PDFs, Documents, Videos, Audio, Archives or Others. The app then shows how many files went into each category and a log of every move.

The sorting logic lives in its own module (`organizer.py`), separate from the interface, and the repository keeps several iterations of the GUI that show how the design evolved.

## Problem Statement

Downloads and desktop folders quickly fill up with a mix of photos, PDFs, documents, videos and zip files. Sorting them by hand is slow and repetitive. This tool does it automatically and reports exactly what it did.

## Features

- **Folder picker** to choose the folder to organize
- **Automatic sorting by file extension** into seven categories:

  | Folder | Extensions |
  |---|---|
  | Images | `.jpg` `.jpeg` `.png` `.gif` `.bmp` |
  | PDFs | `.pdf` |
  | Documents | `.doc` `.docx` `.txt` `.ppt` `.pptx` `.xls` `.xlsx` |
  | Videos | `.mp4` `.avi` `.mov` `.mkv` |
  | Audio | `.mp3` `.wav` `.aac` |
  | Archives | `.zip` `.rar` `.7z` |
  | Others | anything else |

- **Creates category folders only when needed** and leaves existing sub-folders untouched
- **Statistics panel** with the number of files moved into each category
- **Activity log** listing every file and where it went
- **Progress bar and status messages** (Ready, Organizing, Complete)
- **Responsive interface**: sorting runs on a background thread, so the window doesn't freeze on large folders
- **Dark mode UI** built with CustomTkinter

The full feature set above is in `app_v2.py`. See [Project Structure](#project-structure) for what each GUI version contains.

## Tech Stack

- **Language:** Python 3
- **GUI:** CustomTkinter (built on Tkinter)
- **File handling:** `os`, `shutil`
- **Concurrency:** `threading`

## Project Structure

```text
smart-file-organizer/
├── organizer.py     # core logic: organize_folder() sorts files and returns statistics + activity log
├── app_v2.py        # full GUI: statistics, activity log, progress bar, background thread  ← recommended
├── app.py           # minimal GUI: browse, organize, status message
├── app_v1.py        # first GUI with a statistics panel
├── app_v3.py        # sidebar dashboard layout (UI design only, not connected to the organizer)
├── Test_Files/      # small sample files arranged by category
├── requirements.txt
└── .gitignore
```

## Installation and Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/MohammedShareef3527/smart-file-organizer.git
   cd smart-file-organizer
   ```
2. **Install the dependency** (Python 3 with Tkinter is required; it is included with the standard Windows and macOS installers)
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app**
   ```bash
   python app_v2.py
   ```
4. Click **Browse Folder**, choose a folder, then click **Organize Files**.

> **Try it on a copy first.** The app *moves* files. Test it on a copy of a folder, for example by copying a few files from `Test_Files/` into a new empty folder.

## Configuration

No setup or API keys are needed. To add or change categories, edit the `file_types` dictionary at the top of `organize_folder()` in `organizer.py`. Each key is a folder name and each value is a list of lower-case extensions. Add the same key to the `statistics` dictionary so it is counted.

## How It Works

1. `organize_folder(folder_path)` lists the files directly inside the chosen folder. Sub-folders are skipped, so it never moves folders or reaches into nested ones.
2. For each file it reads the extension in lower case and looks it up in the `file_types` dictionary.
3. It creates the matching category folder if it doesn't exist yet (`os.makedirs(..., exist_ok=True)`) and moves the file with `shutil.move`. Unknown extensions go to `Others`.
4. It counts each move in a `statistics` dictionary and records a line such as `✔ photo.png → Images` in an activity list, then returns both.
5. In `app_v2.py`, the **Organize Files** button starts `organize_folder()` on a background thread. When it finishes, the results are passed back to the main thread with `app.after()`, which updates the statistics labels, activity log and progress bar safely.

## Limitations

- Only the top level of the chosen folder is organized.
- If a file with the same name already exists in the destination category folder, the move may fail or replace it, depending on the operating system.
- There is no undo.

## Future Improvements

These are planned ideas, not current features:

- Rename duplicates automatically (for example `photo (1).png`) instead of overwriting
- Undo the last organization using the activity log
- Optional recursive mode for nested folders
- A settings screen to edit categories from the GUI, building on the `app_v3.py` layout
- Watch a folder and organize new files automatically
- Package the app as a Windows executable

## Learning Outcomes

- File-system automation with `os` and `shutil`
- Keeping business logic (`organizer.py`) separate from the user interface
- Building desktop GUIs with CustomTkinter
- Running long tasks on a background thread and updating Tkinter safely with `after()`
- Iterating on a UI design across versions

## Author

**Mohammed Shamsul Qhadri Shareef**
GitHub: [@MohammedShareef3527](https://github.com/MohammedShareef3527)
