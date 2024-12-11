from tkinter import *
from gif import ImageLabel
import math
from pygame import mixer


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
my_timer = 0
reps = 0
# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global status
    global timer
    global reps
    bg.after_cancel(my_timer)
    status.config(text='Idle...', font=(FONT_NAME, 15, 'bold'), bg='black', fg='white')
    timer.config(text=f'00:00', font=(FONT_NAME, 35, 'bold'), bg='black', fg='red')
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start():
    global reps
    global check_label
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps == 9:
        reset()
    elif reps % 2 != 0:
        countdown(work_sec)
        status.config(text='Grind Mode Baby!',font=(FONT_NAME, 15, 'bold'), bg='black', fg='orange')
    elif reps == 8:
        countdown(long_break_sec)
        sound.play()
        status.config(text='Chill Mode', font=(FONT_NAME, 15, 'bold'), bg='black', fg='green')
        all_checks.append(check)
        check_label.config(text=all_checks, bg='black', fg='green')

    elif reps % 2 == 0:
        countdown(short_break_sec)
        sound.play()
        status.config(text='Chill Mode', font=(FONT_NAME, 15, 'bold'), bg='black', fg='green')
        all_checks.append(check)
        check_label.config(text=all_checks, bg='black', fg='green')
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# minutes = 25
# seconds = 00
def countdown(count):
    global my_timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    timer.config(text=f'{count_min}:{count_sec}',)
    if count > 0:
        my_timer = bg.after(1000, countdown, count -1)

    if count == 0:
        start()
# ---------------------------- UI SETUP ------------------------------- #
##GIF
bg = Tk()
lbl = ImageLabel(bg, borderwidth=0, highlightthickness=0)
bg.title('PEPE POMODORO TIMER')
lbl.grid(column=1,row=1)
lbl.load('_internal/data/dj-pepe-black-small-crop.gif')
bg.config(bg='black', padx=5)
bg.resizable(False, False)

#Start Button
start_button = Button(text='Start', command=start)
start_button.grid(column=0, row=3)

#Reset Button
reset_button = Button(text='Reset', command=reset )
reset_button.grid(column=2, row=3)

#Status Label
status = Label(text='Idle...',font=(FONT_NAME, 15, 'bold'), bg='black',fg='white')
status.grid(column=1,row=0)

#Timer Label
timer = Label(text=f'00:00', font=(FONT_NAME, 35, 'bold'), bg='black', fg='red')
timer.grid(column=1,row=3)

#Checkmarks
check = ['✅']
all_checks = []
check_label = Label(text=all_checks, font=('', 10, 'bold'))
check_label.grid(column=1,row=4)
check_label.config(bg='black',fg='green')

## SFX
mixer.init()
sound = mixer.Sound("_internal/data/El-Pepe.mp3")

##MAIN LOOP
bg.mainloop()

