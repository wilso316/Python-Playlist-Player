"""
    Name: python_player_gui.py
    Created: 12/8
    Author: Maya Wilson
    Purpose: To create, add, play, pause and resume music using a .grid gui
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

class PythonPlayer:
    def __init__(self):

        
        self.root = Tk()
        self.playlist = []
        self.var = StringVar(self.root, value=self.playlist)
        self.root.title("Python Playlist Player")

        self.root.resizable(True, True)
        mixer.init()

        self.create_widgets()

        mainloop()
#------------------------------------------------------------------ CREATE WIDGETS ------------------------------------------------------------------#

    def create_widgets(self):
        self.main_frame = LabelFrame(
            self.root,
            
        )

       
        self.listbox = Listbox(
            self.main_frame,
            height=6,
            width=30, 
            font=("Times new roman", 10),
            listvariable=self.var,
            selectmode=SINGLE

            )
            
        

        self.btn_addsong = Button(
            self.main_frame,
            text="Add Songs",
            command=self.add_songs
        )
        self.btn_playsong = Button(
            self.main_frame,
            text="Play",
            command=self.play_song
        )
        self.btn_pausesong = Button(
            self.main_frame,
            text="Pause",
            command=self.pause_song
        )
        self.btn_resumesong = Button(
            self.main_frame,
            text="Resume",
            command=self.resume_song
        )
#------------------------------------------------------------------ GRID WIDGETS ------------------------------------------------------------------#
        self.btn_addsong.grid(row=1, column=0)
        self.btn_playsong.grid(row=1, column=1)
        self.btn_pausesong.grid(row=1, column=2)
        self.btn_resumesong.grid(row=1, column=3)

        self.main_frame.grid_configure(padx=20, pady=20)
        for widget in self.main_frame.winfo_children():
            widget.grid_configure(padx=10, pady=10)

        

    playlist = Listbox(width=100, font=("Times new roman", 10))
    
    def add_songs(self):
        path = filedialog.askdirectory()
        if path:
            os.chdir(path)
            songs = "/songs"

            for song in songs:
                if song.endswith(".mp3"):
                    self.playlist.insert(END, song)
    
    def play_song(self):
        music_name = self.playlist.get(ACTIVE)
        print(music_name[0:-4])
        mixer.music.load(self.playlist.get(ACTIVE))
        mixer.music.play()
    
    def pause_song(self):
        mixer.music.pause()
    
    def resume_song(self):
        mixer.music.unpause()
