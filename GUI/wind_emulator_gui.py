import urllib
import urllib.request
from urllib.request import urlopen

import tkinter as tk
import requests,json
from PIL import ImageTk, Image

from tkinter import *

def get_output(winds):
    return str(winds)



#master = Tk()




def thevalue(entry):
    apikey = "c0362b30402ccebb6f9cef35faa19984"

    api_address = "http://api.openweathermap.org/data/2.5/weather?q="+entry+"&appid="+apikey
    #variable = StringVar(top)
    #variable.set("one") # default value
    #response = requests.get(api_address).json()
    windspeed = response['wind']['speed']
    print(windspeed,"m/s")
    print(windspeed*3.6,"kmph")
    #ts=urlopen('https://api.thingspeak.com/update?api_key=F8P28NG7C4VV1I32&field1='+str(windspeed))
    #return windspeed
    
    #w = tk.OptionMenu(top, variable, "one", "two", "three")
    #w.place(relx=0.42, rely=0.2, relwidth=0.25, relheight=0.08)
    #w.pack()
    label3['text'] = "The windspeed is"+" "+get_output(windspeed)+" "+"in m/s"

def submit_form():
    strFile = variable.get()
    global var_2
    if(strFile == "Maharashtra"):
        var_2 = StringVar()
        var_2.set("Select City")
        w2 = tk.OptionMenu(top, var_2, "Mumbai", "Pune", "Solapur")
        w2.place(relx=0.32, rely=0.29, relwidth=0.25, relheight=0.08)
        w2.config(bg="#C2E8DC")
        w2["menu"].config(bg="#C2E8DC")
        bg_pic = PhotoImage(file="C:/Users/Swapnil/Downloads/Picture1_aa.png")
    if(strFile == "Tamil Nadu"):
        var_2 = StringVar()
        var_2.set("Chennai")
        w2 = tk.OptionMenu(top, var_2, "Chennai", "Coimbatore", "Madurai", "Vellore")
        w2.place(relx=0.32, rely=0.29, relwidth=0.25, relheight=0.08)
        w2.config(bg="#C2E8DC")
        w2["menu"].config(bg="#C2E8DC")   
        #button2 = tk.Button(top, text="Submit", command = submit_form)
        #button.place(relx=0.64, rely=0.4, relwidth=0.25, relheight=0.08)
        #TamilNadu_andIndia.png
        bg_pic = PhotoImage(file="C:/Users/Swapnil/Downloads/TamilNaduandIndia.png")
    #bg_pic = PhotoImage(file="C:/Users/Swapnil/Downloads/Picture1_aa.png")
    bg_placing.config(image=bg_pic)
    bg_placing.image = bg_pic
    bg_placing.place(relwidth=1,relheight=1)
    button2 = tk.Button(top, text="Submit", command = sub_city, bg="#C2E8DC")
    button2.place(relx=0.64, rely=0.29, relwidth=0.25, relheight=0.08)

def sub_city():
    sr2 = var_2.get()
    apikey = "c0362b30402ccebb6f9cef35faa19984"

    api_address = "http://api.openweathermap.org/data/2.5/weather?q="+sr2+"&appid="+apikey
    response = requests.get(api_address).json()
    windspeed = response['wind']['speed']
    print(windspeed,"m/s")
    print(windspeed*3.6,"kmph")
    
    #label3['text'] = "Windspeed"+str(windspeed)
    label3['text'] = "The windspeed is"+" "+str(windspeed)+" "+"in m/s"

    
top = tk.Tk()
top.title('Get Windspeed')
top.iconbitmap('C:/Users/Swapnil/Downloads/443-4439156_offshore-wind-consultancy-offshore-wind-turbine-cartoon-hd.ico')


canvas = tk.Canvas(top, height=500, width=500,bg='yellow')
canvas.pack()

label2 = tk.Label(canvas, text="Wind Speed for an area", fg='black', bg='#969595')
label2.place(relx=0.1,rely=0.03,relheight=0.36,relwidth=0.8)

#top.attributes('-alpha', 0.5)
bg_img = tk.PhotoImage(file="C:/Users/Swapnil/Downloads/India-map-en.svgaa.png")

bg_placing  = tk.Label(top, image=bg_img)
bg_placing.place(relwidth=1,relheight=1)
#bg = canvas.create_image(0, 0, anchor=tk.NW, image=bg_img)
#bg_placing.image=bg_img


#frame = tk.Frame(top,bg='#00569f')
#frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
#frame.attributes('-alpha', 0.5)

#entry = tk.Entry(top, font=20)
#entry.place(relx=0.1, rely=0.17, relwidth=0.504, relheight=0.08)

label = tk.Label(top, text="Enter city name", fg='black', bg='#C2E8DC',borderwidth=1, relief="solid")
label.place(relx=0.1,rely=0.10,relheight=0.06,relwidth=0.8)

variable = StringVar(top)
variable.set("one") # default value
#response = requests.get(api_address).json
w = tk.OptionMenu(top, variable, "Maharashtra", "Tamil Nadu", "three")
w.place(relx=0.32, rely=0.2, relwidth=0.25, relheight=0.08)
w.config(bg="#C2E8DC")
w["menu"].config(bg="#C2E8DC")
#w.pack()

#button  = tk.Button(top, text="Submit", bg='#969595', command=lambda: thevalue(entry.get()))
#button.place(relx=0.64, rely=0.17, relwidth=0.25, relheight=0.08)

#x = thevalue(entry.get())

#lower_frame = tk.Frame(top,bg='#5097d9',bd=5)
#lower_frame.place(relx=0.11, rely=0.65, relwidth=0.79, relheight=0.25)

#label3 = tk.Label(lower_frame,fg='black')
#label3.place(relx=0.1,rely=0.03,relheight=0.36,relwidth=0.8)

label3 = tk.Label(top,fg='black',bg='#C2E8DC',borderwidth=1, relief="solid")
label3.place(relx=0.13,rely=0.73,relheight=0.16,relwidth=0.8)

button = tk.Button(top, text="Submit", command = submit_form,bg="#C2E8DC")
button.place(relx=0.64, rely=0.2, relwidth=0.25, relheight=0.08)

label4 = tk.Label(top,fg='black',text="Windspeed of an Area",borderwidth=1, relief="solid",font=("Times New Roman Bold", 20))
label4.place(relx=0.1,rely=0.02,relheight=0.16,relwidth=0.8)

top.mainloop()
