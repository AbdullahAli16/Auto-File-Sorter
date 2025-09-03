# 📂 Auto File Sorter

A Python script to automatically organize files in a given directory into categorized folders based on their extensions.  
No more messy "Downloads" folder — keep your files neatly sorted with one command 🚀.

---

## ✨ Features
- Automatically creates folders based on file types:
  - **Pictures** (`.jpg`, `.png`, `.gif`, etc.)
  - **Videos** (`.mp4`, `.mkv`, `.avi`, etc.)
  - **Audios** (`.mp3`, `.wav`, `.flac`, etc.)
  - **Documents** (`.pdf`, `.docx`, `.txt`, `.csv`, etc.)
  - **Applications** (`.exe`, `.apk`, `.msi`, etc.)
  - **Archives** (`.zip`, `.rar`, `.7z`, etc.)
  - **Others** (uncategorized files)
- Prevents moving the script file itself.
- Works on **Windows, Linux, and macOS**.
- Uses only Python’s built-in libraries.

---

## 🛠️ Requirements
- Python 3.x  
- Built-in libraries: `os`, `shutil`

---

## 🚀 Installation, Usage, and Example (single terminal)

```bash
=== STEP 1: Clone the repository ===
git clone https://github.com/yourusername/auto-file-sorter.git

=== STEP 2: Enter the project folder ===
cd auto-file-sorter

=== STEP 3: Run the script ===
python auto_file_sorter.py
Welcome to the Sorting program (Made by Abdullah)

=== STEP 4: Provide the directory to sort when prompted ===
Which directory/folder do you want to sort: C:\Users\YourName\Downloads

Sorting done Successfully !
Exiting ...

=== STEP 5: Example directory BEFORE sorting ===
Downloads/
├── song.mp3
├── picture.jpg
├── movie.mkv
├── notes.pdf
├── setup.exe

=== STEP 6: Example directory AFTER sorting ===
Downloads/
├── Audios/
│   └── song.mp3
├── Pictures/
│   └── picture.jpg
├── Videos/
│   └── movie.mkv
├── Documents/
│   └── notes.pdf
├── Applications/
│   └── setup.exe
```

## Contributing
Contributions, issues, and feature requests are welcome!
Feel free to fork the repo and submit a pull request.

## License
This project is licensed under the MIT License – you’re free to use and modify it.

## Author
Made with ❤️ by Abdullah