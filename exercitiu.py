import tkinter as tk

balance = 2000

class Window(tk.Tk):
    def __init__(self,title, geometry):
        super().__init__()
        self.title(title)
        self.geometry(geometry)



def visa():
    suma = input_field.get()
    try:
        suma = float(suma)
        
    except TypeError:
        suma_ramasa = "Nu se poate calcula"
    finally:
        comision = 1/100*suma
        suma_ramasa = balance - suma - comision
        value_var.set(suma_ramasa)

def paypal():
    suma = input_field.get()
    try:
        suma = float(suma)
        
    except TypeError:
        suma_ramasa = "Nu se poate calcula"
    finally:
        comision = 2/100*suma
        suma_ramasa = balance - suma - comision
        value_var.set(suma_ramasa)

def master():
    suma = input_field.get()
    try:
        suma = float(suma)
        
    except TypeError:
        suma_ramasa = "Nu se poate calcula"
    finally:
        comision = 3/100*suma
        suma_ramasa = balance - suma - comision
        value_var.set(suma_ramasa)

if __name__ == "__main__":
    window = Window("Card", "600x600")


    value_var = tk.StringVar()
    value_var.set(f"Current balance: {balance}")

    label = tk.Label(window, textvariable=value_var)
    label.pack()


    input_field = tk.Entry(window)
    input_field.pack()

    button = tk.Button(window, text="Visa", command= visa)
    button.pack()
    button = tk.Button(window, text="PayPal", command= paypal)
    button.pack()
    button = tk.Button(window, text="Master", command= master )
    button.pack()


    window.mainloop()