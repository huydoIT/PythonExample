import tkinter as tk
import requests
import PyQt5 as pt

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(text="PyMi.vn checker")
        self.label.pack()
        s = "Welcome to my app!"
        self.label_2 = tk.Label(text=s)
        self.label_2.pack()
        self.label_2.grid

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        self.contents = tk.StringVar()
        self.entrythingy["textvariable"] = self.contents
        self.entrythingy.bind("<Key-Return>", self.check_site)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Check web site up/down. Enter URL:"
        self.hi_there["command"] = self.check_site
        self.hi_there.pack()

        self.quit = tk.Button(self, text="QUIT", command=root.destroy)
        self.quit.pack()

    def check_site(self, event=None):
        url = self.contents.get().strip() or "https://pymi.vn"
        if not url.startswith("http"):
            url = "http://{}".format(url)

        resp = requests.head(url, timeout=3)
        print("{} response: {}".format(url, resp.status_code))

root = tk.Tk()
app = Application(master=root)
app.master.title("My GUI App")
app.master.minsize(400, 300)
app.mainloop()
