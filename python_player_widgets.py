"""
    Name: python player.py
    Created: 11/17/22
    Author: Maya Wilson
    Purpose: To create, add, play, pause and resume music
    Pseudocode: 
    Import Tkinter
    Def functions, main, title, add_music, player
        Create buttons, add images
    Later, add album art 
"""
# Import tkinter and pygame modules
from re import A
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer
import os


# Initialize main window
root=Tk()
root.title('Python Playlist Player')
root.geometry("1000x900+290+85")
root.configure(bg= "#0f1a2b")
root.resizable(True, True)
mixer.init()


def add_music():
    # Ask user for directory/folder of songs
    songs = "C:\Users\mayaw\Documents\Python-Playlist-Player\songs"

    for song in songs:
        if song.endswith(".mp3"):
            Playlist.insert(END, song)

    # Create list of songs

def play_music():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()
    # Play music of active playlist
    
def create_widgets():
    # Create main label frame to hold widgets
    main_frame = LabelFrame(
        root,
        #image = PhotoImage(file="menu.png"), bg="#0f1a2b",
        text = "Python Music Player",
        relief=GROOVE
    )
    entry = Entry(
        main_frame,
        width = 10
    )

    logo_image = PhotoImage(file="logo.png")
    Button_logo = Button(image = logo_image)

    resume_image = PhotoImage(file="resume.png"),
    Button_Resume = Button(
        image = resume_image,
        command =mixer.music.unpause()
    )

    button_image = PhotoImage(file="play.png"),
    Button_Play = Button(
        image = button_image,
        command =play_music()
    )

    pause_Image = PhotoImage(file="pause.png"),
    Button_Pause = Button(
        image = pause_Image,
        command=mixer.music.pause()
    )

    addsong_image = PhotoImage(file="addsong.png"),
    Button_AddSong = Button(
        image = addsong_image,
        command=add_music()
    )

    # Use Grid layout manager to place widgets in frame
    entry.grid(row=0, column=0)
    Button_logo.grid(row=0, column=0)
    Button_Play.grid(row=0, column=1)
    Button_Pause.grid(row=0, column=2)
    Button_Resume.grid(row=0, column=3)
    Button_AddSong.grid(row=0, column=4)

    main_frame.grid_configure(padx=20, pady=20)

    for widget in main_frame.winfo_children():
        widget.grid_configure(padx=10, pady=10)

    entry.focus_set()



Frame_Music = Frame(root, bd=2, relief = RIDGE)
Frame_Music.place(x=330, y=350, width=560, height=250)

# Scroll
Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman",10), bg="#333333", fg="grey",
selectbackground="lightblue", cursor="hand2", bd=0,
yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill =Y)
Playlist.pack(side=LEFT, fill=BOTH)


create_widgets()



root.mainloop()