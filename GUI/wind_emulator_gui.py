import urllib
import urllib.request
from urllib.request import urlopen

import tkinter as tk
import requests,json
from PIL import ImageTk, Image


def get_output(winds):
    return str(winds)



def thevalue(entry):
    apikey = "c0362b30402ccebb6f9cef35faa19984"

    api_address = "http://api.openweathermap.org/data/2.5/weather?q="+entry+"&appid="+apikey

    response = requests.get(api_address).json()
    windspeed = response['wind']['speed']
    print(windspeed,"m/s")
    print(windspeed*3.6,"kmph")
    ts=urlopen('https://api.thingspeak.com/update?api_key=F8P28NG7C4VV1I32&field1='+str(windspeed))
    #return windspeed
    label3['text'] = "The windspeed is"+" "+get_output(windspeed)+" "+"in m/s"

top = tk.Tk()
top.title('Wind Emulator')
top.iconbitmap('C:/Users/Swapnil/Downloads/443-4439156_offshore-wind-consultancy-offshore-wind-turbine-cartoon-hd.ico')


canvas = tk.Canvas(top, height=500, width=500)
canvas.pack()

label2 = tk.Label(canvas, text="Wind Speed for an area", fg='black', bg='#969595')
label2.place(relx=0.1,rely=0.03,relheight=0.36,relwidth=0.8)

#top.attributes('-alpha', 0.5)
bg_img = tk.PhotoImage(file="C:/Users/Swapnil/Downloads/wind-turbine-energy-green-ecological-power-energy-generation_34998-152.png")

bg_placing  = tk.Label(top, image=bg_img)
bg_placing.place(relwidth=1,relheight=1)
#bg = canvas.create_image(0, 0, anchor=tk.NW, image=bg_img)
#bg_placing.image=bg_img


#frame = tk.Frame(top,bg='#00569f')
#frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
#frame.attributes('-alpha', 0.5)

entry = tk.Entry(top, font=20)
entry.place(relx=0.1, rely=0.17, relwidth=0.504, relheight=0.08)

label = tk.Label(top, text="Enter city name", fg='black', bg='#969595')
label.place(relx=0.1,rely=0.10,relheight=0.06,relwidth=0.8)

button  = tk.Button(top, text="Submit", bg='#969595', command=lambda: thevalue(entry.get()))
button.place(relx=0.64, rely=0.17, relwidth=0.25, relheight=0.08)

#x = thevalue(entry.get())

#lower_frame = tk.Frame(top,bg='#5097d9',bd=5)
#lower_frame.place(relx=0.11, rely=0.65, relwidth=0.79, relheight=0.25)

#label3 = tk.Label(lower_frame,fg='black')
#label3.place(relx=0.1,rely=0.03,relheight=0.36,relwidth=0.8)

label3 = tk.Label(top,fg='black')
label3.place(relx=0.13,rely=0.63,relheight=0.16,relwidth=0.8)

top.mainloop()
