from tkinter import *
from tkinter import filedialog
import json
import csv

back = "#0ABAB5"
base_font = ("comic sans", 20, "bold", "italic")

window = Tk()
window.geometry("800x800")
window.title("txt")

def open_file():
    file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("CSV Files", "*.csv"), ("JSON Files", "*.json")])
    if file:
        with open(file, "r") as reader:
            file_extension = file.split('.')[-1]
            if file_extension == "txt":
                text.delete(1.0, END)
                text.insert(1.0, reader.read())
            elif file_extension == "csv":
                reader = csv.reader(reader)
                content = "\n".join([", ".join(row) for row in reader])
                text.delete(1.0, END)
                text.insert(1.0, content)
            elif file_extension == "json":
                content = json.load(reader)
                text.delete(1.0, END)
                text.insert(1.0, json.dumps(content, indent=4))

def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("CSV Files", "*.csv"), ("JSON Files", "*.json")])
    if file:
        file_extension = file.split('.')[-1]
        with open(file, "w") as writer:
            if file_extension == "txt":
                writer.write(text.get(1.0, END))
            elif file_extension == "csv":
                writer = csv.writer(writer)
                rows = text.get(1.0, END).splitlines()
                for row in rows:
                    writer.writerow(row.split(", "))
            elif file_extension == "json":
                content = text.get(1.0, END)
                try:
                    json_content = json.loads(content)
                    json.dump(json_content, writer, indent=4)
                except json.JSONDecodeError:
                    writer.write(content)

    print("Saved file")

def exit_app():
    window.quit()

def new_window():
    new_win = Toplevel(window)

top_level_menubar = Menu(window)
window.config(menu=top_level_menubar)
filemenu = Menu(top_level_menubar, tearoff=0)
top_level_menubar.add_cascade(label="file", menu=filemenu)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="New window", command=new_window)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_app)


text = Text(window, font=base_font)
text.pack()

window.mainloop()
