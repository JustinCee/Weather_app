# importing modules needed
from configparser import ConfigParser
import requests
from tkinter import *
from tkinter import messagebox

# configuration file needed for my weather api
config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['gfg']['api']
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'


# Functions below is for the weather, clear button and my exit button
def getweather(city):
    result = requests.get(url.format(city, api_key))

    if result:
        json = result.json()
        city = json['name']
        country = json['sys']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15.__round__()
        weather1 = json['weather'][0]['main']
        final = [city, country, temp_kelvin, temp_celsius.__round__(), weather1]
        return final
    else:
        print("NO Content Found")


def search():
    city = city_text.get()
    weather = getweather(city)
    if weather:
        location_lbl.config(text='{} ,{}'.format(weather[0], weather[1]))
        temperature_label.configure(text=str(weather[3]) + " Degree Celsius")
        weather_l.config(text=weather[4])
    else:
        messagebox.showerror('Error', "Cannot find {}".format(city))


def clear():
    city_entry.delete(0, END)


def exit1():
    app.destroy()


# this is to create the window of my tkinter program
app = Tk()
app.title("Weather App")
app.geometry("1000x200")
app.config(bg="yellow")

# Below is my labels, entries and buttons needed for my program
city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()
Search_btn = Button(app, text="Search Weather", width=12, command=search, fg="Yellow", bg="black")
Search_btn.pack()

location_lbl = Label(app, text="Location", font={'bold', 20}, bg="yellow")
location_lbl.pack()
temperature_label = Label(app, text="", bg="yellow")
temperature_label.pack()
weather_l = Label(app, text="", bg="yellow")
weather_l.pack()

clear_btn = Button(app, text="Clear", bg="black", fg="yellow", command=clear)
clear_btn.place(x=10, y=150)
exit_btn = Button(app, text="Exit", fg="Yellow", bg="black", command=exit1)
exit_btn.place(x=920, y=150)

app.mainloop()
