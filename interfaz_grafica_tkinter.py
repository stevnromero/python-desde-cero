"""import tkinter as tk 

apk = tk.Tk()
apk.title("hello babrbie girl")
apk.geometry("300x500") # anchoxalto
apk.configure(background = "black")


# establecer propiedades de la ventana

tk.Wm.wm_title(apk, "hello adriana")
entrada = tk.StringVar(apk)
palabra = tk.StringVar(apk)
apk.config(background = "yellow")
apk.geometry("400x400+100+200")
apk.resizable(width= True, height= False)


def amiga():
    print(entrada.get())

def today():
    palabra.set(entrada.get())



# creamos los widgets

boton = tk.Button(apk, text="pulsa aqui", font= (12),command= amiga , bg= "green", fg= "white")
etiqueta = tk.Label(apk, text="hello rock!", font=(15), bg="black", fg= "white",justify="center")
entrada = tk.Entry(apk, font=(17), bg= "orange", fg= "white", justify= "center")


# orgranizar widgets

etiqueta.pack(fill= tk.BOTH, expand= False)
boton.pack(fill= tk.BOTH, expand= True)
entrada.pack(fill= tk.BOTH, expand= True)

apk.mainloop()"""







"""x = 12
y = 3
set = print(int(x + y))


tk.Button(
    apk,
    text = "click me",
    font = (13),
    bg = "#0049e8",
    fg = "white",
    command= set
).pack(
    fill = tk.BOTH,
    expand= True
  
)
apk.mainloop()"""


"""import tkinter as tk

saludo = tk.Tk()
tk.Wm.wm_title(saludo, "hello adriana")
entry = tk.StringVar(saludo)
word = tk.StringVar(saludo)
saludo.geometry("300x400")
saludo.config(background = "blue")
saludo.attributes("-alpha", 1)

def otty():
    print(entry.get())

def otto():
    word.set(entry.get())

boton = tk.Button(saludo, text="pulsa aqui", font= (12),command= otty , bg= "green", fg= "white")
etiqueta = tk.Label(saludo, text="hello world",font= (12), bg= "orange", fg= "white", justify= "center")
entrada = tk.Entry(saludo, font=(17), bg= "red", fg= "white", justify= "center", textvariable= entry)

boton.pack(fill= tk.BOTH, expand= True)
etiqueta.pack(fill= tk.BOTH, expand= True)
entrada.pack(fill= tk.BOTH, expand= True)

saludo.mainloop()
"""

# ejercicio 1
"""import tkinter as tk

ventana = tk.Tk()


tk.Wm.wm_title(ventana,("😂" , "holla andrea"))
amiga = tk.StringVar(ventana)
amiga_2 = tk.StringVar(ventana)
ventana.geometry("700x300")
ventana.config(background="black")
ventana.resizable(width= 0, height=0)


def saludo():
    print(amiga.get())

def otto():
    amiga_2.set(amiga.get())



etiqueta = tk.Label(ventana, text= "andrea, eres mi novia",font=("Arial", 10), bg= "green", fg="black")
boton = tk.Button(ventana, text= "pulsa el botón!", font= ("Times new roman", 18), bg = "blue", fg = "white", command= saludo)
entrada = tk.Entry(ventana, text= "pulsa el botón!", font= ("Times new roman", 18), bg = "yellow", fg = "blue", textvariable= amiga)


etiqueta.pack(fill= tk.BOTH, expand= True, pady= 10)
boton.pack(fill= tk.BOTH, expand= True)
entrada.pack(fill= tk.BOTH, expand= True)
ventana.mainloop()
"""

# crear barras de menú

"""import tkinter as tk
from tkinter import Menu

# Create the main window
parent = tk.Tk()
parent.title("Spyder (Python 3.6)")

# Create a menu bar
menu_bar = Menu(parent)
parent.config(menu=menu_bar)

# Create a File menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add menu items to the File menu
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=parent.quit)

# Create an Edit menu
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Add menu items to the Edit menu
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")

# Create a Help menu
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Add menu items to the Help menu
help_menu.add_command(label="About Spyder")

# Start the Tkinter event loop
parent.mainloop()
"""


"""import tkinter as web

ventana = web.Tk()
ventana.title("buenas tardes a todos!")
ventana.config(background= "yellow")
ventana.geometry("300x400")

barra_menu = web.Menu(ventana)
menu_archivo =web.Menu(barra_menu, tearoff= 0)
menu_archivo.add_command(label= "file")
menu_archivo.add_separator()
menu_archivo.add_command(label="copiar")
menu_archivo.add_separator()
menu_archivo.add_command(label="salir", command= ventana.quit)


menu_archivo2 = web.Menu(barra_menu,tearoff= 0)
menu_archivo2.add_command(label= "investigar")
menu_archivo2.add_separator()
menu_archivo2.add_command(label= "indicios")
menu_archivo2.add_separator()
menu_archivo2.add_command(label= "detalles")


barra_menu.add_cascade(label="file", menu= menu_archivo)
barra_menu.add_cascade(label="about", menu= menu_archivo2)


ventana.config(menu=barra_menu)
ventana.mainloop()"""


# CREAR IMAGENES

"""import tkinter as tk
from PIL import Image, ImageTk

ventana = tk.Tk()
ventana.title("hello world")
ventana.configure(bg="red")
ventana.geometry("300x600")

imagen = Image.open("fc barcelona.png")
imagen_2 = ImageTk.PhotoImage(imagen)

imagen_label = tk.Label(ventana, image= imagen_2)
imagen_label.pack()

ventana.mainloop()"""


# ejercicio con inicio sesion y contraseña
"""
import tkinter as tk
from tkinter import messagebox

# Function to validate the login
def validate_login():
    userid = username_entry.get()
    password = password_entry.get()

    # You can add your own validation logic here
    if userid == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
parent = tk.Tk()
parent.title("Login Form")

# Create and place the username label and entry
username_label = tk.Label(parent, text="Userid:")
username_label.pack()

username_entry = tk.Entry(parent)
username_entry.pack()

# Create and place the password label and entry
password_label = tk.Label(parent, text="Password:")
password_label.pack()

password_entry = tk.Entry(parent, show="*")  # Show asterisks for password
password_entry.pack()

# Create and place the login button
login_button = tk.Button(parent, text="Login", command=validate_login)
login_button.pack()

# Start the Tkinter event loop
parent.mainloop()"""

"""
import tkinter as tk

# Function to update the display
def update_display(value):
    current_text = display_var.get()
    if current_text == "0":
        display_var.set(value)
    else:
        display_var.set(current_text + value)

# Function to clear the display
def clear_display():
    display_var.set("0")

# Function to evaluate the expression and display the result
def calculate_result():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")

# Create the main window
parent = tk.Tk()
parent.title("Calculator")

# Create a variable to store the current display value
display_var = tk.StringVar()
display_var.set("0")

# Create the display label
display_label = tk.Label(parent, textvariable=display_var, font=("Arial", 24), anchor="e", bg="lightgray", padx=10, pady=10)
display_label.grid(row=0, column=0, columnspan=4)

# Define the button layout
button_layout = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Create and place the buttons
for (text, row, col) in button_layout:
    button = tk.Button(parent, text=text, padx=20, pady=20, font=("Arial", 18),
                       command=lambda t=text: update_display(t) if t != "=" else calculate_result())
    button.grid(row=row, column=col)

# Create a Clear button
clear_button = tk.Button(parent, text="C", padx=20, pady=20, font=("Arial", 18), command=clear_display)
clear_button.grid(row=5, column=0, columnspan=3)

# Start the Tkinter event loop
parent.mainloop()

"""
"""
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

nombre = "alejandra"
dulce = "bon bon bum"

def amistad(respuesta):
    if respuesta.lower() == "si":
        messagebox.showinfo("Respuesta", f"¡{nombre}! Acepto compartir {dulce} contigo 😊🍭")
    elif respuesta.lower() == "no":
        messagebox.showerror("Respuesta", f"No lo siento mucho, perdoname 😢")
    else:
        messagebox.showwarning("Advertencia", "Por favor elige SI o NO")

window = tk.Tk()
window.title("Bienvenido al amor")
window.geometry("600x450")



etiqueta = tk.Label(window, text=f"hola {nombre}, como estas amiga?.\n ya llevamos 1 año de nuestra amistad", bg="black", font=("Arial", 17), fg="white")
etiqueta.pack(fill=tk.BOTH, expand= True)

# creamo la etiqueta
imagen = Image.open("amistad.jpg")
imagen_2 = ImageTk.PhotoImage(imagen)
etiqueta_2 = tk.Label(window, image= imagen_2)
etiqueta_2.pack(fill=tk.BOTH)


etiqueta_1 = tk.Label(window, text=f"{nombre}, ¿compartamos {dulce}?😊💕", bg= "black", font=("Arial", 17), fg="white")
etiqueta_1.pack(fill=tk.BOTH)




# Botones que pasan la respuesta a la función
si = tk.Button(window, text="SI", command=lambda: amistad("si"), justify="left")
no = tk.Button(window, text="NO", command=lambda: amistad("no"), justify="right")

si.pack(fill=tk.BOTH)
no.pack(fill=tk.BOTH)

window.mainloop()"""


import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

nombre = input("ingresa tu nombre: ")
confirmacion = "graduacion"

def Graduation(respuesta):
    if respuesta.lower() == "si":
        messagebox.showinfo("Respuesta", f"Acepto asistir a la {confirmacion} contigo! 😊")
    elif respuesta.lower() == "no":
        messagebox.showerror("Respuesta", f"No lo siento mucho, perdoname! 😢")
    else:
        messagebox.showwarning("Advertencia", "Por favor elige SI o NO")

window = tk.Tk()
window.title("Bienvenido al amor")
window.geometry("600x450")

etiqueta = tk.Label(window, text=f"hola {nombre}.", bg="black", font=("Arial", 17), fg="white")
etiqueta.pack(fill=tk.BOTH)

etiqueta_1 = tk.Label(window, text=f"{nombre}, quieres ir a mi {confirmacion} en GENERATION COLOMBIA?😊💕", bg= "red", font=("Arial", 17), fg="white")
etiqueta_1.pack(fill=tk.BOTH, expand= True)

# Botones que pasan la respuesta a la función
si = tk.Button(window, text="SI", command=lambda: Graduation("si"), justify="left")
no = tk.Button(window, text="NO", command=lambda: Graduation("no"), justify="right")

si.pack(fill=tk.BOTH)
no.pack(fill=tk.BOTH)

imagen = Image.open("graduar oso.jpg")
imagen_2 = ImageTk.PhotoImage(imagen)
etiqueta_2 = tk.Label(window, image= imagen_2, background= "#26DEC6")
etiqueta_2.pack(fill=tk.BOTH)

window.mainloop()