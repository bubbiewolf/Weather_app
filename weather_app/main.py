import customtkinter
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageTk, ImageSequence
from io import BytesIO

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1900x1900")

def button_function():
    print("button pressed")

# Get weather
search = "whitehouse tx temp"
url = f"https://www.google.com/search?q={search}"
req = requests.get(url)
sav = BeautifulSoup(req.content, "html.parser")
update = sav.find("div", class_="BNeawe").text

# Load the GIF file using Pillow

gif_path = "/home/evan/Documents/weather_app/BG.gif"
gif = Image.open(gif_path)
gif_frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]

# Display the GIF frames in a label (set the label as the background image)
gif_label = customtkinter.CTkLabel(master=app)
gif_label.place(relwidth=1, relheight=1, relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

# Function to play the GIF
def play_gif(frame_index):
    if frame_index < len(gif_frames):
        gif_label.config(image=gif_frames[frame_index])
        app.after(100, lambda: play_gif(frame_index + 1))

# Schedule the GIF to start playing after a delay
app.after(1000, lambda: play_gif(0))  # Start from the first frame

app.title("Weather App")
app.resizable(0, 0)
title = customtkinter.CTkLabel(master=app, text="Today's Weather", font=("Arial", 100, "bold"))
title.place(relx=0.5, rely=0.05, anchor=customtkinter.CENTER)
weather_label = customtkinter.CTkLabel(master=app, text=update, font=("Arial", 100, "bold"))
weather_label.place(relx=0.2, rely=0.16, anchor=customtkinter.CENTER)

app.mainloop()


