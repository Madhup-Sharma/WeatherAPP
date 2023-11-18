import tkinter as tk
import json 
from PIL import Image, ImageTk 

# JSON Play

file = open("./weather.json", "r")

x = file.read() 
final_data = json.loads(x)       # final_data is an array I have



# Generating the Root Box
root = tk.Tk()
root.title("WEATHER APP ☁️")
root.geometry("600x500")



# Functions 

def format_response(a):

    try:
        city = a["city"]
        description = a["description"].title()
        temp = a["temp"]
        str = "City : %s 🏙️ \n Condition: %s ☁️ \n Temperature: %s 🌡️\n"%(city, description, temp)
    except:
        str = "City is not listed yet"
    return str



def getWeather(city):
    cnt = 0
    for a in final_data:
        data = a["city"]
       
        if( data== city):
            result["text"]=format_response(a)
            cnt = 1

    if(cnt == 0):
        print("City Not Listed Yet")


# Manipulating the image to fit the size

img = Image.open('./bg5.jpg')

img = img.resize((600,1000), Image.LANCZOS)

photo = ImageTk.PhotoImage(img)

bg_lbl = tk.Label(root, image=photo)
bg_lbl.place(x=0, y=0, width=600, height=500)

# Heading of the Project Feature 

heading_title = tk.Label(bg_lbl, text=" | WEATHER APP | ", fg="white",bg="black",font=('times new roman', 18, 'bold'))

heading_title.place(x=200, y=18)



# Frame in which the Search Bar and Button is being hold
frame1 = tk.Frame(bg_lbl, bg = "#161912", bd = 5)
frame1.place(x = 80,y=60, width=450, height=50)

txt_box = tk.Entry(frame1, font=('times new roman', 25),bg="#D0D4CA", width = 17)
txt_box.grid(row=0, column=0,sticky='w')

btn = tk.Button(frame1, text='Get Weather', fg='white', bg= 'black', font=('times new roman', 16, 'bold'), command = lambda: getWeather(txt_box.get()))

btn.grid(row=0, column=1, padx=10)


# Frame which will show the weather information

frame2 = tk.Frame(bg_lbl, bg = "#161912", bd = 5)
frame2.place(x = 155,y=200, width=300, height=200)

# Result Box over the Frame 2
result = tk.Label(frame2, font=40, bg="#D0D4CA")
result.place(relheight=1, relwidth=1)

root.mainloop()

# End of Program

