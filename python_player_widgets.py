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
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdire(path)

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
        image=Top_Image, bg="#0f1a2b",
        text = "Python Music Player",
        relief=GROOVE
    )
    logo_image = PhotoImage(file="logo.png")

    Button_Resume = Button(
        button_image = PhotoImage(file="resume.png"),
        command =mixer.music.unpause()
    )

    Button_Play = Button(
        button_image = PhotoImage(file="play.png"),
        command =play_music()
    )

    Button_Pause = Button(
        Button_Image = PhotoImage(file="pause.png"),
        command=mixer.music.pause()
    )

    Button_AddSong = Button(
        Button_image = PhotoImage(file="addsong.png"),
        command=add_music()
    )
root.iconbitmap("musicICO.ico")

Top_Image = PhotoImage(file="background.png")
Label(root, image=Top_Image, bg="#0f1a2b").pack()

# Logo
logo_Image = PhotoImage(file="logo.png")
Label(root, image=logo_Image, bg="#0f1a2b").place(x=65, y= 115)

# Menu label
Menu = PhotoImage(file="menu.png")
Label(root, image=Menu, bg="#0f1a2b").pack(padx=10, pady=50, side=RIGHT)

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




root.mainloop()