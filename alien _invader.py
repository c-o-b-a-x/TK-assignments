import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox

window = tk.Tk()
window.geometry("600x650")
window.configure(bg="#0ABAB5")
window.title("Alien Invader HQ Control Panel")

base_font = ("Comic Sans", 32, "bold", "italic")
background_color = "#0ABAB5"
status_message = tk.StringVar()
status_message.set("Ready...")

top_frame = tk.Frame(window, bg=background_color)
top_frame.grid(row=0, column=0, columnspan=2, pady=20)

alien_label = tk.Label(top_frame, text="👽", font=base_font, bg=background_color)
alien_label.pack(side=tk.TOP)

middle_frame = tk.Frame(window, bg=background_color)
middle_frame.grid(row=1, column=0, columnspan=2, pady=20)

spaceship_label = tk.Label(middle_frame, text="Spaceship Display", bg="gray", width=30, height=5)
spaceship_label.grid(row=0, column=0)

def change_spaceship_color():
    color = colorchooser.askcolor()[1]
    if color:
        spaceship_label.config(bg=color)
        status_message.set(f"Color changed to {color}")

spaceship_color_btn = tk.Button(middle_frame, text="Change Spaceship Color", command=change_spaceship_color, font=("Arial", 12), bg=background_color, fg="white")
spaceship_color_btn.grid(row=0, column=1)

status_label = tk.Label(window, textvariable=status_message, font=("Arial", 12), bg=background_color)
status_label.grid(row=2, column=0, columnspan=2, pady=20)

message_label = tk.Label(window, text="Message Alien Pilots:", font=("Arial", 12), bg=background_color)
message_label.grid(row=3, column=0)

message_text = tk.Text(window, width=40, height=5, font=("Arial", 12))
message_text.grid(row=3, column=1)

def send_message():
    message = message_text.get("1.0", tk.END).strip()
    if message:
        print(f"Alien Message: {message}")
        status_message.set("Message sent to Alien Pilots!")

send_message_btn = tk.Button(window, text="Send Message", command=send_message, font=("Arial", 12), bg=background_color, fg="white")
send_message_btn.grid(row=4, column=0, columnspan=2, pady=20)

def upload_secret_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                file_content = file.read()
            print(f"File Name: {file_path}")
            print(f"File Content:\n{file_content}")
            status_message.set(f"File '{file_path}' uploaded successfully!")
        except Exception as e:
            status_message.set(f"Error reading file: {e}")

upload_file_btn = tk.Button(window, text="Upload Secret File", command=upload_secret_file, font=("Arial", 12), bg=background_color, fg="white")
upload_file_btn.grid(row=5, column=0, columnspan=2, pady=20)


plan_label = tk.Label(window, text="Select Invasion Plan:", font=("Arial", 12), bg=background_color)
plan_label.grid(row=6, column=0)

listbox = tk.Listbox(window, width=25, height=8, bg=background_color,font=("Arial", 12))
listbox.insert(1, "Plan A: Earth Takeover")
listbox.insert(2, "Plan B: Moon Domination")
listbox.insert(3, "Plan C: Mars Colonization")
listbox.select_set(0)
listbox.grid(row=6, column=1)

def launch_plan():
    selected_plan = listbox.get(tk.ACTIVE)
    if messagebox.askyesno("Confirm Launch", f"Are you sure you want to launch {selected_plan}?"):
        messagebox.showinfo("Launch Confirmed", f"{selected_plan} launched!")
        status_message.set(f"{selected_plan} launched!")
    else:
        messagebox.showinfo("Launch Aborted", "Launch Aborted!")
        status_message.set("Launch Aborted!")

plan_btn = tk.Button(window, text="Launch Plan", command=launch_plan, font=("Arial", 12), bg=background_color, fg="white")
plan_btn.grid(row=7, column=0, columnspan=2, pady=20)


quit_btn=tk.Button(window,text="QUIT",command=quit,bg=background_color)
quit_btn.grid(row=8, column=0, columnspan=2, pady=20)
window.mainloop()

