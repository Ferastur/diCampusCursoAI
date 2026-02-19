import sqlite3
import hashlib
import webbrowser
import urllib.request
import urllib.parse
import io
import re
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
from PIL import Image, ImageTk

# ==========================================
# BASE DE DATOS
# ==========================================
class Database:
    def __init__(self):
        self.conn = sqlite3.connect("biblioteca_v3.db")
        self.cursor = self.conn.cursor()
        self.inicializar_tablas()

    def inicializar_tablas(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT, email TEXT UNIQUE, password TEXT, 
                telefono TEXT, rol TEXT DEFAULT 'usuario', fin_penalizacion DATE
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS libros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT, autor TEXT, isbn TEXT UNIQUE, 
                url_portada TEXT, stock INTEGER DEFAULT 5
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS prestamos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER, libro_id INTEGER,
                fecha_prestamo DATE, fecha_limite DATE, fecha_devolucion DATE,
                estado TEXT DEFAULT 'activo',
                FOREIGN KEY(usuario_id) REFERENCES usuarios(id),
                FOREIGN KEY(libro_id) REFERENCES libros(id)
            )
        """)
        self.cursor.execute("CREATE TABLE IF NOT EXISTS configuracion (id INT, max_dias INT, max_libros INT)")
        
        self.cursor.execute("SELECT COUNT(*) FROM configuracion")
        if self.cursor.fetchone()[0] == 0:
            self.cursor.execute("INSERT INTO configuracion VALUES (1, 15, 3)")
            admin_pass = hashlib.sha256("admin123".encode()).hexdigest()
            self.cursor.execute("INSERT INTO usuarios (nombre, email, password, telefono, rol) VALUES (?,?,?,?,?)",
                               ('Admin Biblioteca', 'admin@talento.com', admin_pass, '34600000000', 'admin'))
            self.conn.commit()

# ==========================================
# APLICACIÓN PRINCIPAL
# ==========================================
class BibliotecaApp:
    def __init__(self, root):
        self.db = Database()
        self.root = root
        self.root.title("Talento Solutions | Library AI Master V3")
        self.root.geometry("1200x850")
        
        # Estilos visuales
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Overdue.Treeview", background="#ffcccc") # Fondo rojo para retrasos
        
        self.usuario_actual = None
        self.mostrar_login()

    def limpiar_pantalla(self):
        for widget in self.root.winfo_children(): widget.destroy()

    # --- AUTENTICACIÓN ---
    def mostrar_login(self):
        self.limpiar_pantalla()
        f = ttk.Frame(self.root, padding="40")
        f.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(f, text="ACCESO BIBLIOTECA", font=('Arial', 18, 'bold')).grid(row=0, columnspan=2, pady=20)
        ttk.Label(f, text="Email:").grid(row=1, column=0, sticky="w")
        self.ent_email = ttk.Entry(f, width=35); self.ent_email.grid(row=1, column=1, pady=10)
        ttk.Label(f, text="Clave:").grid(row=2, column=0, sticky="w")
        self.ent_pass = ttk.Entry(f, width=35, show="*"); self.ent_pass.grid(row=2, column=1, pady=10)

        ttk.Button(f, text="ENTRAR", command=self.procesar_login).grid(row=3, columnspan=2, pady=20, sticky="ew")
        ttk.Button(f, text="REGISTRARSE", command=self.ventana_registro).grid(row=4, columnspan=2)

    def ventana_registro(self):
        reg = tk.Toplevel(self.root)
        reg.title("Nuevo Usuario")
        reg.geometry("400x500")
        
        f = ttk.Frame(reg, padding=20)
        f.pack()

        entries = {}
        for campo in ["Nombre", "Email", "Teléfono", "Password"]:
            ttk.Label(f, text=campo).pack(anchor="w")
            ent = ttk.Entry(f, width=40, show="*" if campo=="Password" else "")
            ent.pack(pady=5)
            entries[campo] = ent

        def registrar():
            e = entries["Email"].get()
            p = entries["Password"].get()
            if not re.match(r"[^@]+@[^@]+\.[^@]+", e): return messagebox.showerror("Error", "Email inválido")
            if len(p) < 6: return messagebox.showerror("Error", "Clave min. 6 caracteres")
            
            h = hashlib.sha256(p.encode()).hexdigest()
            try:
                self.db.cursor.execute("INSERT INTO usuarios (nombre, email, password, telefono) VALUES (?,?,?,?)",
                                       (entries["Nombre"].get(), e, h, entries["Teléfono"].get()))
                self.db.conn.commit()
                messagebox.showinfo("OK", "Registrado con éxito")
                reg.destroy()
            except: messagebox.showerror("Error", "El email ya existe")

        ttk.Button(f, text="CREAR CUENTA", command=registrar).pack(pady=20)

    def procesar_login(self):
        h = hashlib.sha256(self.ent_pass.get().encode()).hexdigest()
        self.db.cursor.execute("SELECT id, nombre, rol FROM usuarios WHERE email=? AND password=?", (self.ent_email.get(), h))
        u = self.db.cursor.fetchone()
        if u:
            self.usuario_actual = {'id': u[0], 'nombre': u[1], 'rol': u[2]}
            self.mostrar_dashboard()
        else: messagebox.showerror("Error", "Credenciales inválidas")

    # --- INTERFAZ PRINCIPAL ---
    def mostrar_dashboard(self):
        self.limpiar_pantalla()
        
        # CAMBIO AQUÍ: Usamos tk.Frame en lugar de ttk.Frame para el fondo azul
        top = tk.Frame(self.root, bg="#2c3e50", padx=10, pady=10)
        top.pack(fill="x")
        
        # Los labels dentro de un tk.Frame también deben ser tk.Label para heredar el fondo fácilmente
        tk.Label(top, text=f"👤 {self.usuario_actual['nombre']} ({self.usuario_actual['rol'].upper()})", 
                 fg="white", bg="#2c3e50", font=('Arial', 10, 'bold')).pack(side="left")
        
        ttk.Button(top, text="Cerrar Sesión", command=self.mostrar_login).pack(side="right")

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", expand=True, padx=10, pady=10)

        # Pestañas condicionales
        self.tab_catalogo = ttk.Frame(self.tabs)
        self.tabs.add(self.tab_catalogo, text="📚 Catálogo")
        
        self.tab_mis_libros = ttk.Frame(self.tabs)
        self.tabs.add(self.tab_mis_libros, text="🤝 Mis Préstamos")

        if self.usuario_actual['rol'] == 'admin':
            self.tab_admin_retornos = ttk.Frame(self.tabs)
            self.tabs.add(self.tab_admin_retornos, text="⚙️ Gestión Devoluciones")
            self.tab_mora = ttk.Frame(self.tabs)
            self.tabs.add(self.tab_mora, text="🚨 Alertas Mora")
            self.disenar_tab_admin_retornos()
            self.disenar_tab_mora()

        self.disenar_tab_catalogo()
        self.disenar_tab_mis_libros()

    # --- CATÁLOGO DE LIBROS ---
    def disenar_tab_catalogo(self):
        for w in self.tab_catalogo.winfo_children(): w.destroy()
        
        header = ttk.Frame(self.tab_catalogo, padding=10)
        header.pack(fill="x")
        
        if self.usuario_actual['rol'] == 'admin':
            ttk.Button(header, text="➕ AÑADIR LIBRO", command=lambda: self.ventana_libro_form()).pack(side="left", padx=5)
            ttk.Button(header, text="📝 EDITAR", command=self.editar_libro).pack(side="left", padx=5)

        ttk.Label(header, text="BUSCAR:").pack(side="left", padx=(20,5))
        self.bus_ent = ttk.Entry(header, width=25); self.bus_ent.pack(side="left")
        ttk.Button(header, text="🔍", command=self.refrescar_libros).pack(side="left", padx=5)

        cols = ("ID", "Título", "Autor", "ISBN", "Disponibles")
        self.tree_libros = ttk.Treeview(self.tab_catalogo, columns=cols, show="headings")
        for c in cols: self.tree_libros.heading(c, text=c)
        self.tree_libros.pack(fill="both", expand=True, padx=10)

        # Footer Acciones
        f = ttk.Frame(self.tab_catalogo, padding=10)
        f.pack(fill="x")
        ttk.Button(f, text="📖 VER FICHA DETALLADA", command=self.ver_ficha).pack(side="left")
        ttk.Button(f, text="✅ SOLICITAR ESTE LIBRO", command=self.solicitar_prestamo).pack(side="right")
        
        self.refrescar_libros()

    def refrescar_libros(self):
        for i in self.tree_libros.get_children(): self.tree_libros.delete(i)
        
        # Filtro base: Si no es admin, solo mostrar stock > 0
        if self.usuario_actual['rol'] == 'admin':
            query = "SELECT id, titulo, autor, isbn, stock FROM libros WHERE titulo LIKE ?"
        else:
            query = "SELECT id, titulo, autor, isbn, stock FROM libros WHERE stock > 0 AND titulo LIKE ?"
            
        self.db.cursor.execute(query, (f"%{self.bus_ent.get()}%",))
        for r in self.db.cursor.fetchall(): self.tree_libros.insert("", "end", values=r)

    # --- FICHA DETALLE (HISTORIAL OCULTO PARA USUARIOS) ---
    def ver_ficha(self):
        sel = self.tree_libros.selection()
        if not sel: return
        l_id = self.tree_libros.item(sel)['values'][0]
        self.db.cursor.execute("SELECT * FROM libros WHERE id=?", (l_id,))
        libro = self.db.cursor.fetchone()

        win = tk.Toplevel(self.root); win.title("Detalle"); win.geometry("500x650")
        
        # Imagen Portada
        lbl_img = ttk.Label(win, text="[Cargando Imagen...]")
        lbl_img.pack(pady=10)
        if libro[4]:
            try:
                with urllib.request.urlopen(libro[4]) as u: raw_data = u.read()
                img = Image.open(io.BytesIO(raw_data)).resize((180, 250))
                photo = ImageTk.PhotoImage(img)
                lbl_img.config(image=photo, text=""); lbl_img.image = photo
            except: lbl_img.config(text="Error de imagen")

        ttk.Label(win, text=libro[1], font=('Arial', 14, 'bold')).pack()
        ttk.Label(win, text=f"Autor: {libro[2]} | ISBN: {libro[3]}").pack()

        # HISTORIAL: Solo para ADMIN
        if self.usuario_actual['rol'] == 'admin':
            ttk.Label(win, text="\n--- HISTORIAL DE PRÉSTAMOS (SOLO ADMIN) ---", foreground="blue").pack()
            t_h = ttk.Treeview(win, columns=("U", "F", "E"), show="headings", height=5)
            t_h.heading("U", text="Usuario"); t_h.heading("F", text="Fecha"); t_h.heading("E", text="Estado")
            t_h.pack(fill="x", padx=10)
            self.db.cursor.execute("SELECT u.nombre, p.fecha_prestamo, p.estado FROM prestamos p JOIN usuarios u ON p.usuario_id=u.id WHERE p.libro_id=?", (l_id,))
            for r in self.db.cursor.fetchall(): t_h.insert("", "end", values=r)
        else:
            ttk.Label(win, text="\n(Historial de préstamos restringido para lectores)", font=('Arial', 8, 'italic')).pack()

    # --- GESTIÓN DE MIS PRÉSTAMOS (VISTA USUARIO CON ALERTAS) ---
    def disenar_tab_mis_libros(self):
        for w in self.tab_mis_libros.winfo_children(): w.destroy()
        
        cols = ("Título", "Fecha Límite", "Estado", "Alerta")
        tree = ttk.Treeview(self.tab_mis_libros, columns=cols, show="headings")
        for c in cols: tree.heading(c, text=c)
        tree.tag_configure("atraso", background="#ffcccc")
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        self.db.cursor.execute("""
            SELECT l.titulo, p.fecha_limite, p.estado 
            FROM prestamos p JOIN libros l ON p.libro_id=l.id 
            WHERE p.usuario_id=? AND p.estado='activo'
        """, (self.usuario_actual['id'],))
        
        hoy = datetime.now().strftime('%Y-%m-%d')
        for r in self.db.cursor.fetchall():
            tag = "atraso" if r[1] < hoy else ""
            alerta = "⚠️ FUERA DE PLAZO" if r[1] < hoy else "En tiempo"
            tree.insert("", "end", values=(r[0], r[1], r[2], alerta), tags=(tag,))

    # --- GESTIÓN DE RETORNOS (SOLO ADMIN) ---
    def disenar_tab_admin_retornos(self):
        for w in self.tab_admin_retornos.winfo_children(): w.destroy()
        ttk.Label(self.tab_admin_retornos, text="REGISTRAR DEVOLUCIONES DE USUARIOS", font=('Arial', 12, 'bold')).pack(pady=10)
        
        cols = ("ID", "Usuario", "Libro", "Fecha Límite")
        self.tree_ret = ttk.Treeview(self.tab_admin_retornos, columns=cols, show="headings")
        for c in cols: self.tree_ret.heading(c, text=c)
        self.tree_ret.pack(fill="both", expand=True, padx=10)

        self.db.cursor.execute("""
            SELECT p.id, u.nombre, l.titulo, p.fecha_limite 
            FROM prestamos p JOIN usuarios u ON p.usuario_id=u.id JOIN libros l ON p.libro_id=l.id 
            WHERE p.estado='activo'
        """)
        for r in self.db.cursor.fetchall(): self.tree_ret.insert("", "end", values=r)
        
        ttk.Button(self.tab_admin_retornos, text="MARCAR COMO DEVUELTO ✅", command=self.admin_registrar_devolucion).pack(pady=10)

    def admin_registrar_devolucion(self):
        sel = self.tree_ret.selection()
        if not sel: return
        p_id = self.tree_ret.item(sel)['values'][0]
        
        # Obtener datos para penalización
        self.db.cursor.execute("SELECT fecha_limite, usuario_id, libro_id FROM prestamos WHERE id=?", (p_id,))
        datos = self.db.cursor.fetchone()
        
        hoy = datetime.now()
        limite = datetime.strptime(datos[0], '%Y-%m-%d')
        
        # Actualizar préstamo
        self.db.cursor.execute("UPDATE prestamos SET estado='devuelto', fecha_devolucion=? WHERE id=?", (hoy.strftime('%Y-%m-%d'), p_id))
        # Devolver stock
        self.db.cursor.execute("UPDATE libros SET stock = stock + 1 WHERE id=?", (datos[2],))
        
        # Penalizar si es tarde
        if hoy > limite:
            fin_pen = (hoy + timedelta(days=7)).strftime('%Y-%m-%d')
            self.db.cursor.execute("UPDATE usuarios SET fin_penalizacion=? WHERE id=?", (fin_pen, datos[1]))
            messagebox.showwarning("Penalización", f"Devolución tardía. Usuario penalizado hasta {fin_pen}")
        
        self.db.conn.commit()
        messagebox.showinfo("OK", "Libro devuelto al inventario")
        self.mostrar_dashboard()

    # --- LÓGICA PRÉSTAMO ---
    def solicitar_prestamo(self):
        sel = self.tree_libros.selection()
        if not sel: return
        l_id = self.tree_libros.item(sel)['values'][0]
        
        # Verificar penalización
        self.db.cursor.execute("SELECT fin_penalizacion FROM usuarios WHERE id=?", (self.usuario_actual['id'],))
        pen = self.db.cursor.fetchone()[0]
        if pen and datetime.strptime(pen, '%Y-%m-%d') > datetime.now():
            return messagebox.showerror("Error", f"Tu cuenta está penalizada hasta {pen}")

        # Realizar préstamo
        hoy = datetime.now()
        lim = (hoy + timedelta(days=15)).strftime('%Y-%m-%d')
        
        self.db.cursor.execute("INSERT INTO prestamos (usuario_id, libro_id, fecha_prestamo, fecha_limite) VALUES (?,?,?,?)",
                               (self.usuario_actual['id'], l_id, hoy.strftime('%Y-%m-%d'), lim))
        self.db.cursor.execute("UPDATE libros SET stock = stock - 1 WHERE id=?", (l_id,))
        self.db.conn.commit()
        messagebox.showinfo("Éxito", "Libro prestado. Revisa 'Mis Préstamos'")
        self.mostrar_dashboard()

    # --- ADMIN: ALERTAS MORA & WHATSAPP ---
    def disenar_tab_mora(self):
        for w in self.tab_mora.winfo_children(): w.destroy()
        cols = ("Usuario", "Teléfono", "Libros Retrasados")
        t = ttk.Treeview(self.tab_mora, columns=cols, show="headings")
        for c in cols: t.heading(c, text=c)
        t.pack(fill="both", expand=True, padx=10, pady=10)

        hoy = datetime.now().strftime('%Y-%m-%d')
        self.db.cursor.execute("""
            SELECT u.nombre, u.telefono, GROUP_CONCAT(l.titulo, ', ') 
            FROM prestamos p JOIN usuarios u ON p.usuario_id=u.id JOIN libros l ON p.libro_id=l.id 
            WHERE p.estado='activo' AND p.fecha_limite < ? GROUP BY u.id
        """, (hoy,))
        for r in self.db.cursor.fetchall(): t.insert("", "end", values=r)

        def ws():
            sel = t.selection()
            if not sel: return
            n, tel, libs = t.item(sel)['values']
            msg = f"Estimado {n}, tiene pendiente: {libs}. Por favor devuélvalos."
            webbrowser.open(f"https://wa.me/{tel}?text={urllib.parse.quote(msg)}")

        ttk.Button(self.tab_mora, text="📲 ENVIAR RECORDATORIO WHATSAPP", command=ws).pack(pady=10)

    # --- ADMIN: FORMULARIO LIBROS ---
    def ventana_libro_form(self, l_id=None):
        w = tk.Toplevel(self.root); w.title("Libro"); w.geometry("400x450")
        f = ttk.Frame(w, padding=20); f.pack()
        
        lbls = ["Título", "Autor", "ISBN", "URL Portada", "Stock"]
        ents = []
        val = [""]*4 + [5]
        if l_id:
            self.db.cursor.execute("SELECT titulo, autor, isbn, url_portada, stock FROM libros WHERE id=?", (l_id,))
            val = self.db.cursor.fetchone()

        for i, txt in enumerate(lbls):
            ttk.Label(f, text=txt).pack(anchor="w")
            e = ttk.Entry(f, width=40); e.insert(0, val[i]); e.pack(pady=5)
            ents.append(e)

        def save():
            v = [e.get() for e in ents]
            if l_id: self.db.cursor.execute("UPDATE libros SET titulo=?, autor=?, isbn=?, url_portada=?, stock=? WHERE id=?", (*v, l_id))
            else: self.db.cursor.execute("INSERT INTO libros (titulo, autor, isbn, url_portada, stock) VALUES (?,?,?,?,?)", v)
            self.db.conn.commit(); w.destroy(); self.refrescar_libros()

        ttk.Button(f, text="GUARDAR", command=save).pack(pady=20)

    def editar_libro(self):
        sel = self.tree_libros.selection()
        if sel: self.ventana_libro_form(self.tree_libros.item(sel)['values'][0])

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()