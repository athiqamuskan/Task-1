import os
folder_path = input("Enter the directory path: ")
if os.path.exists(folder_path):
    file_list = os.listdir(folder_path)
    counter = 1
    for fname in file_list:
        current_file = os.path.join(folder_path, fname)
        if os.path.isfile(current_file):
            ext = os.path.splitext(fname)[1]   # get file extension
            renamed_file = f"file_{counter}{ext}"
            new_location = os.path.join(folder_path, renamed_file)
            os.rename(current_file, new_location)
            print(f"Renamed: {fname} → {renamed_file}")  # shows old → new
            counter += 1
    print("\n All files have been renamed successfully!")
else:
    print("The given folder path does not exist.")
