import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
tic_count = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global tic_count

    window.after_cancel(timer)
    tic_count = 0
    canva.itemconfig(main_text, text="25:00")
    tic_label.config(text="")



# ---------------------------- TIMER MECHANISM ------------------------------- #


def set_timer():
    global tic_count
    tic_count += 1

    if tic_count != 0:
        tic = "✓"
        if tic_count % 8 == 0:
            count_down(LONG_BREAK_MIN * 60)
        elif tic_count % 2 == 0:
            count_down(SHORT_BREAK_MIN * 60)
        else:
            count_down(WORK_MIN*60)

        tic_label.config(text=tic)
        tic += " ✓"


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
        min = count//60
        sec = count - min * 60
        if sec//10 == 0:
            canva.itemconfig(main_text, text=f"{min}:0{sec}")
        else:
            canva.itemconfig(main_text, text=f"{min}:{sec}")


# ---------------------------- UI SETUP ------------------------------- #
# window part
window = tk.Tk()
window.title("pomodoro")
window.minsize(width=600, height=500)
window.config(padx=100, pady=50, bg=PINK)


# canva part(uploaded image)
canva = tk.Canvas(width=400, height=350, bg=YELLOW, highlightthickness=1)
tomato_img = tk.PhotoImage(file="pomodoro.png")
canva.create_image(200, 200, image=tomato_img)
main_text = canva.create_text(200, 300, text="25:00", font=(FONT_NAME, 20, "bold"))
canva.place(x=0, y=0)


# button part
def action1():
    set_timer()


button1 = tk.Button(text="Start", command=action1, bg=RED, fg="white", relief="raised", font=("Helvetica", 12), padx=10)
button1.place(x=90, y=380)


def action2():
    reset_timer()


button2 = tk.Button(text="Reset", command=action2, bg=RED, fg="white", relief="raised", font=("Helvetica", 12), padx=10)
button2.place(x=250, y=380)


tic_label = tk.Label(text="")
tic_label.place(x=145, y=320)
tic_label.config(bg="white", fg=GREEN, font=("Helvetica", 14))


window.mainloop()