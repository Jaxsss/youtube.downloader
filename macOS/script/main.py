from __future__ import unicode_literals
import os
from yt_dlp import YoutubeDL
from yt_dlp.postprocessor.common import PostProcessor
from tkinter import *
from tkinter import ttk
import tkinter as tk
import threading


# yt_dlp class
class MyLogger:
    def debug(self, msg):
        # For compatability with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


class MyCustomPP(PostProcessor):
    def run(self, info):
        self.to_screen('Doing stuff')
        return []


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


# threading for downloading one file
def thread():
    global thread
    thread = threading.Thread(target=download).start()


# threading for downloading multiple files
def thread1():
    global thread1
    thread1 = threading.Thread(target=download_multiple).start()


# download one file
def download():
    type = str(format_selection())
    url = entry.get()

    if type == "mp4":
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': '../videos' + '/mp4' + '/%(title)s.%(ext)s',
            'logger': MyLogger(),
            'progress_hooks': [my_hook]
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            button = tk.Button(master, text="File was downloaded.", command=lambda: button.grid_forget())
            button.grid(column=1, row=3)

    if type == "mp3":
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl':  "../videos" + '/mp3' + '/%(title)s.%(ext)s',
            'writethumbnail': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320'},
                {'key': 'EmbedThumbnail'},
            ],
            'logger': MyLogger(),
            'progress_hooks': [my_hook],
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            button = tk.Button(master, text="File was downloaded.", command=lambda: button.grid_forget())
            button.grid(column=1, row=3)


# download multiple files
def download_multiple():
    file_format = str(format_selection())

    list_of_urls = []
    try:
        with open("./urls.txt", "r") as file:
            for line in file:
                stripped_line = line.strip()
                list_of_urls.append(stripped_line)

            file.close()
    except:
        button = tk.Button(master, text="File urls.txt is missing.", command=lambda : button.grid_forget())
        button.grid(column=1, row=3)

    if file_format == "mp4":
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': '../videos' + '/mp4' + '/%(title)s.%(ext)s'
        }

        for x in range(len(list_of_urls)):
            url = list_of_urls[x]
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                button = tk.Button(master, text="File " + str(x + 1) + " was downloaded.", command=lambda: button.grid_forget())
                button.grid(column=1, row=3)

    if file_format == "mp3":
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '../videos' + '/mp3' + '/%(title)s.%(ext)s',
            'writethumbnail': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320'},
                {'key': 'EmbedThumbnail'},
            ],
            'logger': MyLogger(),
            'progress_hooks': [my_hook],
        }

        for x in range(len(list_of_urls)):
            url = list_of_urls[x]
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                button = tk.Button(master, text="File " + str(x + 1) + " was downloaded.", command=lambda: button.grid_forget())
                button.grid(column=1, row=3)


def format_selection():
    return type.get()

# options for dropdown menu
OPTIONS = [
    "mp3",
    "mp4"
]

# tkinter essentials
master = tk.Tk()
master.iconbitmap("./favicon.ico")
master.title("YouTube to MP3")

# dropdown menu
type = StringVar(master)
type.set(OPTIONS[0])

w = OptionMenu(master, type, *OPTIONS)
w.grid(column = 2, row = 0)

# window resize and center when opened
window_height = 150
window_width = 350
master.resizable(False, False)
screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
master.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

# buttons
input_box1 = tk.Label(master, text="YouTube URL: ").grid(column = 0, row = 0)

entry = tk.Entry(master, width=20)
entry.grid(column = 1, row = 0)

button = tk.Button(master, text="Download", command = thread)
button.grid(column = 1, row = 1)

button = tk.Button(master, text="Download multiple files", command = thread1)
button.grid(column = 1, row = 2)

master.mainloop()