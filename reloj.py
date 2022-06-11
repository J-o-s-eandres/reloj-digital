from tkinter import Label,Tk
import time

ventana= Tk()
ventana.title("Reloj Digital Joseandres")
ventana.geometry("500x140")
ventana.resizable (1,1)
texto= ("times new roman",68,"italic")
background ="#bdecb6"
foreground ="#000000"
borde=30
Label=Label(ventana,font=texto,bg=background,fg=foreground,bd=borde)
Label.grid(row=8,column=1)
def digital_clock():
    linea_tiempo=time.strftime('%H: %M: %S ')
    Label.config(text=linea_tiempo)
    Label.after(200,digital_clock)
digital_clock()
ventana.mainloop()

