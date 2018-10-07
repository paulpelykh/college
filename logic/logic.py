import tkinter as tk
from tkinter import messagebox

def to_bool(s):
	if s == 'True': return True
	elif s == 'False': return False
    
#алгоритм
def select():
    sf = "value is %s" % q_element.get()
    root.title(sf)

    q = q_element.get()
    logic = logics.get()
    p = p_element.get()

    if logic == "Заперечення":
    	messagebox.showinfo("Відповідь", str(not to_bool(q)))
    if logic == "Кон'юнкція":
    	messagebox.showinfo("Відповідь", str(to_bool(q) and to_bool(p)))
    if logic == "Диз'юнкція":
    	messagebox.showinfo("Відповідь", str(to_bool(q) or to_bool(p)))
    if logic == "Альтернативне або":
    	messagebox.showinfo("Відповідь", str(to_bool(q) ^ to_bool(p)))
    if logic == "Імплікація":
    	if q == p or (q == "False" and p == "True"):
    		messagebox.showinfo("Відповідь", "True")
    	else: messagebox.showinfo("Відповідь", "False")
    if logic == "Еквівалентність":
    	if p == q:
    		messagebox.showinfo("Відповідь", "True")
    	else: messagebox.showinfo("Відповідь", "False")
#gui
root = tk.Tk()

root.geometry("%dx%d+%d+%d" % (350, 170, 200, 150))
root.title("tk.Optionmenu as combobox")
q_element = tk.StringVar(root)
p_element = tk.StringVar(root)
logics = tk.StringVar(root)

q_element.set('True')
p_element.set('False')
logics.set("Заперечення")

q_choices = ['True', 'False']
p_choices = ['True', 'False']
logic = ["Заперечення", "Кон'юнкція", "Диз'юнкція", "Альтернативне або", "Імплікація", "Еквівалентність"]

q = tk.OptionMenu(root, q_element, *q_choices)
q.pack(side='left', padx=10, pady=1)

p = tk.OptionMenu(root, p_element, *p_choices)
p.pack(side='right', padx=10, pady=1) 

logic = tk.OptionMenu(root, logics, *logic)
logic.pack(side='left', padx=12, pady=1)

button = tk.Button(root, text="Порахувати",background="#001f3f", foreground="#fff", padx="14", pady="7", font="13", command=select)
button.place(relx=.5, rely=.9, anchor="c", height=40, width=150)

root.mainloop()