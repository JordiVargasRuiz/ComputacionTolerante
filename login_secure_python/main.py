import tkinter as tk
from tkinter import messagebox
from auth import autenticar
from errors import *

# FUNCIÓN LOGIN
def login():
    usuario = entry_user.get()
    password = entry_pass.get()

    try:
        autenticar(usuario, password)
        messagebox.showinfo("Acceso concedido", "Bienvenido al sistema Computolellas")

    except EmptyFieldError:
        messagebox.showwarning("Campos vacíos", "Completa todos los campos")

    except InvalidCredentialsError:
        messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos")

    except AccountLockedError:
        messagebox.showerror("Cuenta bloqueada", "Demasiados intentos fallidos")

    except Exception as e:
        messagebox.showerror("Error crítico", str(e))


#VENTANA PRINCIPAL
root = tk.Tk()
root.title("Secure Login Simulator")
root.geometry("420x360")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

#CONTENEDOR CENTRAL
frame = tk.Frame(root, bg="#2a2a40", padx=25, pady=25)
frame.place(relx=0.5, rely=0.5, anchor="center")

#TITULO
tk.Label(
    frame,
    text="ACCESO DE SEGURIDAD",
    fg="#00d4ff",
    bg="#2a2a40",
    font=("Segoe UI", 18, "bold")
).pack(pady=(0, 20))

#USUARIO
tk.Label(
    frame,
    text="Usuario",
    fg="white",
    bg="#2a2a40",
    font=("Segoe UI", 10)
).pack(anchor="w")

entry_user = tk.Entry(
    frame,
    font=("Segoe UI", 11),
    bg="#1e1e2f",
    fg="white",
    insertbackground="white",
    relief="flat"
)
entry_user.pack(fill="x", pady=(5, 15))

#CONTRASEÑA
tk.Label(
    frame,
    text="Contraseña",
    fg="white",
    bg="#2a2a40",
    font=("Segoe UI", 10)
).pack(anchor="w")

entry_pass = tk.Entry(
    frame,
    show="●",
    font=("Segoe UI", 11),
    bg="#1e1e2f",
    fg="white",
    insertbackground="white",
    relief="flat"
)
entry_pass.pack(fill="x", pady=(5, 20))

# BOTÓN
btn_login = tk.Button(
    frame,
    text="INICIAR SESIÓN",
    font=("Segoe UI", 11, "bold"),
    bg="#00d4ff",
    fg="#1e1e2f",
    relief="flat",
    cursor="hand2",
    command=login
)
btn_login.pack(fill="x", pady=(10, 5))

# FOOTER
tk.Label(
    frame,
    text="Sistema con manejo de errores y seguridad",
    fg="#aaaaaa",
    bg="#2a2a40",
    font=("Segoe UI", 8)
).pack(pady=(15, 0))

root.mainloop()
