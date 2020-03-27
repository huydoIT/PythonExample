import tkinter as tk

def msg_box():
    msg = "Hello" + name.get()
    tk.messagebox.showinfo("Hello message", msg)

frm = tk.Tk()
tk.Label(frm, text="First Name").grid(row=0)
tk.Label(frm, text="Age").grid(row=1)

name = tk.Entry(frm)
name.grid(row=0, column=1)
age = tk.Entry(frm)
age.grid(row=1, column=1)

bt1 = tk.Button(frm, text="OK", command=msg_box)
bt1.grid(row=2, column=0)
bt2 = tk.Button(frm, text="Exit", command=frm.quit)
bt2.grid(row=2, column=1)

frm.minsize(300, 200)
frm.mainloop()
