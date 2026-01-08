import tkinter as tk
import random

# this is currently not working as images are not loading properly
imagedict = {
    1: "dice1.png",
    2: "dice2.png",
    3: "dice3.png",
    4: "dice4.png",
    5: "dice5.png",
    6: "dice6.png",
}

# create a roll_dice function which will do all the function and we attach it to the button using result_label
def roll_dice():
    dice_roll_1 = random.randint(1, 6)
    dice_roll_2 = random.randint(1, 6)
    result_label_1.config(text=f"You rolled a {dice_roll_1} and {dice_roll_2}")
    result_label_2.config(text=f"And there sum is {dice_roll_1 + dice_roll_2}")
    image_label_1.config(image=imagedict[dice_roll_1])
    image_label_2.config(image=imagedict[dice_roll_2])

root = tk.Tk()
root.title("Dice Rolling Simulator")   # title of the window
root.geometry("600x400")   # size of the window

roll_button = tk.Button(root, text="Roll Dice", font=("Arial", 16), command=roll_dice)
roll_button.pack(pady=20)  # this function adds roll button to the application

image_label_1 = tk.Label(root, image="")
image_label_1.pack(pady=20)  

image_label_2 = tk.Label(root, image="")
image_label_2.pack(pady=20)  

result_label_1 = tk.Label(root, text="", font=("Arial", 16))
result_label_1.pack(pady=20)  

result_label_2 = tk.Label(root, text="", font=("Arial", 16))
result_label_2.pack(pady=20)  

root.mainloop()  # this function runs the application