import customtkinter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("800x600")
realfeel = 0
def get_weather():
    url = "https://www.accuweather.com/en/us/whitehouse/75791/weather-forecast/2107008"

    # Set up the Selenium webdriver
    driver = webdriver.Chrome()
    driver.get(url)

    try:
        # Wait for the temperature element to be present
        temperature_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body > div > div.two-column-page-content > div.page-column-1 > div.page-content.content-module > a.cur-con-weather-card.card-module.content-module.lbar-panel > div.cur-con-weather-card__body > div:nth-child(1) > div > div > div.temp"))
        )

        Feeltemperature_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"body > div > div.two-column-page-content > div.page-column-1 > div.page-content.content-module > a.cur-con-weather-card.card-module.content-module.lbar-panel > div.cur-con-weather-card__body > div:nth-child(1) > div > div > div.real-feel" ))
        )


        # Print the HTML content for debugging
        print(driver.page_source)

        # Extract and return the text of the temperature element

        return temperature_element.text
        
    finally:
        # Close the browser window
        driver.quit()

# App setup
app.title("Weather App")
app.resizable(0, 0)

title = customtkinter.CTkLabel(master=app, text="Today's Weather", font=("Arial", 20, "bold"))
title.pack(pady=10)

# Displaying initial weather information
initial_weather = get_weather()
weather_label = customtkinter.CTkLabel(master=app, text=initial_weather, font=("Arial", 20, "bold"))
weather_label.pack(pady=10)


# Button to refresh weather information
refresh_button = customtkinter.CTkButton(
    master=app,
    text="Refresh Weather",
    command=lambda: weather_label.configure(text=get_weather())
)
refresh_button.pack(pady=10)

app.mainloop()
