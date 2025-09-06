import tkinter as tk
from tkinter import filedialog, colorchooser, font, messagebox, simpledialog
from tkinter.scrolledtext import ScrolledText

class TextEditor:
    def __int__(self, root):
        self.root = root
        self.root.title("Untitled - Text Editor")
        self.filename = None
        
        self.current_font_family = "Consolas"
        self.current_font_size = 14
        self.text_font = font.Font(family=self.current_font_family, size=self.current_font_size)
        
        self.text_area = ScrolledText(root, wrap="word", font=self.text_font, undo=True)
        self.text_area.pack(expand=1, fill="both")
        self.text_area.focus_set()
        
        self.status_bar = tk.Label(root, text="Ln 1, Col 1", anchor="e")
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM)
        self.text_area.bind("<KeyRelease>", self.update_status)
        self.text_area.bind("<ButtonRelease>", self.update_status)
        
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)
        
        file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", accelarator="Ctrl+N", command=self.new_file)
        file_menu.add_command(label="Open", accelarator="Ctrl+O", command=self.open_file)
        file_menu.add_command(label="Save", accelarator="Ctrl+S", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        
        edit_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: self.text_area.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: self.text_area.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: self.text_area.event_generate("<<Paste>>"))
        
        