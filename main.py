import shutil
import os

print("Welcome to the Sorting program (Made by Abdullah)")
given_path=str(input("Which directory/folder do you want to sort: "))

# Defining all the folders to be created along with their extensions
folders = {
    "Pictures": (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".heic"),
    "Videos": (".mp4", ".mkv", ".mov", ".avi", ".flv", ".wmv", ".webm", ".mpeg", ".mpg", ".3gp"),
    "Audios": (".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a", ".aiff", ".alac"),
    "Documents": (".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".rtf", ".odt", ".csv"),
    "Applications": (".exe", ".msi", ".apk", ".bat", ".app", ".dmg", ".pkg", ".deb", ".rpm", ".sh"),
    "Archives": (".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso"),
    "Others": ()
}

# Making Folders for files in the directory
for folder in folders.keys():
    os.makedirs(os.path.join(given_path,folder), exist_ok=True)

# Listing all the files in the directory
all_files=os.listdir(given_path)

# Preventing this very script file from moving
this_file = os.path.basename(__file__)

for file in all_files:

    # Preventing this_file to be moved if it lies in the same directory that is to be sorted
    if file==this_file:
        continue

    # Checking the current_path for each file
    current_path=os.path.join(given_path,file)

    # Skips if the path of the file is already in a directory
    if os.path.isdir(current_path):
        continue    

    # Splitting and lowercasing the extension of the file 
    extension=os.path.splitext(file)[-1].lower()

    # Making sure that the file is a file, not a directory
    if os.path.isfile(current_path):

        # Variable declared to check if each file in the directory was moved in a folder or not 
        moved_status=False

        
        for folder, folder_extns in folders.items():
            ''' Will check each folder and in whichever folder the current file's extension lies it will move the
                #file in that folder '''
            if extension in folder_extns:
                new_path=os.path.join(given_path,folder,file)
                shutil.move(current_path,new_path)
                moved_status=True
                break
            
        # If the file was'nt moved in any of the folders in the folders dictionary
        if not moved_status:
            new_path=os.path.join(given_path,"Others",file)
            shutil.move(current_path,new_path)

    else:
        continue
    
print("Sorting done Successfully !")
print("Exiting ...")