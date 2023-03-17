import tkinter as tk
from tkinter import ttk


class PomodoroApp:
    def __init__(self, master):
        self.master = master
        master.title("Pomodoro App")
        master.geometry("500x500")

        # Add background image
        try:
            self.background_image = tk.PhotoImage(file="pomodoro.png")
            self.background_label = tk.Label(master, image=self.background_image)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        except:
            print("exception")

        # Add timer label and buttons
        self.timer_label = tk.Label(master, text="25:00", font=("Arial", 20), bg="white")
        self.start_button = ttk.Button(master, text="Start", command=self.start_timer, style="my.TButton")
        self.reset_button = ttk.Button(master, text="Reset", command=self.reset_timer, style="my.TButton")

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("my.TButton", padding=5, relief="flat",
                        font=("Arial", 14), foreground="black", background="light blue",
                        borderwidth=0)

        style.map("my.TButton", background=[('active', '#f9b208'), ('!disabled', 'light blue')])
        style.map("my.TButton", foreground=[('pressed', 'white'), ('active', 'black')])

        # Place timer label and buttons on top of the background image
        self.timer_label.place(relx=0.5, rely=0.75, anchor="center")
        self.start_button.place(relx=0.3, rely=0.85, anchor="center")
        self.reset_button.place(relx=0.7, rely=0.85, anchor="center")

        self.timer_running = False
        self.paused = False
        self.minutes = 25
        self.seconds = 0

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.start_button.config(text="Pause")
            self.countdown()
        else:
            self.timer_running = False
            self.paused = True
            self.start_button.config(text="Resume")

    def reset_timer(self):
        self.timer_running = False
        self.paused = False
        self.minutes = 25
        self.seconds = 0
        self.timer_label.config(text="25:00")
        self.start_button.config(text="Start")

    def countdown(self):
        if self.timer_running:
            if self.seconds == 0:
                if self.minutes == 0:
                    self.timer_running = False
                    self.start_button.config(text="Start")
                else:
                    self.minutes -= 1
                    self.seconds = 59
            else:
                self.seconds -= 1
            self.timer_label.config(text=f"{self.minutes:02d}:{self.seconds:02d}")
            self.master.after(1000, self.countdown)
        elif self.paused:
            self.start_button.config(text="Resume")
            self.paused = False


root = tk.Tk()
app = PomodoroApp(root)
root.mainloop()


