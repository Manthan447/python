# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 12:12:55 2022

@author: Arya Berde
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Planet Encyclopedia")
root.geometry("600x400")
root.configure( bg = "lightblue")

planets = ["Mercury", "Venus", "Earth"]
Selected_value = StringVar()


Dropdown = ttk.Combobox(root, values = planets, textvariable = Selected_value)
Dropdown.place(relx = 0.5, rely = 0.1, anchor = CENTER)
Mercury = ImageTk.PhotoImage(Image.open("mercury.jpg"))
Venus = ImageTk.PhotoImage(Image.open("venus.jpg"))
Earth = ImageTk.PhotoImage(Image.open("earth.jpg"))

Planets = Label(root, text = "Planets : ", font = ("castellar"), bg = "lightblue")
Planets.place(relx = 0.2, rely = 0.1, anchor = CENTER)
Planet_name = Label(root, font = ("Courier", 18, "bold"), bg = "lightblue")
Planet_name.place(relx = 0.5, rely = 0.25, anchor = CENTER)
Planet_Image = Label(root, bg = "gold2", highlightthickness = 5, borderwidth = 2, relief = SOLID)
Planet_Image.place(relx = 0.5, rely = 0.5, anchor= CENTER)
Gravity_radius = Label(root , font = ("Impact"), bg = "lightblue")
Gravity_radius.place(relx = 0.5, rely = 0.8, anchor=CENTER)
label_info = Label(root, text = "", bg = "lightblue", font= ("castellar", 10, "bold"), wrap = 500)
label_info.place(relx = 0.5, rely = 0.9, anchor=CENTER)



def planet_info():
    planet = Selected_value.get()
    if planet == "Mercury":
        Planet_name["text"]= "Mercury"
        Planet_Image["image"]= Mercury
        Gravity_radius["text"]= "Gravity : 3.7 m/s² \n Radius : 2,439.7 km"
        label_info["text"] = "Mercury is the smallest planet in our solar system. It's just a little bigger than Earth's moon"
    elif planet == "Venus":
        Planet_name["text"]= "Venus"
        Planet_Image["image"]= Venus
        Gravity_radius["text"]= "Gravity : 8.87 m/s² \n Radius : 6,051.8 km"
        label_info["text"] = "Venus is the brightest object in the sky after the Sun and the Moon, and sometimes looks like a bright star in the morning or evening sky"    
    elif planet == "Earth":
            Planet_name["text"]= "Earth"
            Planet_Image["image"]= Earth
            Gravity_radius["text"]= "Gravity : 9.807 m/s² \n Radius : 6,371 km"
            label_info["text"] = "Earth is the only place in the known universe confirmed to host life and it's the only one known for sure to have liquid water on its surface"
btn = Button(root, text = "Show Planet Info", command=planet_info)
btn.place(relx = 0.5, rely = 0.18, anchor=CENTER)    
root.mainloop()