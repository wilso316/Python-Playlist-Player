from pygame import mixer
  
# Call the mixer module 
mixer.init()
  
# Load the song
mixer.music.load("D:\Comp. Sci\clair.mp3")
  
# Set the volume so it doesn't blast my ears
mixer.music.set_volume(0.7)
  
# Start playing the song
mixer.music.play()
  
# Create loop
while True:
    # Create (p)ause and (r)esume
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input("  ")
      
    if query == 'p':
  
        # Pausing the music
        mixer.music.pause()     
    elif query == 'r':
  
        # Resuming the music
        mixer.music.unpause()
    elif query == 'e':
  
        # Stop the mixer
        mixer.music.stop()
        break