import tkinter as tk
from tkinter import ttk, DISABLED

import requests

# root window creation using geometry and changing the window icon
root = tk.Tk()
root.title('Weather App!')
root.geometry('350x500')
root.iconphoto(True, tk.PhotoImage(file='iconsun.png'))

# creating images to appear based on conditions
clouds = tk.PhotoImage(file='clouds.png')
sun = tk.PhotoImage(file='sun.png')
rain = tk.PhotoImage(file='rain.png')
snow = tk.PhotoImage(file='snow.png')
storm = tk.PhotoImage(file='storm.png')
clear = tk.PhotoImage(file='clear.png')
unique = tk.PhotoImage(file='unique.png')

# create main frame
frame_home = ttk.Frame(root)
frame_home.pack(fill=tk.BOTH, expand=True)


def get_weather_button():
    """
    connects to openweathermap website to retrieve current weather conditions
    does not intake parameters or return anything directly, instead updates GUI fields.
    """
    weather_list = []
    # set fields to empty on click in case a new city has missing information
    current_temp_box.set("")
    feels_like_temp_box.set("")
    summary_box.set("")
    wind_speed_box.set("")
    wind_gusts_box.set("")
    # gather basic data retrieval information
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city = city_box.get()
    api_key = "5b14797d1d7cab9b7cd773e45fda379e"
    url = f'{base_url}q={city}&appid={api_key}'
    print(url)
    weather_data = requests.get(url)
    # check if accepted city
    if weather_data.status_code == 200:
        data = weather_data.json()
        for k, v in data.items():
            print(k, v)
            # find temp values in the key "main"
            if k == 'main':
                main_weather = v
                for keys, vals in main_weather.items():
                    if keys == 'temp':
                        kelvin = vals
                        celsius = round(kelvin - 273.15)
                        # convert kelvin to celsius and use degree symbol
                        current_temp_box.set(f"{celsius} {chr(176)}C")
                    elif keys == 'feels_like':
                        kelvin = vals
                        feels_like_c = round(kelvin - 273.15)
                        feels_like_temp_box.set(f"{feels_like_c} {chr(176)}C")
            # find summary of conditions (description) in key "weather"
            if k == 'weather':
                weather_list = v
                # inside list
                des = weather_list[0]['description']
                summary_box.set(des)
                # check condition key-words for appropriate image
                if "cloud" in des:
                    cloud_label = tk.Label(root, image=clouds)
                    cloud_label.place(x=0, y=300)
                elif "sun" in des:
                    sun_label = tk.Label(root, image=sun)
                    sun_label.place(x=0, y=300)
                elif "clear" in des:
                    clear_label = tk.Label(root, image=clear)
                    clear_label.place(x=0, y=300)
                elif "rain" in des or "drizzle" in des or "mist" in des:
                    rain_label = tk.Label(root, image=rain)
                    rain_label.place(x=0, y=300)
                elif "snow" in des or "sleet" in des:
                    snow_label = tk.Label(root, image=snow)
                    snow_label.place(x=0, y=300)
                elif "storm" in des:
                    storm_label = tk.Label(root, image=storm)
                    storm_label.place(x=0, y=300)
                else:
                    unique_label = tk.Label(root, image=unique)
                    unique_label.place(x=0, y=300)
            # wind speed and gusts in key "wind"
            if k == 'wind':
                wind_weather = v
                for keys, vals in wind_weather.items():
                    # convert from meter/sec to km/h
                    if keys == 'speed':
                        met_sec = vals
                        w_speed = round(met_sec * 3.6)
                        wind_speed_box.set(f"{w_speed} km/h")
                    elif keys == 'gust':
                        met_sec = vals
                        w_gusts = round(met_sec * 3.6)
                        wind_gusts_box.set(f"{w_gusts} km/h")

    # clause for invalid city
    else:
        current_temp_box.set("Error: Invalid City")


# labels - using padx and pady to create padding around the element(spacing)
ttk.Label(frame_home, text="Enter City ").grid(column=0, row=0, padx=10, pady=10)
ttk.Label(frame_home, text="Current Temp ").grid(column=0, row=4, padx=10, pady=10)
ttk.Label(frame_home, text="Feels Like Temp ").grid(column=0, row=6, padx=10, pady=10)
ttk.Label(frame_home, text="Summary ").grid(column=0, row=8, padx=10, pady=10)
ttk.Label(frame_home, text="Wind Speed ").grid(column=0, row=10, padx=10, pady=10)
ttk.Label(frame_home, text="Wind Gusts ").grid(column=0, row=12, padx=10, pady=10)

# Get weather button
ttk.Button(frame_home, text='Get Weather Data',
           command=get_weather_button).grid(column=0, row=2, columnspan=2, padx=10, pady=10, ipadx=5, ipady=5)

# Entry boxes, disabling ones that aren't to be edited by the user
city_box = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=city_box).grid(column=1, row=0)
current_temp_box = tk.StringVar()
ttk.Entry(frame_home, width=30, state=DISABLED, textvariable=current_temp_box).grid(column=1, row=4)
feels_like_temp_box = tk.StringVar()
ttk.Entry(frame_home, width=30, state=DISABLED, textvariable=feels_like_temp_box).grid(column=1, row=6)
summary_box = tk.StringVar()
ttk.Entry(frame_home, width=30, state=DISABLED, textvariable=summary_box).grid(column=1, row=8)
wind_speed_box = tk.StringVar()
ttk.Entry(frame_home, width=30, state=DISABLED, textvariable=wind_speed_box).grid(column=1, row=10)
wind_gusts_box = tk.StringVar()
ttk.Entry(frame_home, width=30, state=DISABLED, textvariable=wind_gusts_box).grid(column=1, row=12)
current_conditions_box = tk.StringVar()


root.mainloop()
