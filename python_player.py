"""
    Name: python player.py
    Created: 9/29/22
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

def main():
    init()
      

def init():

    title()
    # Initialize anything here

def title():
    # Initialize main window
    root=Tk()
    root.title('Python Playlist Player')
    root.geometry("920x670+290+85")
    root.configure(bg= "#0f1a2b")
    root.resizable(False, False)
    mixer.init()

    # Put photos, icon, logo, windows, still need photo
    #Icon_Image = PhotoImage(file="logo.png")
    #root.iconphoto(False, Icon_Image =
    #PhotoImage(file="logo.png"))

    Top_Image = PhotoImage(file="background.png")
    Label(root, image=Top_Image, bg="#0f1a2b").pack()

    # Logo, still need photo
    logo_Image = PhotoImage(file="logo.png")
    Label(root, image=logo_Image, bg="#0f1a2b").place(x=65, y= 115)

    # Menu label, need image
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

    # Have commands/labels tied to buttons here

    # Resume command, need image
    Button_Resume = PhotoImage(file="resume.png")
    Button(root, image=Button_Resume, bg="#0f1a2b", bd=0,
    command=mixer.music.unpause).place(x=115, y=500)

    # Play command, need image
    Button_Play = PhotoImage(file="play.png")
    Button(root,image=Button_Play, bg="#0f1a2b", bd=0,
    command=play_music).place(x=100, y=400)

    # Pause command
    Button_Pause = PhotoImage(file="pause.png")
    Button(root, image=Button_Pause, bg="#0f1a2b", bd=0,
    command=mixer.music.pause).place(x=200, y=500)

    # Skip command

    # Select another playlist



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
    

main()