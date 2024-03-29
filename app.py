from tkinter import *
from tkinter import ttk
from functools import partial

mw = Tk()
mw.title("YouTube downloader")
mw.geometry("500x500")

str_variable = StringVar()


def downloader(url):
    print(str_variable.get())


content = ttk.Frame(mw).grid(row=0, column=0)


url_label = ttk.Label(content, text="URL: ", background="#000fff000").grid(
    row=0, column=0
)
url = ttk.Entry(content, textvariable=str_variable, width=50).grid(row=0, column=1)


btn_download = ttk.Button(
    content, text="Download", command=lambda: downloader(str_variable.get())
).grid(row=1, column=3)


mw.mainloop()
