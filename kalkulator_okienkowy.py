from tkinter import *
import math

def klikniecie(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def rownanie():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except (SyntaxError, NameError, TypeError):
        equation_label.set("cos ty odwalil")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("tak sie nie dzieli debilu")
        equation_text = ""

def oblicz_pierwiastek():
    global equation_text
    try:
        wynik = str(math.sqrt(float(eval(equation_text))))
        equation_label.set(wynik)
        equation_text = wynik
    except Exception:
        equation_label.set("ty jestes upo chyba")
        equation_text = ""

def oblicz_kwadrat():
    global equation_text
    try:
        wynik = str(float(eval(equation_text)) ** 2)
        equation_label.set(wynik)
        equation_text = wynik
    except Exception:
        equation_label.set("ty jestes upo chyba")
        equation_text = ""

def oblicz_log2():
    global equation_text
    try:
        wynik = str(math.log2(float(eval(equation_text))))
        equation_label.set(wynik)
        equation_text = wynik
    except Exception:
        equation_label.set("ty jestes upo chyba")
        equation_text = ""

def wyczysc():
    global equation_text
    equation_label.set("")
    equation_text = ""

window = Tk()
window.title("Brutalny kalkulator")
window.geometry("1000x1200")
window.resizable(False, False)
window.configure(bg="black") 

equation_text = ""
equation_label = StringVar()

frame = Frame(window, bg="black")
frame.pack(pady=20)

label = Label(frame, textvariable=equation_label, font=('Times New Roman', 18), bg="black", fg="white", width=31, height=1)
label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

button_clear = Button(frame, text='C', height=4, width=9, font=35, bg="#313131", fg="red", command=wyczysc)
button_clear.grid(row=5, column=0)

pierwiastek = Button(frame, text='√', height=4, width=9, font=35, bg="#313131", fg="#00BD2C", command=oblicz_pierwiastek)
pierwiastek.grid(row=1, column=1)

kwadrat = Button(frame, text='x²', height=4, width=9, font=35, bg="#313131", fg="#00BD2C", command=oblicz_kwadrat)
kwadrat.grid(row=1, column=2)

divide = Button(frame, text='÷', height=4, width=9, font=35, bg="#313131", fg="#00BD2C", command=lambda: klikniecie('/'))
divide.grid(row=1, column=3)

button7 = Button(frame, text=7, height=4, width=9, font=35, bg="#1F1F1F", fg="white", command=lambda: klikniecie(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, bg="#1F1F1F", fg="white", command=lambda: klikniecie(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, bg="#1F1F1F", fg="white", command=lambda: klikniecie(9))
button9.grid(row=2, column=2)

multiply = Button(frame, text='x', height=4, width=9, font=35, bg="#313131", fg="#00BD2C", command=lambda: klikniecie('*'))
multiply.grid(row=2, column=3)

button4 = Button(frame, text=4, height=4, width=9, font=35, bg="#1F1F1F", fg="white", command=lambda: klikniecie(4))
button4.grid(row=3, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, bg="#1F1F1F", fg="white", command=lambda: klikniecie(5))
button5.grid(row=3, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, bg="#1F1F1F", fg="white", command=lambda: klikniecie(6))
button6.grid(row=3, column=2)

minus = Button(frame, text='-', height=4, width=9, font=35, bg="#313131", fg="#00BD2C", command=lambda: klikniecie('-'))
minus.grid(row=3, column=3)

button1 = Button(frame, text=1, height=4, width=9, font=35, bg="#1F1F1F", fg="white", command=lambda: klikniecie(1))
button1.grid(row=4, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35, bg="#1F1F1F", fg="white", command=lambda: klikniecie(2))
button2.grid(row=4, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, bg="#1F1F1F", fg="white", command=lambda: klikniecie(3))
button3.grid(row=4, column=2)

plus = Button(frame, text='+', height=4, width=9, font=35, bg="#313131", fg="#00BD2C", command=lambda: klikniecie('+'))
plus.grid(row=4, column=3)

logarytm = Button(frame, text='log2', height=4, width=9, font=35, bg="#313131", fg="#00BD2C", command=oblicz_log2)
logarytm.grid(row=1, column=0)

button0 = Button(frame, text=0, height=4, width=9, font=35, bg="#1F1F1F", fg="white", command=lambda: klikniecie(0))
button0.grid(row=5, column=1)

decimal = Button(frame, text='.', height=4, width=9, font=35, bg="#313131", fg="white", command=lambda: klikniecie('.'))
decimal.grid(row=5, column=2)

equal = Button(frame, text='=', height=4, width=9, font=35, bg="#3CBC00", fg="white", command=rownanie)
equal.grid(row=5, column=3)

window.mainloop()