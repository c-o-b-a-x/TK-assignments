import tkinter as tk
import math
import time

# Create the main window
root = tk.Tk()
root.title("Wave Effect with Clock")

# Set the window size to the screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")  # Set window size to full screen
root.config(bg="white")  # Set the overall background to white (for the area above the wave)

# Create a canvas to draw the wave
canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg="white", bd=0, highlightthickness=0)
canvas.pack()
canvas.create_rectangle(0, screen_height / 2, screen_width, screen_height, fill="black", outline="black", tags="background")

# Wave parameters (adjusted for visibility)
amplitude = 100  # Increased amplitude for better visibility
frequency = 0.03  # Adjusted frequency for a more noticeable wave
speed = 3  # Increased speed for a faster-moving wave
offset = 0  # Offset to shift the wave horizontally
drawn_up_to = 0  # Variable to keep track of how much of the wave has been drawn

# Function to draw the flipped black wave (now in the bottom half)
def draw_top_wave():
    global offset, drawn_up_to
    
    # Clear the canvas (optional: if you want to clear it every time)
    canvas.delete("top_wave")
    
    # Loop to draw the wave incrementally
    points = []
    # Draw the wave from the beginning to the current drawn position
    for x in range(drawn_up_to):  
        y = amplitude * math.sin(frequency * (x + offset)) + screen_height / 2 + amplitude  # Center around the middle (bottom half)
        if y > screen_height / 2:  # Only draw in the bottom half
            points.append(x)
            points.append(y)

    # Only draw the wave if there are points
    if points:
        # Always black when in the bottom half
        canvas.create_line(points, fill="black", width=10, tags="top_wave")

    # Update the wave's horizontal offset and the drawn position
    offset += speed
    drawn_up_to += speed  # Slowly increase the drawn_up_to value
    if drawn_up_to > screen_width:  # Allow the wave to smoothly scroll horizontally
        drawn_up_to = screen_width  # Limit the drawn_up_to value to the screen width

    # Redraw the top wave at a certain interval (50 milliseconds)
    root.after(50, draw_top_wave)

# Function to draw the bottom wave (white wave, only in the top half)
def draw_bottom_wave():
    global offset, drawn_up_to
    
    # Clear the canvas (optional: if you want to clear it every time)
    canvas.delete("bottom_wave")
    
    # Loop to draw the wave incrementally
    points = []
    # Draw the wave from the beginning to the current drawn position
    for x in range(drawn_up_to):  
        y = amplitude * math.sin(frequency * (x + offset)) + screen_height / 2 - amplitude  # Center around the middle (top half)
        if y < screen_height / 2:  # Only draw in the top half
            points.append(x)
            points.append(y)

    # Only draw the wave if there are points
    if points:
        # Always white when in the top half
        canvas.create_line(points, fill="white", width=10, tags="bottom_wave")

    # Redraw the bottom wave at a certain interval (50 milliseconds)
    root.after(50, draw_bottom_wave)

# Function to update the clock
def update_clock():
    current_time = time.strftime("%H:%M:%S")  # Get current time in HH:MM:SS format
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)  # Update clock every second

# Create the clock label at the top center of the screen
clock_label = tk.Label(root, font=("Helvetica", 30), bg="#f0f0f0", fg="black")
clock_label.place(relx=0.5, rely=0.05, anchor="center")

# Start drawing the waves and updating the clock
draw_top_wave()  # Black wave now at the bottom
draw_bottom_wave()  # White wave at the top
update_clock()

# Run the Tkinter event loop
root.mainloop()
