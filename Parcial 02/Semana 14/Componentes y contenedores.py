"""
Agenda Personal (Tkinter)
Autor: Paúl Dany Yauri
Descripción:
- Ventana con Treeview que muestra eventos: Fecha | Hora | Descripción
- Permite agregar eventos (DatePicker, hora, descripción)
- Permite eliminar evento seleccionado (con confirmación)
- Persiste eventos en 'eventos.json'
- Usa tkcalendar.DateEntry si está disponible; si no, muestra un calendario popup propio.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, date
import json
import os
import calendar

# Intentamos importar DateEntry de tkcalendar (opcional).
try:
    from tkcalendar import DateEntry
    TKCAL_AVAILABLE = True
except Exception:
    TKCAL_AVAILABLE = False


# ----------------------------
# Utilidades de persistencia
# ----------------------------
ARCHIVO_EVENTOS = "eventos.json"


def cargar_eventos():
    """Carga eventos desde archivo JSON si existe, devuelve lista de dicts."""
    if os.path.exists(ARCHIVO_EVENTOS):
        try:
            with open(ARCHIVO_EVENTOS, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            messagebox.showwarning("Aviso", "No se pudo leer eventos.json. Se iniciará vacío.")
            return []
    return []


def guardar_eventos(eventos):
    """Guarda la lista de eventos (lista de dicts) en JSON."""
    try:
        with open(ARCHIVO_EVENTOS, "w", encoding="utf-8") as f:
            json.dump(eventos, f, indent=4, ensure_ascii=False)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar eventos: {e}")


# ----------------------------
# Calendario popup (si no hay tkcalendar)
# ----------------------------
class MiniCalendario(tk.Toplevel):
    """Popup simple para seleccionar fecha si no existe tkcalendar."""
    def __init__(self, parent, callback):
        super().__init__(parent)
        self.title("Seleccionar fecha")
        self.resizable(False, False)
        self.callback = callback  # función a llamar con la fecha seleccionada
        self.year = date.today().year
        self.month = date.today().month
        self._dibujar()

    def _dibujar(self):
        # encabezado con mes y año
        header = tk.Frame(self)
        header.pack(padx=5, pady=5)
        prev_btn = tk.Button(header, text="<", width=3, command=self._mes_anterior)
        prev_btn.pack(side=tk.LEFT)
        lbl = tk.Label(header, text=f"{calendar.month_name[self.month]} {self.year}", width=20)
        lbl.pack(side=tk.LEFT)
        next_btn = tk.Button(header, text=">", width=3, command=self._mes_siguiente)
        next_btn.pack(side=tk.LEFT)

        cal_frame = tk.Frame(self)
        cal_frame.pack(padx=5, pady=5)

        # cabecera dias
        dias = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]
        for i, d in enumerate(dias):
            tk.Label(cal_frame, text=d, width=4, borderwidth=0).grid(row=0, column=i)

        monthcal = calendar.Calendar(firstweekday=0).monthdayscalendar(self.year, self.month)
        for r, semana in enumerate(monthcal, start=1):
            for c, dia in enumerate(semana):
                if dia == 0:
                    tk.Label(cal_frame, text="", width=4).grid(row=r, column=c)
                else:
                    btn = tk.Button(cal_frame, text=str(dia), width=4,
                                    command=lambda d=dia: self._seleccionar(d))
                    btn.grid(row=r, column=c)

    def _mes_anterior(self):
        self.month -= 1
        if self.month < 1:
            self.month = 12
            self.year -= 1
        for widget in self.winfo_children():
            widget.destroy()
        self._dibujar()

    def _mes_siguiente(self):
        self.month += 1
        if self.month > 12:
            self.month = 1
            self.year += 1
        for widget in self.winfo_children():
            widget.destroy()
        self._dibujar()

    def _seleccionar(self, dia):
        dt = date(self.year, self.month, dia)
        self.callback(dt.strftime("%Y-%m-%d"))  # formato ISO
        self.destroy()


# ----------------------------
# Aplicación principal GUI
# ----------------------------
class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📅 Agenda Personal - Dany Yauri")
        self.root.geometry("700x450")
        self.root.resizable(False, False)

        # Datos en memoria (lista de dicts)
        self.eventos = cargar_eventos()

        # ----------------- Frames -----------------
        top_frame = tk.Frame(root, pady=10)
        top_frame.pack(fill=tk.X)

        middle_frame = tk.Frame(root, pady=5)
        middle_frame.pack(fill=tk.X)

        bottom_frame = tk.Frame(root, pady=10)
        bottom_frame.pack(fill=tk.BOTH, expand=True)

        # ----------------- Inputs -----------------
        # Date picker: usamos tkcalendar.DateEntry si existe; si no, Entry + botón popup
        lbl_fecha = tk.Label(top_frame, text="Fecha (YYYY-MM-DD):")
        lbl_fecha.grid(row=0, column=0, padx=5, sticky=tk.W)

        if TKCAL_AVAILABLE:
            self.date_entry = DateEntry(top_frame, date_pattern="yyyy-mm-dd")
            self.date_entry.grid(row=0, column=1, padx=5)
        else:
            self.date_var = tk.StringVar()
            self.date_entry = tk.Entry(top_frame, textvariable=self.date_var, width=15)
            self.date_entry.grid(row=0, column=1, padx=5)
            btn_cal = tk.Button(top_frame, text="📅", command=self._abrir_calendario_popup)
            btn_cal.grid(row=0, column=2, padx=3)

        lbl_hora = tk.Label(top_frame, text="Hora (HH:MM):")
        lbl_hora.grid(row=0, column=3, padx=5, sticky=tk.W)
        self.hora_entry = tk.Entry(top_frame, width=10)
        self.hora_entry.grid(row=0, column=4, padx=5)

        lbl_desc = tk.Label(middle_frame, text="Descripción:")
        lbl_desc.grid(row=0, column=0, padx=5, sticky=tk.W)
        self.desc_entry = tk.Entry(middle_frame, width=60)
        self.desc_entry.grid(row=0, column=1, padx=5, columnspan=3)

        # ----------------- Botones -----------------
        btn_agregar = tk.Button(middle_frame, text="➕ Agregar Evento", bg="#2ecc71", fg="white",
                                command=self.agregar_evento, width=16)
        btn_agregar.grid(row=1, column=1, pady=8, sticky=tk.W)

        btn_eliminar = tk.Button(middle_frame, text="🗑 Eliminar Seleccionado", bg="#e74c3c", fg="white",
                                 command=self.eliminar_evento, width=18)
        btn_eliminar.grid(row=1, column=2, pady=8, sticky=tk.W)

        btn_salir = tk.Button(middle_frame, text="Salir", command=self.root.quit, width=8)
        btn_salir.grid(row=1, column=3, pady=8, sticky=tk.E)

        # ----------------- Treeview (lista de eventos) -----------------
        columns = ("fecha", "hora", "descripcion")
        self.tree = ttk.Treeview(bottom_frame, columns=columns, show="headings", height=12)
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")
        self.tree.column("fecha", width=120, anchor=tk.CENTER)
        self.tree.column("hora", width=80, anchor=tk.CENTER)
        self.tree.column("descripcion", width=460, anchor=tk.W)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0))

        # Scrollbar vertical
        scrollbar = ttk.Scrollbar(bottom_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Cargar eventos guardados al iniciar
        self._cargar_en_tree()

    # ----------------------------
    # Calendar popup wrapper
    # ----------------------------
    def _abrir_calendario_popup(self):
        MiniCalendario(self.root, self._seleccion_fecha)

    def _seleccion_fecha(self, fecha_str):
        # fecha_str en formato 'YYYY-MM-DD'
        self.date_var.set(fecha_str)

    # ----------------------------
    # Operaciones sobre eventos
    # ----------------------------
    def _cargar_en_tree(self):
        """Carga los eventos desde self.eventos al Treeview."""
        for ev in self.eventos:
            self.tree.insert("", tk.END, values=(ev["fecha"], ev["hora"], ev["descripcion"]))

    def agregar_evento(self):
        """Valida inputs, agrega evento a memoria y persiste en archivo y Treeview."""
        if TKCAL_AVAILABLE:
            fecha = self.date_entry.get_date().strftime("%Y-%m-%d")
        else:
            fecha = self.date_entry.get().strip()

        hora = self.hora_entry.get().strip()
        desc = self.desc_entry.get().strip()

        if not fecha or not hora or not desc:
            messagebox.showwarning("Campos incompletos", "Por favor completa fecha, hora y descripción.")
            return

        # Validar formato de fecha y hora
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Formato fecha", "La fecha debe tener formato YYYY-MM-DD.")
            return

        try:
            datetime.strptime(hora, "%H:%M")
        except ValueError:
            messagebox.showerror("Formato hora", "La hora debe tener formato HH:MM (24h).")
            return

        evento = {"fecha": fecha, "hora": hora, "descripcion": desc}
        self.eventos.append(evento)
        guardar_eventos(self.eventos)  # persistir
        self.tree.insert("", tk.END, values=(fecha, hora, desc))

        # limpiar entradas
        if TKCAL_AVAILABLE:
            pass  # DateEntry muestra fecha por defecto; no lo limpiamos
        else:
            self.date_entry.delete(0, tk.END)
        self.hora_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

        messagebox.showinfo("Éxito", "Evento agregado correctamente.")

    def eliminar_evento(self):
        """Elimina el evento seleccionado con confirmación."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selecciona", "Por favor selecciona un evento en la lista.")
            return

        # confirmación
        if not messagebox.askyesno("Confirmar", "¿Estás seguro que deseas eliminar el evento seleccionado?"):
            return

        for item in selected:
            vals = self.tree.item(item, "values")
            # remover del arreglo self.eventos: buscar coincidencia por los 3 campos
            for ev in self.eventos:
                if ev["fecha"] == vals[0] and ev["hora"] == vals[1] and ev["descripcion"] == vals[2]:
                    self.eventos.remove(ev)
                    break
            self.tree.delete(item)

        guardar_eventos(self.eventos)
        messagebox.showinfo("Eliminado", "Evento(s) eliminado(s) correctamente.")


# ----------------------------
# Ejecutar la aplicación
# ----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
