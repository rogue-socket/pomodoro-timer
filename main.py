import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
TICK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SESSIONS = -1
STOPWATCH = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global SESSIONS
    window.after_cancel(STOPWATCH)
    timer_label.config(text="Timer")
    SESSIONS = -1
    tick_label.config(text="")
    canvas.itemconfig(timer, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start():
    global SESSIONS
    SESSIONS += 1
    if SESSIONS % 2 == 0:
        timer_work()
    elif SESSIONS % 7 == 0:
        long_break()
    else:
        short_break()


def timer_work():
    count = WORK_MIN * 60
    timer_label.config(text="WORK!", fg=RED)
    count_down(count)
    return 1


def short_break():
    count = SHORT_BREAK_MIN * 60
    timer_label.config(text="SHORT-BREAK", fg=PINK)
    count_down(count)
    tick_label.config(text=((SESSIONS // 2) + 1) * TICK)
    return 1


def long_break():
    count = LONG_BREAK_MIN * 60
    timer_label.config(text="lONG-BREAK", fg=PINK)
    count_down(count)
    tick_label.config(text=((SESSIONS // 2) + 1) * TICK)
    return 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    secs = count % 60
    if secs < 10:
        secs = f"0{secs}"
    canvas.itemconfig(timer, text=f"{count // 60}:{secs}")
    if count > 0:
        global STOPWATCH
        STOPWATCH = window.after(1000, count_down, count - 1)
    else:
        start()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(bg=YELLOW)
window.minsize(width=400, height=400)
window.config(padx=60, pady=20)

canvas = tk.Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)

tomato = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

timer_label = tk.Label(text="Timer")
timer_label.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
timer_label.grid(row=0, column=1)

start_button = tk.Button(text="Start", command=start)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text="Reset", command=reset)
reset_button.grid(row=2, column=2)

tick_label = tk.Label(bg=YELLOW, fg="Green")
tick_label.grid(row=3, column=1)

window.mainloop()
