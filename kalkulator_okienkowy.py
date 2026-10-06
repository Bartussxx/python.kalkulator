from tkinter import *
import math

def klikniecie(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def pokaz_blad(komunikat):
    global equation_text
    equation_label.set(komunikat)
    equation_text = ""

def rownanie():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except (SyntaxError, NameError, TypeError):
        pokaz_blad("cos ty odwalil")
    except ZeroDivisionError:
        pokaz_blad("tak sie nie dzieli debilu")

def wykonaj_operacje(operacja):
    global equation_text
    try:
        wynik = str(operacja(float(eval(equation_text))))
        equation_label.set(wynik)
        equation_text = wynik
    except Exception:
        pokaz_blad("ty jestes upo chyba")

def oblicz_pierwiastek():
    wykonaj_operacje(math.sqrt)

def oblicz_kwadrat():
    wykonaj_operacje(lambda x: x ** 2)

def oblicz_log2():
    wykonaj_operacje(math.log2)

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

przyciski = [
    [('log2', oblicz_log2), ('√', oblicz_pierwiastek), ('x²', oblicz_kwadrat), ('÷', lambda: klikniecie('/'))],
    [(7, lambda: klikniecie(7)), (8, lambda: klikniecie(8)), (9, lambda: klikniecie(9)), ('x', lambda: klikniecie('*'))],
    [(4, lambda: klikniecie(4)), (5, lambda: klikniecie(5)), (6, lambda: klikniecie(6)), ('-', lambda: klikniecie('-'))],
    [(1, lambda: klikniecie(1)), (2, lambda: klikniecie(2)), (3, lambda: klikniecie(3)), ('+', lambda: klikniecie('+'))],
    [('C', wyczysc), (0, lambda: klikniecie(0)), ('.', lambda: klikniecie('.')), ('=', rownanie)]
]

for r_idx, wiersz in enumerate(przyciski, start=1):
    for c_idx, (tekst, akcja) in enumerate(wiersz):
        bg_col, fg_col = "#1F1F1F", "white"
        if tekst in ('+', '-', 'x', '÷', '√', 'x²', 'log2', '.'):
            bg_col, fg_col = "#313131", "#00BD2C"
        elif tekst == 'C':
            bg_col, fg_col = "#313131", "red"
        elif tekst == '=':
            bg_col, fg_col = "#3CBC00", "white"

        btn = Button(frame, text=tekst, height=4, width=9, font=35, bg=bg_col, fg=fg_col, command=akcja)
        btn.grid(row=r_idx, column=c_idx, padx=2, pady=2)

window.mainloop()