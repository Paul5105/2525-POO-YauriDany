import tkinter as tk
from tkinter import ttk, messagebox


class AplicacionTareas:
    def __init__(self, ventana):
        # Configuración de la ventana principal
        self.ventana = ventana
        self.ventana.title("Gestor de Tareas - Aplicación GUI")
        self.ventana.geometry("600x400")
        self.ventana.resizable(True, True)

        # Variables de control
        self.tareas = []

        # Configurar el estilo de los widgets
        self.configurar_estilos()

        # Crear los componentes de la interfaz
        self.crear_widgets()

    def configurar_estilos(self):
        """Configura los estilos para los widgets de la aplicación"""
        estilo = ttk.Style()
        estilo.configure('Titulo.TLabel', font=('Arial', 16, 'bold'))
        estilo.configure('Normal.TLabel', font=('Arial', 10))
        estilo.configure('Boton.TButton', font=('Arial', 10))

    def crear_widgets(self):
        """Crea y organiza todos los widgets en la ventana"""
        # Marco principal para organizar los elementos
        marco_principal = ttk.Frame(self.ventana, padding="10")
        marco_principal.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configurar la expansión de filas y columnas
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)
        marco_principal.columnconfigure(1, weight=1)
        marco_principal.rowconfigure(4, weight=1)

        # Título de la aplicación
        titulo = ttk.Label(marco_principal, text="Gestor de Tareas", style='Titulo.TLabel')
        titulo.grid(row=0, column=0, columnspan=3, pady=(0, 15))

        # Etiqueta y campo de texto para nueva tarea
        etiqueta_tarea = ttk.Label(marco_principal, text="Nueva Tarea:", style='Normal.TLabel')
        etiqueta_tarea.grid(row=1, column=0, sticky=tk.W, padx=(0, 5))

        self.entrada_tarea = ttk.Entry(marco_principal, width=40)
        self.entrada_tarea.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(0, 5))
        self.entrada_tarea.bind('<Return>', lambda e: self.agregar_tarea())  # Enter para agregar

        # Botón para agregar tarea
        boton_agregar = ttk.Button(marco_principal, text="Agregar",
                                   command=self.agregar_tarea, style='Boton.TButton')
        boton_agregar.grid(row=1, column=2, sticky=tk.W)

        # Etiqueta para la lista de tareas
        etiqueta_lista = ttk.Label(marco_principal, text="Tareas Pendientes:", style='Normal.TLabel')
        etiqueta_lista.grid(row=2, column=0, columnspan=3, sticky=tk.W, pady=(15, 5))

        # Marco para la lista de tareas y scrollbar
        marco_lista = ttk.Frame(marco_principal)
        marco_lista.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))
        marco_lista.columnconfigure(0, weight=1)
        marco_lista.rowconfigure(0, weight=1)

        # Lista de tareas con scrollbar
        self.lista_tareas = tk.Listbox(marco_lista, height=10, selectmode=tk.SINGLE)
        self.lista_tareas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        scrollbar = ttk.Scrollbar(marco_lista, orient=tk.VERTICAL, command=self.lista_tareas.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.lista_tareas.configure(yscrollcommand=scrollbar.set)

        # Marco para botones de acción
        marco_botones = ttk.Frame(marco_principal)
        marco_botones.grid(row=4, column=0, columnspan=3, sticky=(tk.E, tk.S), pady=(10, 0))

        # Botón para limpiar selección
        boton_limpiar = ttk.Button(marco_botones, text="Limpiar Selección",
                                   command=self.limpiar_seleccion, style='Boton.TButton')
        boton_limpiar.grid(row=0, column=0, padx=(0, 5))

        # Botón para eliminar tarea seleccionada
        boton_eliminar = ttk.Button(marco_botones, text="Eliminar Tarea",
                                    command=self.eliminar_tarea, style='Boton.TButton')
        boton_eliminar.grid(row=0, column=1, padx=(0, 5))

        # Botón para marcar como completada
        boton_completar = ttk.Button(marco_botones, text="Marcar como Completada",
                                     command=self.marcar_completada, style='Boton.TButton')
        boton_completar.grid(row=0, column=2)

    def agregar_tarea(self):
        """Agrega una nueva tarea a la lista"""
        tarea = self.entrada_tarea.get().strip()
        if tarea:
            self.tareas.append({"texto": tarea, "completada": False})
            self.actualizar_lista_tareas()
            self.entrada_tarea.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Campo vacío", "Por favor, ingresa una tarea.")

    def actualizar_lista_tareas(self):
        """Actualiza la lista de tareas en la interfaz"""
        self.lista_tareas.delete(0, tk.END)
        for i, tarea in enumerate(self.tareas):
            estado = "✓ " if tarea["completada"] else "☐ "
            self.lista_tareas.insert(tk.END, estado + tarea["texto"])
            if tarea["completada"]:
                self.lista_tareas.itemconfig(i, {'fg': 'gray'})

    def limpiar_seleccion(self):
        """Limpia la selección actual en la lista de tareas"""
        self.lista_tareas.selection_clear(0, tk.END)

    def eliminar_tarea(self):
        """Elimina la tarea seleccionada de la lista"""
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            del self.tareas[indice]
            self.actualizar_lista_tareas()
        else:
            messagebox.showwarning("Ninguna selección", "Por favor, selecciona una tarea para eliminar.")

    def marcar_completada(self):
        """Marca la tarea seleccionada como completada"""
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            self.tareas[indice]["completada"] = True
            self.actualizar_lista_tareas()
        else:
            messagebox.showwarning("Ninguna selección", "Por favor, selecciona una tarea para marcar como completada.")


def main():
    """Función principal que inicia la aplicación"""
    ventana = tk.Tk()
    app = AplicacionTareas(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
