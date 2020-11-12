import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Button
from tkinter.ttk import Progressbar
from tkinter import Menu

def init_window():

    windows = tk.Tk()
    windows.title("Calculadora NOG G12")  # titulo de la pantalla
    windows.geometry('500x300')  # tamaño de la ventana
    
    # creacion de una etiqueta
    label = tk.Label(windows, text="Calculadora 2.0", font=("arial bold", 15))
    # ubicacion de la etiqueta en una columna
    label.grid(column=1, row=0)
    label.configure(bg="yellow")
    # agregar dos campos de texto
    n1 = tk.Entry(windows, width=10)
    n2 = tk.Entry(windows, width=10)

    n1.grid(column=1, row=1)
    n2.grid(column=1, row=2)
    label_n1 = tk.Label(
        windows, text="Ingrese el primer numero", font=("arial bold", 10))
    label_n1.grid(column=0, row=1)
    label_n1.configure(bg ="yellow")
    label_n2 = tk.Label(
        windows, text="Ingrese el segundo numero", font=("arial bold", 10))
    label_n2.grid(column=0, row=2)
    label_n2.configure(bg ="yellow")

    # agregar un seleccionador o combobox
    # 1) crearemos la etiqueta para este
    label_operador = tk.Label(
        windows, text="elija una operacion", font=("arial bond", 10))
    label_operador.grid(column=0, row=3)
    label_operador.configure(bg ="yellow")
    # 2) crear el seleccionador
    combo_operadores = ttk.Combobox(windows)
    # 3) asignaremos los valores dele seleccionador
    combo_operadores["values"] = ["+", "-", "*", "/", "pow"]
    # 4) asignaremos un valor por defecto
    combo_operadores.current(0)
    # 5) ubicar el seleccionador
    combo_operadores.grid(column=1, row=3)
    # ahora vamos a agregar un boton para poder hacer las operacione sy mostrar el resultado

    # pero primero agregaremos la etiqueta resultado
    label_resultado = tk.Label(
        windows, text='Resultado:', font=("arial bond", 15))
    label_resultado.grid(column=0, row=5)
    label_resultado.configure(bg = "white")
    # y luego de crear las funciones proseguimos a la ceacion del boton
    # boton calcular
    boton = tk.Button(windows, command=lambda: click_calcular(label_resultado, n1.get(), n2.get(), combo_operadores.get()),
                      text="calcular", bg="orange", fg="white")
    boton.grid(column=1, row=4)
    # primer widgets menssagebox

    def click():
        messagebox.showinfo("hola", "Todo va a estar bien , sonrie :)")
    btn = Button(windows, text="¿estas triste?, clickea aca", command=click)
    btn.grid(column=1, row=15)
    # segundo widget progress bar
    style = ttk.Style()
    style.theme_use("default")
    style.configure("red.Horizontal.TProgressbar", background=("yellow"))
    bar = Progressbar(windows, length=200,style="red.Horizontal.TProgressbar")
    bar['value'] = 90
    bar.grid(column=1, row=12)
    # tercer widget menu
    menu = Menu(windows)
    new_item = Menu(menu)
    new_item.add_command(label='Proximamente')
    menu.add_cascade(label='opciones', menu=new_item)
    windows.config(menu=menu)
    # 4 cambiar color de fondo
    windows.configure(bg = "blue")
    windows.mainloop()


# funcion que hace las operacion
def operacion(n1, n2, operador):
    if operador == "+":
        resultado = n1+n2
    elif operador == "-":
        resultado = n1-n2
    elif operador == "*":
        resultado = n1*n2
    elif operador == "/":
        if n2 != 0:
            resultado = round(n1 / n2, 2)
        else:
            resultado = "la division por 0 no es valida"
    else:
        resultado = n1**n2
    return resultado
# funcion que calcula al dar click


def click_calcular(label, n1, n2, operador):

    valor1 = float(n1)
    valor2 = float(n2)

    # calculo de los valores
    res = operacion(valor1, valor2, operador)

    # actualizar el texto de la etiqueta
    label.configure(text="Resultado : "+str(res))

def main():
    init_window()
main()
