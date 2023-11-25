import customtkinter
import requests
from bs4 import BeautifulSoup
import time
from PIL import ImageTk, Image


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1900x1900")

def button_function():
    print("button pressed")

#get weather
search = "whitehouse tx temp"
url = f"https://www.google.com/search?q={search}"
req = requests.get(url)
sav = BeautifulSoup(req.content, "html.parser")
update = sav.find("div",class_ = "BNeawe").text

#widgets

app.title("Weather App")
app.resizable(0, 0)
title = customtkinter.CTkLabel(master=app, text="Today's Weather", font=("Arial", 100, "bold"))
title.place(relx=0.5, rely=0.05, anchor=customtkinter.CENTER)
Weather = customtkinter.CTkLabel(master=app, text=update, font=("Arial", 100, "bold"))
Weather.place(relx=0.2, rely=0.16, anchor=customtkinter.CENTER)


app.mainloop()