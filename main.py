import tkinter as tk
import random

window = tk.Tk()
window.title("MATEMATYCZNY NINJA")
window.geometry("400x300")
window.configure(bg="#4F6048")
window.grid_columnconfigure(0, weight=1)

title = tk.Label(window, text="🥷 Matematyczny Ninja", font=("Arial", 22, "bold"), bg="#4F6048")
title.grid(row=0, column=0, pady=20)
etykieta = tk.Label(window, text="Witaj w grze!", font=("Arial", 20), bg="#4F6048")
etykieta.grid(row=1, column=0)



correct_answer = 0
points = 0

points_label = tk.Label(
    window,
    text=f"Punkty: {points}",
    bg="#4F6048",
    font=("Arial", 14, "bold")
)
points_label.grid(row=7, column=0, pady=10)

def points_add():
    global points
    points += 1


def start_game():
    global correct_answer
    title.destroy()
    etykieta.destroy()
    start_button.destroy()

    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    operation = random.choice(["+", "-"])

    if operation == "+":
        correct_answer = number1 + number2
    else:
        if number1 < number2:
            number1, number2 = number2, number1
        correct_answer = number1 - number2

    exer_text = tk.Label(
        window,
        text="Ile to jest?",
        font=("Arial", 14, "bold"),
        bg="#4F6048"
    )
    exer_text.grid(row=0, column=0, pady=10)

    math = tk.Label(
        window,
        text=f"{number1} {operation} {number2} = ?",
        font=("Arial", 24, "bold"),
        bg="#4F6048"
    )
    math.grid(row=3, column=0, pady=15)

    answer = tk.Entry(window, font=("Arial", 16))
    answer.grid(row=4, column=0, pady=10)

    result_label = tk.Label(
        window,
        text="",
        bg="#4F6048",
        font=("Arial", 14, "bold")
    )
    result_label.grid(row=6, column=0, pady=10)

    check_button = tk.Button(
        window,
        text="SPRAWDŹ",
        command=lambda: check_answer(answer, result_label, math),
        font=("Arial", 14, "bold"),
        padx=20,
        pady=10,
        bg="#6B7D5A",
        highlightthickness=0,
        relief="flat",
        bd=0
    )
    check_button.grid(row=5, column=0, pady=10)



start_button = tk.Button(
    window,
    text="START",
    command=start_game,
    font=("Arial", 14, "bold"),
    padx=20,
    pady=10,
    bg="#6B7D5A",
    relief="flat",
    bd=0,
    highlightthickness=0
)
start_button.grid(row=2, column=0, pady=(15, 10))

def check_answer(answer, result_label, math):
    global correct_answer
    user_answer = int(answer.get())

    if user_answer == correct_answer:
        result_label.config(text="🎉 SUPER")
        points_add()
        points_label.config(text=f"Punkty: {points}")
        correct_answer = new_question(math)
    else:
        result_label.config(text="❌ BŁĄD! Spróbuj jeszcze raz.")

def new_question(math):
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    operation = random.choice(["+", "-"])

    if operation == "+":
        correct_answer = number1 + number2
    else:
        if number1 < number2:
            number1, number2 = number2, number1
        correct_answer = number1 - number2

    math.config(text=f"{number1} {operation} {number2} = ?")

    return correct_answer






window.mainloop()