import student_utils
import tkinter as tk

students = ["Anna", "Ivan", "Olha"]

def print_student(count):
    lines = []
    for name in students:
        grades = student_utils.generate_grades(count)
        average = student_utils.avarege_grade(grades)
        level = student_utils.get_level(average)
        lines.append(f"{name}: {grades} → {average:.2f} → {level}")
    return "\n".join(lines)


def on_click():
    value = entry.get()
    if not value.isdigit():
        report = "Помилка: введіть ціле число від 1 до 20."
    else:
        count = int(value)
        if count < 1 or count > 20:
            report = "Помилка: кількість оцінок має бути від 1 до 20."
        else:
            report = print_student(count)

    print(report)
    text.delete("1.0", tk.END)
    text.insert(tk.END, report)

root = tk.Tk()
root.title("Статистика Учнів")
root.geometry("300x300")
label = tk.Label(root, text="Введіть кількість оцінок (1-20):")
label.pack()
entry = tk.Entry(root)
entry.pack()
text = tk.Text(root, width=60, height=10)
button = tk.Button(root, text="Сформувати звіт", command=on_click)
button.pack()
text.pack()
root.mainloop()