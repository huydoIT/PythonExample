from tkinter import messagebox
import tkinter as tk
import frame_2 as frm

def bt_run():
    msg = "Hello " + e1.get()
    tk.messagebox.showinfo("Messages", msg)
    # messagebox.showinfo("Messages", msg)


def call_frm():
    frm


def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)


def get_sum():
    rs.delete(0, tk.END)
    res = int(n1.get()) + int(n2.get())
    rs.insert(0, res)
    # print("Result = ", res)


master = tk.Tk()
tk.Label(master, text="First Name").grid(row=0)
tk.Label(master, text="Last Name").grid(row=1)
tk.Label(master, text="Number 1").grid(row=2)
tk.Label(master, text="Number 2").grid(row=3)
tk.Label(master, text="Result", background="blue").grid(row=4, column=4)


e1 = tk.Entry(master)
e2 = tk.Entry(master)
# e1.insert(10, "Miller")
# e2.insert(10, "Jill")
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

n1 = tk.Entry(master)
n1.grid(row=2, column=1)
n2 = tk.Entry(master)
n2.grid(row=3, column=1)
rs = tk.Entry(master)
rs.grid(row=5, column=4)

tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=4,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='Test',
          command=get_sum).grid(row=4,
                                column=2,
                                sticky=tk.W,
                                pady=4)
tk.Button(master, text='Show', command=bt_run).grid(row=4,
                                                    column=1,
                                                    sticky=tk.W,
                                                    pady=4)
master.minsize(400, 300)  # (with, height)
master.title("My GUI app")
master.mainloop()

