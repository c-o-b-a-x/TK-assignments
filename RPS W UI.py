import tkinter as tk
import random
 
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "Win"
    else:
        return "Loss"
 
def play_game():
    global player_choice
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
   
    if computer_choice == "Rock":
        computer_img = tk.PhotoImage(file="Resources/rock100.png")
    elif computer_choice == "Paper":
        computer_img = tk.PhotoImage(file="Resources/paper100.png")
    elif computer_choice == "Scissors":
        computer_img = tk.PhotoImage(file="Resources/scissors100.png")
   
    if player_choice == "Rock":
        player_img = tk.PhotoImage(file="Resources/rock100.png")
    elif player_choice == "Paper":
        player_img = tk.PhotoImage(file="Resources/paper100.png")
    elif player_choice == "Scissors":
        player_img = tk.PhotoImage(file="Resources/scissors100.png")
   
    computer_label.config(image=computer_img)
    computer_label.image = computer_img
    player_label.config(image=player_img)
    player_label.image = player_img
   
    result = determine_winner(player_choice, computer_choice)
   
    if result == "Win":
        score["Wins"] += 1
    elif result == "Loss":
        score["Losses"] += 1
    else:
        score["Ties"] += 1
 
    update_score_display()
 
def update_score_display():
    wins_label.config(text=f"Wins: {score['Wins']}")
    losses_label.config(text=f"Losses: {score['Losses']}")
    ties_label.config(text=f"Ties: {score['Ties']}")
 
def reset_game():
    global player_choice
    player_choice = None
 
    score["Wins"] = 0
    score["Losses"] = 0
    score["Ties"] = 0
   
 
    computer_img = tk.PhotoImage(file="Resources/tbd100.png")
    computer_label.config(image=computer_img)
    computer_label.image = computer_img
    player_label.config(image=computer_img)
    player_label.image = computer_img
   
 
    player_choice_var.set(None)
   
 
    update_score_display()
 
def update_player_choice():
    global player_choice
    if player_choice_var.get() == 1:
        player_choice = "Rock"
    elif player_choice_var.get() == 2:
        player_choice = "Paper"
    elif player_choice_var.get() == 3:
        player_choice = "Scissors"
 
window = tk.Tk()
window.title("Rock, Paper, Scissors")
window.geometry("400x400")
 
frame = tk.Frame(window)
frame.grid(row=0, column=0)
 
player_choice_var = tk.IntVar()
 
rock_button = tk.Radiobutton(frame, text="Rock", variable=player_choice_var, value=1, command=update_player_choice)
rock_button.grid(row=0, column=0)
 
paper_button = tk.Radiobutton(frame, text="Paper", variable=player_choice_var, value=2, command=update_player_choice)
paper_button.grid(row=0, column=1)
 
scissors_button = tk.Radiobutton(frame, text="Scissors", variable=player_choice_var, value=3, command=update_player_choice)
scissors_button.grid(row=0, column=2)
 
player_img = tk.PhotoImage(file="Resources/tbd100.png")
player_label = tk.Label(frame, image=player_img)
player_label.grid(row=1, column=0)
 
computer_img = tk.PhotoImage(file="Resources/tbd100.png")
computer_label = tk.Label(frame, image=computer_img)
computer_label.grid(row=1, column=2)

play_button = tk.Button(window, text="Play", command=play_game)
play_button.grid(row=1, column=0)
 
score = {"Wins": 0, "Losses": 0, "Ties": 0}
 
frame_score = tk.Frame(window)
frame_score.grid(row=2, column=0, columnspan=3)
 
wins_label = tk.Label(frame_score, text="Wins: 0")
wins_label.grid(row=2, column=0)
 
losses_label = tk.Label(frame_score, text="Losses: 0")
losses_label.grid(row=2, column=1)
 
ties_label = tk.Label(frame_score, text="Ties: 0")
ties_label.grid(row=2, column=2)
 
reset_button = tk.Button(window, text="Reset Scores", command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)
 
player_choice = None

window.mainloop()