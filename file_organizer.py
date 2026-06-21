import os
import shutil
from tkinter import *
from tkinter import filedialog, messagebox

def organize_files():
    folder_path = entry.get()
    
    if not folder_path:
        messagebox.showerror("Error", "Pehle folder select karo!")
        return
    
    
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".xlsx"],
        "Videos": [".mp4", ".mkv",".mov"],
        "Music": [".mp3"],
        "Others": []
    }
    
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        
        if os.path.isfile(file_path):
            moved = False
            
            for folder_name, extensions in file_types.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    
                    dest_folder = os.path.join(folder_path, folder_name)
                    os.makedirs(dest_folder, exist_ok=True)   
                    
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    print(f"Moved: {filename} → {folder_name}")
                    moved = True
                    break
            
            if not moved:
                others_folder = os.path.join(folder_path, "Others")
                os.makedirs(others_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(others_folder, filename))
                print(f"Moved: {filename} → Others")
    
    messagebox.showinfo("Success", "Files organize ho gaye!")

root = Tk()
root.title("Mera File Organizer")
root.geometry("600x400")
root.configure(bg="#2c3e50")

Label(root, text="Advanced File Organizer", font=("Arial", 16, "bold"), bg="#2c3e50", fg="white").pack(pady=20)

Label(root, text="Folder Select Karo:", bg="#2c3e50", fg="white", font=("Arial", 12)).pack(pady=10)

entry = Entry(root, width=60, font=("Arial", 10))
entry.pack(pady=5)

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        entry.delete(0, END)
        entry.insert(0, folder)

Button(root, text="Browse Folder", command=browse_folder, bg="#3498db", fg="white", font=("Arial", 10), width=15).pack(pady=10)

Button(root, text="Organize Files Now", command=organize_files, bg="#2ecc71", fg="white", font=("Arial", 12, "bold"), height=2, width=25).pack(pady=30)


root.mainloop()