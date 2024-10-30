import tkinter as tk
from tkinter import messagebox
from Logica import Procesos  # Supongo que ya tienes el archivo de lógica en otro módulo

class Principal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de % Cuota$")
        self.geometry("1000x700")
        
        self.procesos = Procesos()  # Instancia de la clase Procesos
        
        self.init_components()
    
    def init_components(self):
        # Crear panel principal
        self.panel1 = tk.Frame(self, bg="gray")
        self.panel1.pack(fill=tk.BOTH, expand=True)
        
        # Crear el título
        self.label1 = tk.Label(self.panel1, text="Calculadora de % Cuota$", font=("Comic Sans MS", 36), bg="gray", fg="white")
        self.label1.pack(pady=20)
        
        # Aquí irán los otros componentes (labels, textfields, buttons, etc.)
        # Continuaremos con la GUI a partir de aquí en las siguientes partes.
root = tk.Tk()
root.title("Calculadora de Cuotas")

# Crear la instancia de la clase Procesos
procesos = Procesos()

# Definir las etiquetas y entradas de texto
lblMontoContado = tk.Label(root, text="Monto Contado:")
lblMontoContado.grid(row=0, column=0, padx=10, pady=5)

lblMontoContado = tk.Label(root, text="Costo Final:")
lblMontoContado.grid(row=0, column=2, padx=5, pady=5)

lblMontoContado = tk.Label(root, text="Cuota X Mes:")
lblMontoContado.grid(row=0, column=3, padx=5, pady=5)

txtMontoContado = tk.Entry(root)
txtMontoContado.grid(row=0, column=1, padx=5, pady=5)

# Sección para cuotas de 1 mes
lblUno = tk.Label(root, text="1 Cuota:")
lblUno.grid(row=1, column=0, padx=5, pady=5)

txtUno = tk.Entry(root)
txtUno.grid(row=1, column=1, padx=5, pady=5)

txtTotalUno = tk.Entry(root, state='disabled')
txtTotalUno.grid(row=1, column=2, padx=5, pady=5)

txtMontoUno = tk.Entry(root, state='disabled')
txtMontoUno.grid(row=1, column=3, padx=5, pady=5)

# Sección para cuotas de 3 meses
lblTres = tk.Label(root, text="3 Cuotas:")
lblTres.grid(row=2, column=0, padx=5, pady=5)

txtTres = tk.Entry(root)
txtTres.grid(row=2, column=1, padx=5, pady=5)

txtTotalTres = tk.Entry(root, state='disabled')
txtTotalTres.grid(row=2, column=2, padx=5, pady=5)

txtMontoTres = tk.Entry(root, state='disabled')
txtMontoTres.grid(row=2, column=3, padx=5, pady=5)

# Sección para cuotas de 6 meses
lblSeis = tk.Label(root, text="6 Cuotas:")
lblSeis.grid(row=3, column=0, padx=5, pady=5)

txtSeis = tk.Entry(root)
txtSeis.grid(row=3, column=1, padx=5, pady=5)

txtTotalSeis = tk.Entry(root, state='disabled')
txtTotalSeis.grid(row=3, column=2, padx=5, pady=5)

txtMontoSeis = tk.Entry(root, state='disabled')
txtMontoSeis.grid(row=3, column=3, padx=5, pady=5)

# Sección para cuotas de 9 meses
lblNueve = tk.Label(root, text="9 Cuotas:")
lblNueve.grid(row=4, column=0, padx=5, pady=5)

txtNueve = tk.Entry(root)
txtNueve.grid(row=4, column=1, padx=5, pady=5)

txtTotalNueve = tk.Entry(root, state='disabled')
txtTotalNueve.grid(row=4, column=2, padx=5, pady=5)

txtMontoNueve = tk.Entry(root, state='disabled')
txtMontoNueve.grid(row=4, column=3, padx=5, pady=5)

# Sección para cuotas de 12 meses
lblDoce = tk.Label(root, text="12 Cuotas:")
lblDoce.grid(row=5, column=0, padx=5, pady=5)

txtDoce = tk.Entry(root)
txtDoce.grid(row=5, column=1, padx=5, pady=5)

txtTotalDoce = tk.Entry(root, state='disabled')
txtTotalDoce.grid(row=5, column=2, padx=5, pady=5)

txtMontoDoce = tk.Entry(root, state='disabled')
txtMontoDoce.grid(row=5, column=3, padx=5, pady=5)


# Función que maneja el botón de calcular
def calcular():
    try:
        monto_contado = txtMontoContado.get()
        if monto_contado:
            contado = int(monto_contado)

            # CUOTA DE 1 MES
            una_cuota = txtUno.get()
            if una_cuota:
                cuota_uno = int(una_cuota)
                procesos.set_valor(contado)
                procesos.set_porcentaje(cuota_uno)
                procesos.calcular_cuota()
                txtTotalUno.config(state='normal')
                txtTotalUno.delete(0, tk.END)
                txtTotalUno.insert(tk.END, f"{procesos.get_total():.2f}")
                txtTotalUno.config(state='disabled')

                procesos.set_cant_cuota(1)
                procesos.valor_cuota()
                txtMontoUno.config(state='normal')
                txtMontoUno.delete(0, tk.END)
                txtMontoUno.insert(tk.END, f"{procesos.get_monto_cuota():.2f}")
                txtMontoUno.config(state='disabled')

            # CUOTA DE 3 MESES
            tres_cuotas = txtTres.get()
            if tres_cuotas:
                cuota_tres = int(tres_cuotas)
                procesos.set_valor(contado)
                procesos.set_porcentaje(cuota_tres)
                procesos.calcular_cuota()
                txtTotalTres.config(state='normal')
                txtTotalTres.delete(0, tk.END)
                txtTotalTres.insert(tk.END, f"{procesos.get_total():.2f}")
                txtTotalTres.config(state='disabled')

                procesos.set_cant_cuota(3)
                procesos.valor_cuota()
                txtMontoTres.config(state='normal')
                txtMontoTres.delete(0, tk.END)
                txtMontoTres.insert(tk.END, f"{procesos.get_monto_cuota():.2f}")
                txtMontoTres.config(state='disabled')

            # CUOTA DE 6 MESES
            seis_cuotas = txtSeis.get()
            if seis_cuotas:
                cuota_seis = int(seis_cuotas)
                procesos.set_valor(contado)
                procesos.set_porcentaje(cuota_seis)
                procesos.calcular_cuota()
                txtTotalSeis.config(state='normal')
                txtTotalSeis.delete(0, tk.END)
                txtTotalSeis.insert(tk.END, f"{procesos.get_total():.2f}")
                txtTotalSeis.config(state='disabled')

                procesos.set_cant_cuota(6)
                procesos.valor_cuota()
                txtMontoSeis.config(state='normal')
                txtMontoSeis.delete(0, tk.END)
                txtMontoSeis.insert(tk.END, f"{procesos.get_monto_cuota():.2f}")
                txtMontoSeis.config(state='disabled')

            # CUOTA DE 9 MESES
            nueve_cuotas = txtNueve.get()
            if nueve_cuotas:
                cuota_nueve = int(nueve_cuotas)
                procesos.set_valor(contado)
                procesos.set_porcentaje(cuota_nueve)
                procesos.calcular_cuota()
                txtTotalNueve.config(state='normal')
                txtTotalNueve.delete(0, tk.END)
                txtTotalNueve.insert(tk.END, f"{procesos.get_total():.2f}")
                txtTotalNueve.config(state='disabled')

                procesos.set_cant_cuota(9)
                procesos.valor_cuota()
                txtMontoNueve.config(state='normal')
                txtMontoNueve.delete(0, tk.END)
                txtMontoNueve.insert(tk.END, f"{procesos.get_monto_cuota():.2f}")
                txtMontoNueve.config(state='disabled')

            # CUOTA DE 12 MESES
            doce_cuotas = txtDoce.get()
            if doce_cuotas:
                cuota_doce = int(doce_cuotas)
                procesos.set_valor(contado)
                procesos.set_porcentaje(cuota_doce)
                procesos.calcular_cuota ()
                txtTotalDoce.config(state='normal')
                txtTotalDoce.delete(0, tk.END)
                txtTotalDoce.insert(tk.END, f"{procesos.get_total():.2f}")
                txtTotalDoce.config(state='disabled')

                procesos.set_cant_cuota(12)
                procesos.valor_cuota()
                txtMontoDoce.config(state='normal')
                txtMontoDoce.delete(0, tk.END)
                txtMontoDoce.insert(tk.END, f"{procesos.get_monto_cuota():.2f}")
                txtMontoDoce.config(state='disabled')

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores válidos.")


# Crear el botón de calcular
btnCalcular = tk.Button(root, text="Calcular", command=calcular)
btnCalcular.grid(row=6, column=1, padx=5, pady=5)

# Ejecutar la ventana
root.mainloop()