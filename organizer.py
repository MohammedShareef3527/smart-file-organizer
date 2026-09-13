import os
import shutil


def organize_folder(folder_path):

    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "PDFs": [".pdf"],
        "Documents": [".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
        "Videos": [".mp4", ".avi", ".mov", ".mkv"],
        "Audio": [".mp3", ".wav", ".aac"],
        "Archives": [".zip", ".rar", ".7z"]
    }

    statistics = {
        "Images": 0,
        "PDFs": 0,
        "Documents": 0,
        "Videos": 0,
        "Audio": 0,
        "Archives": 0,
        "Others": 0
    }

    activity = []

    if not os.path.exists(folder_path):
        return statistics, activity

    files = os.listdir(folder_path)

    for file in files:

        source = os.path.join(folder_path, file)

        if os.path.isdir(source):
            continue

        extension = os.path.splitext(file)[1].lower()

        moved = False

        for category, extensions in file_types.items():

            if extension in extensions:

                destination_folder = os.path.join(folder_path, category)

                os.makedirs(destination_folder, exist_ok=True)

                destination = os.path.join(destination_folder, file)

                shutil.move(source, destination)

                statistics[category] += 1

                activity.append(f"✔ {file} → {category}")

                moved = True

                break

        if not moved:

            other_folder = os.path.join(folder_path, "Others")

            os.makedirs(other_folder, exist_ok=True)

            destination = os.path.join(other_folder, file)

            shutil.move(source, destination)

            statistics["Others"] += 1

            activity.append(f"✔ {file} → Others")

    return statistics, activity