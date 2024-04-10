import os, shutil, pathlib
from pathlib import Path
from shutil import move

if __name__ == "__main__":
    # Path to folder
    os.chdir(r"")

    # Create folders
    folders = [
        "Pictures",
        "Audio",
        "Videos",
        "Installer",
        "Fonts",
        "Compressed",
        "Documents",
        "Others",
    ]

    # Make sure all the folders exist
    for folder in folders:
        Path(folder).mkdir(exist_ok=True)

    for file in os.listdir():
        try:
            # Move files to respective folders based on extension
            if file.endswith((".jpg", ".png", ".jpeg")):
                shutil.move(file, "Pictures")
            elif file.endswith((".mp3", ".wav")):
                shutil.move(file, "Audio")
            elif file.endswith((".mp4", ".wmv", ".mkv")):
                shutil.move(file, "Videos")
            elif file.endswith((".ttf", ".TTF", ".otf")):
                shutil.move(file, "Fonts")
            elif file.endswith((".exe", ".rar", "msi")):
                shutil.move(file, "Installer")
            elif file.endswith(".zip"):
                shutil.move(file, "Compressed")
            elif file.endswith((".pdf", ".docx")):
                destination = "Documents"
                dest_file = os.path.join(destination, file)
                # check for duplicate files
                if os.path.exists(dest_file):
                    filename, file_extension = os.path.splitext(file)
                    new_file = f"{filename}(dup){file_extension}"
                    shutil.move(file, os.path.join(destination, new_file))
                else:
                    shutil.move(file, destination)
            else:
                # Handling files with other extensions
                if os.path.isfile(file):
                    shutil.move(file, "Others")
        # Error handling
        except PermissionError as e:
            print(f"PermissionError: {e}")
