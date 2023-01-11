# importing modules
import time
from tkinter import *
from tkinter import messagebox as mb
import requests
from plyer import notification

# creating the window
wn = Tk()
wn.title(" Weather Alert")
wn.geometry('700x200')
wn.config(bg='DarkSeaGreen1')

# Heading label
Label(wn, text="My Weather Desktop Notifier", font=('Courier', 15), fg='black', bg='DarkSeaGreen1').place(x=100, y=15)

# Getting the city name
Label(wn, text='Enter the Location:', font=("Courier", 13), bg='DarkSeaGreen1').place(relx=0.05, rely=0.3)

place = StringVar(wn)
place_entry = Entry(wn, width=50, textvariable=place)
place_entry.place(relx=0.5, rely=0.3)


def getNotification():
    cityName = place.get()  # getting input of name of the place from user
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"  # base url from where we extract weather report
    try:
        # This is the complete url to get weather conditions of a city
        url = baseUrl + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + cityName
        response = requests.get(url)  # requesting for the the content of the url
        x = response.json()  # converting it into json
        y = x["main"]  # getting the "main" key from the json object

        # getting the "temp" key of y
        temp = y["temp"]
        temp -= 273# converting temperature from kelvin to celsius

        # storing the value of the "pressure" key of y
        pres = y["pressure"]

        # getting the value of the "humidity" key of y
        hum = y["humidity"]

        vis = x["visibility"]
        print(vis)
        # storing the value of "weather" key in variable z
        z = x["weather"]

        # getting the corresponding "description"
        weather_desc = z[0]["description"]

        # combining the above values as a string
        info = "Hi! Charvi ,Weather of " + cityName.capitalize() + ":" + "\nTemperature = " + str(
            int(temp)) + "°C" + " pressure = " + str(int(pres / 1)) + " mb" + " humidity = " + str(
            hum) + " visibility = " + str(vis) + "%" + "\nWeather Desc = " + str(weather_desc)

        # showing the notification
        notification.notify(
            title="YOUR WEATHER REPORT",
            message=info,

            app_icon="download.ico",

            # displaying time
            timeout=2)
        # waiting time
        time.sleep(7)

    except Exception as e:
        mb.showerror('Error')


# Button to get notification
Button(wn, text='Get Notification', font=7, fg='grey19', command=getNotification).place(relx=0.4, rely=0.75)

# run the window till the closed by user
wn.mainloop()

# Function to get notification of weather report
# show pop up message if any error occurred
