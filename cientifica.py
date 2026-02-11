import tkinter as tk
from tkinter import messagebox
import math

class CalculadoraCientifica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        # Variable para almacenar el contenido de la pantalla
        self.pantalla_var = tk.StringVar()
        
        # --- Pantalla de visualización ---
        # state='readonly' bloquea la escritura desde el teclado
        self.pantalla = tk.Entry(
            root, textvariable=self.pantalla_var, font=("Arial", 24), 
            bg="#f0f0f0", fg="black", bd=10, relief="flat", 
            justify="right", state="readonly"
        )
        self.pantalla.pack(fill="both", padx=10, pady=20, ipady=15)

        # --- Contenedor de botones ---
        self.botonera = tk.Frame(root)
        self.botonera.pack(expand=True, fill="both", padx=10, pady=10)

        # Definición de botones: (Texto, Fila, Columna, Comando)
        botones = [
            ('sin', 0, 0), ('cos', 0, 1), ('tan', 0, 2), ('log', 0, 3),
            ('√', 1, 0), ('x²', 1, 1), ('^', 1, 2), ('π', 1, 3),
            ('(', 2, 0), (')', 2, 1), ('C', 2, 2), ('DEL', 2, 3),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('/', 3, 3),
            ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('*', 4, 3),
            ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('-', 5, 3),
            ('0', 6, 0), ('.', 6, 1), ('=', 6, 2), ('+', 6, 3),
        ]

        # Estilo de botones
        btn_config = {'font': ("Arial", 12, "bold"), 'width': 5, 'height': 2, 'bd': 2}

        for (texto, fila, col) in botones:
            action = lambda x=texto: self.click_boton(x)
            tk.Button(self.botonera, text=texto, command=action, **btn_config).grid(row=fila, column=col, sticky="nsew", padx=2, pady=2)

        # Ajustar proporciones de la rejilla
        for i in range(7): self.botonera.grid_rowconfigure(i, weight=1)
        for i in range(4): self.botonera.grid_columnconfigure(i, weight=1)

    def click_boton(self, valor):
        actual = self.pantalla_var.get()

        if valor == "C":
            self.actualizar_pantalla("")
        elif valor == "DEL":
            self.actualizar_pantalla(actual[:-1])
        elif valor == "=":
            self.calcular()
        elif valor == "√":
            self.insertar_funcion("math.sqrt")
        elif valor == "sin":
            self.insertar_funcion("math.sin(math.radians")
        elif valor == "cos":
            self.insertar_funcion("math.cos(math.radians")
        elif valor == "tan":
            self.insertar_funcion("math.tan(math.radians")
        elif valor == "log":
            self.insertar_funcion("math.log10")
        elif valor == "x²":
            self.actualizar_pantalla(actual + "**2")
        elif valor == "^":
            self.actualizar_pantalla(actual + "**")
        elif valor == "π":
            self.actualizar_pantalla(actual + str(math.pi))
        else:
            self.actualizar_pantalla(actual + str(valor))

    def insertar_funcion(self, nombre_func):
        actual = self.pantalla_var.get()
        self.actualizar_pantalla(f"{nombre_func}({actual})")

    def actualizar_pantalla(self, texto):
        # Para modificar un widget readonly, hay que pasarlo a 'normal' momentáneamente
        self.pantalla.config(state="normal")
        self.pantalla_var.set(texto)
        self.pantalla.config(state="readonly")

    def calcular(self):
        try:
            expresion = self.pantalla_var.get()
            # Evaluamos de forma segura usando el namespace de math
            resultado = eval(expresion, {"__builtins__": None, "math": math})
            self.actualizar_pantalla(str(resultado))
        except Exception as e:
            messagebox.showerror("Error", "Expresión no válida")
            self.actualizar_pantalla("")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraCientifica(root)
    root.mainloop()