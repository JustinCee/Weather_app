from tkinter import *
import pyowm
import requests


def omw():
    api_key = 'a9ba8c17507a7e5b9fac5201e3ccfd1f'
    response = requests.get("https://api.chucknorris.io/jokes/random")
    data = response.json()
    owm_obj = pyowm.OWM(data)
    city_name = entry1.get()
    mgr = owm_obj.weather_manager()
    obs_obj = mgr.weather_at_place(city_name)
    weather = obs_obj.get_weather()
    temp = weather.get_temperature('celsius')["temp"]
    humidity = weather.get_humidity()
    description = weather.get_detailed_status()
    entry2.insert(15, str(temp) + " Celsius ")
    entry3.insert(15, str(humidity) + " %")
    entry4.insert(10, str(description))


def clear():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)


def exit1():
    window.destroy()


window = Tk()
window.title("Weather App")
window.geometry("300x500")
window.config(bg="yellow")

label = Label(window, text="Weather in your city", bg="black", fg="yellow")
label.place(x=60, y=5)
label1 = Label(window, text="Enter your city:", bg="Yellow")
label1.place(x=60, y=30)
entry1 = Entry(window)
entry1.place(x=60, y=60)

label2 = Label(window, text="Temperature", bg="yellow")
label2.place(x=60, y=150)
entry2 = Entry(window)
entry2.place(x=60, y=180)

label3 = Label(window, text="Humidity", bg="Yellow")
label3.place(x=60, y=210)
entry3 = Entry(window)
entry3.place(x=60, y=240)

label4 = Label(window, text="Description", bg="yellow")
label4.place(x=60, y=270)
entry4 = Entry(window)
entry4.place(x=60, y=300)

weather_btn = Button(window, text="Search city", fg="Yellow", bg="black")
weather_btn.place(x=60, y=90)
clear_btn = Button(window, text="Clear", fg="Yellow", bg="black", command=clear)
clear_btn.place(x=60, y=330)
ex_btn = Button(window, text="Exit", fg="Yellow", bg="black", command=exit1)
ex_btn.place(x=220, y=450)

window.mainloop()
