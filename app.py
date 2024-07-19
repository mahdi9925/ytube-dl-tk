from tkinter import *  # noqa: F403
from tkinter import ttk
import main
from multiprocessing import Queue
from multiprocessing import Process


# * Main window and its settings
mw = Tk()  # noqa: F405
mw.title("YouTube downloader")
mw.geometry("500x500")

url_variable = StringVar()  # noqa: F405
show_result_connection = StringVar()  # noqa: F405


def Check_internet_connection_process():
    queue = Queue()
    print("hello")
    main.check_internet_connection(queue)
    print("queue", queue.get())


def downloader(url):
    print(url_variable.get())


# * Create a frame for hold content
content = ttk.Frame(mw).grid(row=0, column=0)
content_frame = ttk.Frame(content).grid(row=1, column=1)  # noqa: F405


# * Create a Entry object for get url and its Label
url_label = ttk.Label(content, text="URL: ", background="#000fff000").grid(
    row=0, column=0
)
url = ttk.Entry(content, textvariable=url_variable, width=50).grid(row=0, column=1)

# * Create a download button and its style
btn_download = ttk.Button(
    content,
    text="Download",
    command=lambda: downloader(url_variable.get()),
).grid(row=1, column=3)


# * Create a Label object for show the result of internet connection
label_net_connection = ttk.Label(mw, text="Checking Internet Connection...")
label_net_connection.grid(row=1, column=1)

if __name__ == "__main__":
    # * create a child process process for checking internet connectivity
    process = Process(target=Check_internet_connection_process)
    process.start()

    # * Execute the Main Window
    mw.mainloop()
