# import modules and global librarys

import tkinter as tk

global selector
selector = None

# zarb function

def zarb_():
    global selector
    selector = "*"

# jam function

def jam():
    global selector
    selector = "+"
    
# manfi function
    
def manfi_():
    global selector
    selector = "-"    

# devision function

def devision():
    global selector
    selector = "%"    
    
# caculate function its so importent and it wil caculate the selectors! 

def caculate():
    if selector == "+":
        result = float(number1.get()) + float(number2.get())        
        awnser = tk.Label(window , text=f"result: {result}")
        awnser.pack()
        return awnser
    
    elif selector == "*":
        result = float(number1.get()) * float(number2.get())        
        awnser = tk.Label(window , text=f"result: {result}")
        awnser.pack()
        return awnser
    
    elif selector == "-":
        result = float(number1.get()) - float(number1.get())
        awnser = tk.Label(window , text=f"result: {result}")
        awnser.pack()
        return awnser
    
    elif selector == "%":
        result = float(number1.get()) / float(number2.get())
        awnser = tk.Label(window , text=f"result: {result}")
        awnser.pack()
        return awnser
        


# design the aplicaton with tkinter

window = tk.Tk()
window.title("hooman caculate")

tk.Label(window , text="").pack()
tk.Label(window , text="welcome to hooman caculate!...").pack()

tk.Label(window , text="").pack()

number1 = tk.Entry(window)
number2 = tk.Entry(window)
number1.pack()
number2.pack()

tk.Label(window , text="").pack()

plus = tk.Button(window , text="*" , command=zarb_)
plus.pack()

zarb = tk.Button(window , text="+" , command=jam)
zarb.pack()


manfi = tk.Button(window , text="-" , command=manfi_)
manfi.pack()

taghsim = tk.Button(window , text="%" , command=devision)
taghsim.pack()

go = tk.Button(window , text="          go          " , command=caculate)
go.pack()

if __name__ == "__main__":
    window.mainloop()
