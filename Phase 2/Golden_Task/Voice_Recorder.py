# Importing the libraries
import time
from tkinter import *
from tkinter import messagebox

import sounddevice as sound
from scipy.io.wavfile import write

# Creating the Voice recorder application
root = Tk()
root.geometry("700x630")
root.title("Voice Recorder Ap")
root.resizable(False, False)


# Function for Recording the audio with frequency level set as 44100 as standard
def Record():
    freq = 44100
    dur = int(duration.get())
    record = sound.rec(dur * freq, samplerate=freq, channels=2)

    # Timer to record
    temp = int(duration.get())
    while temp >= 0:
        root.update()
        time.sleep(1)
        temp -= 1

        if temp == 0:
            messagebox.showinfo(title="Voice Recorder", message="Time's Up! Thanks for recording. Your recording is "
                                                                "saved as My_Recording.mp3")
    sound.wait()
    write("My_Recording.mp3", freq, record)


# Set the icon for the application
icon_app = PhotoImage(file="Icon_app.png")
root.iconphoto(False, icon_app)

# Set the background for the image
background_img = PhotoImage(file="Background_2.jpg")
Bg_1 = Label(root, image=background_img)
Bg_1.place(x=0, y=0)

# Logo for the application
logo_img = PhotoImage(file="Logo_app.png")
Logo_app = Label(root, image=logo_img)
Logo_app.pack(padx=200, pady=50)

# Name to display below the logo

Label(root, text="Voice Recorder App! Ready to record?", font="Magneto", background="#ADD8E6", fg="black").pack()

# Input the duration from user
duration = StringVar()
Entry(root, textvariable=duration, font="Calibra", width=10).pack(pady=5)
Label(text="Enter the time in seconds...", font="Consolas", background="#ADD8E6", fg="Black").pack(padx=10)

# Record button
Button(root, text="Record now", font="Raleway", bg="#EEEEEE", border=10, command=Record).pack(pady=20)

root.mainloop()
