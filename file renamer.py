import os
import tkinter as tk
from tkinter import filedialog, messagebox

__version__ = "1.1.0 @ vuthao.id.vn"

class FileRenamer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Renamer")

        # Directory selection
        self.directory_label = tk.Label(self, text="Thư mục file cần rename:")
        self.directory_label.grid(row=0, column=0, padx=10, pady=10)

        self.directory_entry = tk.Entry(self, width=50)
        self.directory_entry.grid(row=0, column=1, padx=10, pady=10)

        self.browse_button = tk.Button(self, text="Browse", command=self.browse_directory)
        self.browse_button.grid(row=0, column=2, padx=10, pady=10)

        # Character to delete
        self.character_label = tk.Label(self, text="Ký tự cần xoá trong tên file:")
        self.character_label.grid(row=1, column=0, padx=10, pady=10)

        self.character_entry = tk.Entry(self, width=20)
        self.character_entry.grid(row=1, column=1, padx=10, pady=10)

        # Rename button
        self.rename_button = tk.Button(self, text="Đổi tên file", command=self.delete_character)
        self.rename_button.grid(row=2, column=1, padx=10, pady=10)

        # Version label
        self.version_label = tk.Label(self, text=f"Version {__version__}")
        self.version_label.grid(row=3, column=1, padx=10, pady=10)

    def delete_character_from_filename(self, directory, character_to_delete):
        """
        Renames files in the specified directory by removing the given character from the filename.
        
        Args:
            directory (str): The path to the directory containing the files.
            character_to_delete (str): The character to be removed from the filenames.
        """
        try:
            for filename in os.listdir(directory):
                new_filename = filename.replace(character_to_delete, "")
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            messagebox.showinfo("Thành công", "Tên file đã được thay đổi.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi trong quá trình đổi tên tệp: {str(e)}")

    def browse_directory(self):
        """
        Opens a file dialog to allow the user to select a directory.
        """
        directory = filedialog.askdirectory()
        self.directory_entry.delete(0, tk.END)
        self.directory_entry.insert(0, directory)

    def delete_character(self):
        """
        Retrieves the directory and character to delete from the user interface, then calls the file renaming function.
        """
        directory = self.directory_entry.get()
        character_to_delete = self.character_entry.get()
        self.delete_character_from_filename(directory, character_to_delete)

def main():
    """
    The main entry point of the application.
    """
    app = FileRenamer()
    app.mainloop()

if __name__ == "__main__":
    main()
