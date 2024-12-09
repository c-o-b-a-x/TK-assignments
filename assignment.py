import tkinter as tk
from tkinter import messagebox

def show_message():
    band = entry.get()

    genres = []
    if rock.get():
        genres.append("Rock")
    if pop.get():
        genres.append("Pop")
    if jazz.get():
        genres.append("Jazz")
    
    genres_str = ", ".join(genres) if genres else "None"
    
    method = vote.get() if vote.get() else "Not selected"

    response = messagebox.showinfo("Your Preferences", f"Favorite Artist / Band: {band}\nFavorite Genres: {genres_str}\nPreferred Listening Method: {method}")

window = tk.Tk()
base_font = ("comic sans", 20, "bold", "italic")
back = "#0ABAB5"
window.geometry("600x1200")
window.configure(bg=back)
window.title("My Music Preferences")

title = tk.Label(window, bg=back, font=base_font, text="Welcome to My Music Preferences")
title.pack()

label = tk.Label(window, pady=50, bg=back, font=base_font, text="Who is your favorite artist or band?")
label.pack()
entry = tk.Entry(bg=back, font=base_font)
entry.pack()

genres = tk.Label(window, pady=25, bg=back, font=base_font, text="Select your favorite music genres")
genres.pack()

rock = tk.IntVar()
checkbox_rock = tk.Checkbutton(window, pady=10, text="Rock", variable=rock, bg=back, font=base_font)
checkbox_rock.pack(anchor="w")

pop = tk.IntVar()
checkbox_pop = tk.Checkbutton(window, text="Pop", pady=10, variable=pop, bg=back, font=base_font)
checkbox_pop.pack(anchor="w")

jazz = tk.IntVar()
checkbox_jazz = tk.Checkbutton(window, text="Jazz", pady=10, variable=jazz, bg=back, font=base_font)
checkbox_jazz.pack(anchor="w")

method = tk.Label(window, bg=back, font=base_font, text="Choose your preferred listening method:")
method.pack()

vote = tk.StringVar()

tk.Radiobutton(window, text="Streaming", variable=vote, value="Streaming", font=base_font, bg=back).pack(anchor="w")
tk.Radiobutton(window, text="CDs", variable=vote, value="CDs", font=base_font, bg=back).pack(anchor="w")
tk.Radiobutton(window, text="Vinyl", variable=vote, value="Vinyl", font=base_font, bg=back).pack(anchor="w")

btn = tk.Button(window, text="Submit", command=show_message, bg=back, font=base_font)
btn.pack(pady=20)





window.mainloop()
