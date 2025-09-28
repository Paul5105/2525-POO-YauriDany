import tkinter as tk
from tkinter import messagebox

# -----------------------------
# Aplicación de Lista de Tareas
# -----------------------------

def agregar_tarea(event=None):
    """Agrega una nueva tarea a la lista"""
    tarea = entry_tarea.get().strip()
    if tarea != "":
        listbox_tareas.insert(tk.END, tarea)
        entry_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes agregar una tarea vacía.")

def marcar_completada():
    """Marca una tarea como completada (agrega '[✔]' al inicio)"""
    try:
        seleccion = listbox_tareas.curselection()[0]
        tarea = listbox_tareas.get(seleccion)
        if not tarea.startswith("[✔]"):
            listbox_tareas.delete(seleccion)
            listbox_tareas.insert(seleccion, "[✔] " + tarea)
    except IndexError:
        messagebox.showinfo("Información", "Selecciona una tarea primero.")

def eliminar_tarea():
    """Elimina la tarea seleccionada"""
    try:
        seleccion = listbox_tareas.curselection()[0]
        listbox_tareas.delete(seleccion)
    except IndexError:
        messagebox.showinfo("Información", "Selecciona una tarea para eliminar.")

# -----------------------------
# Interfaz Gráfica
# -----------------------------
ventana = tk.Tk()
ventana.title("Mi Lista de Tareas")
ventana.geometry("400x450")
ventana.config(bg="lightblue")  # Fondo azul claro

# Etiqueta de título
titulo = tk.Label(ventana, text="Agenda de Tareas", font=("Arial", 16, "bold"), bg="lightblue", fg="navy")
titulo.pack(pady=10)

# Campo de entrada
entry_tarea = tk.Entry(ventana, width=40)
entry_tarea.pack(pady=10)
entry_tarea.bind("<Return>", agregar_tarea)

# Botones
frame_botones = tk.Frame(ventana, bg="lightblue")
frame_botones.pack(pady=5)

btn_agregar = tk.Button(frame_botones, text="Añadir Tarea", bg="navy", fg="white", command=agregar_tarea)
btn_agregar.grid(row=0, column=0, padx=5)

btn_completar = tk.Button(frame_botones, text="Marcar como Completada", bg="green", fg="white", command=marcar_completada)
btn_completar.grid(row=0, column=1, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", bg="red", fg="white", command=eliminar_tarea)
btn_eliminar.grid(row=0, column=2, padx=5)

# Lista de tareas
listbox_tareas = tk.Listbox(ventana, width=50, height=15, selectmode=tk.SINGLE, bg="white")
listbox_tareas.pack(pady=10)

# Botón de salir
btn_salir = tk.Button(ventana, text="Salir", bg="gray", fg="white", command=ventana.quit)
btn_salir.pack(pady=5)

ventana.mainloop()
