import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
base_font = ("comic sans", 20, "bold", "italic")
back = "#0ABAB5"
window.geometry("600x1200")
window.configure(bg=back)
window.title("Event Planner")

def show_message():
    name = entry.get()
    num_of_guests = scale.get()
    theme = listbox.get(tk.ACTIVE)
    genres = []
    if catering.get():
        genres.append("Catering")
    if music.get():
        genres.append("Provide Music ")
    if streaming.get():
        genres.append("Online Streaming")
    
    genres_str = ", ".join(genres) if genres else "None"
    
    method = type.get() if type.get() else "Not selected"

    response = messagebox.showinfo("Your Event", f"Event Name: {name}\nPreferences: {genres_str}\nEvent Type:{method}\nNumber Of Guests:{num_of_guests}\nEvent Theme: {theme}")

def reset_fields():
    entry.delete(0, tk.END)
    scale.set(0)
    listbox.select_set(0)
    catering.set(0)
    music.set(0)
    streaming.set(0)
    type.set("")
    
title = tk.Label(window, bg=back, font=base_font, text="Plan Your Event ")
title.pack()

label = tk.Label(window, pady=25, bg=back, font=base_font, text="Enter the Event Name ")
label.pack()

entry = tk.Entry(bg=back, font=base_font)
entry.pack()

preferences = tk.Label(window, pady=12, bg=back, font=base_font, text="Select Preferences:")
preferences.pack()

catering = tk.IntVar()
checkbox_catering = tk.Checkbutton(window, pady=5, text="Include catering", variable=catering, bg=back, font=base_font)
checkbox_catering.pack(anchor="w")

music = tk.IntVar()
checkbox_music = tk.Checkbutton(window, text="Provide music", pady=5, variable=music, bg=back, font=base_font)
checkbox_music.pack(anchor="w")

streaming = tk.IntVar()
checkbox_streaming = tk.Checkbutton(window, text="Enable Online streaming", pady=5, variable=streaming, bg=back, font=base_font)
checkbox_streaming.pack(anchor="w")

eventtype = tk.Label(window, pady=25, bg=back, font=base_font, text="Select Event Type:")
eventtype.pack()

type = tk.StringVar()

tk.Radiobutton(window, text="Wedding", variable=type, value="Wedding", font=base_font, bg=back).pack(anchor="w")
tk.Radiobutton(window, text="Conference", variable=type, value="Conference", font=base_font, bg=back).pack(anchor="w")
tk.Radiobutton(window, text="Birthday Party", variable=type, value="Birthday Party", font=base_font, bg=back).pack(anchor="w")

guests = tk.Label(window, pady=25, bg=back, font=base_font, text="Number Of Guests:")
guests.pack()

scale = tk.Scale(window, from_=0, to=500, length=400, bg=back, orient="horizontal", tickinterval=50, highlightthickness=0)
scale.pack()

theme = tk.Label(window, pady=25, bg=back, font=base_font, text="Select Event Theme:")
theme.pack()

listbox = tk.Listbox(window, width=25, height=8, bg=back, font=base_font)
listbox.pack()
listbox.insert(1, "Modern")
listbox.insert(2, "Classic")
listbox.insert(3, "Rustic")
listbox.insert(4, "Futuristic")
listbox.select_set(0)

btn_submit = tk.Button(window, text="Submit", command=show_message, bg=back, font=base_font)
btn_submit.pack()

btn_reset = tk.Button(window, text="Reset", command=reset_fields, bg=back, font=base_font)
btn_reset.pack()

window.mainloop()
