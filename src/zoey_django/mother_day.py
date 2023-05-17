import tkinter as tk
import pygame
import random


class MothersDayGame:
    def __init__(self, master):
        self.master = master
        master.title("Mother's Day Game")
        self.score = 0
        # Load the background music
        pygame.mixer.init()
        pygame.mixer.music.load('demo.mp3')  # replace to your music clip
        pygame.mixer.music.play(-1)  # play the music in a loop

        # Create a label for the game instructions
        self.instruction_text = tk.Label(master, text="Click on the heart!")  # more message to your mom
        self.instruction_text.pack(pady=200)

        # Create a button for the heart to be clicked
        self.button = tk.Button(master, text="❤", font=('Modern', 40), command=self.increment_score)
        self.button.pack(pady=200)

        # Create a label for the score
        self.score_label = tk.Label(master, text="Score: {}".format(self.score))
        self.score_label.pack(pady=200)

        # Create a timer
        self.time_left = 30
        self.timer_label = tk.Label(master, text="Timer: {}".format(self.time_left), font=('Modern', 20))
        self.timer_label.pack(pady=200)
        self.timer_function()

    def increment_score(self):
        self.score += 1
        self.score_label.configure(text="Score: {}".format(self.score))

    def timer_function(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.configure(text="Timer: {}".format(self.time_left))
            self.master.after(1000, self.timer_function())  # 1000ms ==> 1s
            # this timer_function will call timer_function over and over every 1 second
        else:
            self.instruction_text.configure(text="Game Over!")
            self.score_label.configure(text="Final Score: {}".format(self.score))
            self.button.destroy()


master = tk.Tk()  # similar to turtle.Turtle()
game = MothersDayGame(master)
master.mainloop()
