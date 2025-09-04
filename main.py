import tkinter as tk

app = tk.Tk()
app.title("cAlCuLaDoRa")
app.geometry("300x300")
app.minsize(300, 300)

etiqueta = tk.Label(app, text="Calculadora")
etiqueta.pack(pady=5)

entrada = tk.Entry(app)
entrada.pack(pady=5)

