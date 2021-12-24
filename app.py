"""
Backend 
"""
print(__doc__)

import tkinter

# creat a window
app = tkinter.Tk()

# fix a window size for frist opening
canvas = tkinter.Canvas(app, height=600, width=700)
canvas.pack() # you have to pack this for effect

# if you want to disable resize
app.resizable(False, False)

app.title("ZSA's app")

# background image setting
b_img = tkinter.PhotoImage(file="bimg.png")

# labeling works as PhotoShop's level

# positioning the image
b_img_label = tkinter.Label(app, image=b_img) # insert in a label
b_img_label.place(relwidth=1) # palce image in canvas backgrount as percentage 1 == 100%

# heading of the app
h1 = tkinter.Label(app, text='Weather Info', font=('Helvetica', 25, 'bold'), bg='#ffff99', bd=5) # bd is border
h1.place(x = 70, y = 10, relwidth=0.80)

# frame creating
input_frame = tkinter.Frame(app, bg = '#ffff99', bd=5)
input_frame.place(x= 0, y = 70, relwidth=1, relheight=0.1)

# creating data entry box

box = tkinter.Entry(input_frame, font= ('courier', 14))
box.place(x = 20, y=5, relwidth= 0.75, relheight= 0.75)

# creating a button for search
button_1 = tkinter.Button(input_frame, text= 'Search', font= 35)
button_1.place(x = 545, y = 2, relwidth = 0.21, relheight= 0.90)

output_frame = tkinter.Frame(app, bg= '#ffff99', bd = 5)
output_frame.place(x = 70, y= 150, relwidth = 0.80, relheight = 0.70)

info = tkinter.Label(output_frame, font=('Courier', 14), anchor='nw', justify='left', bg='white', bd=4)
info.place(relheight=1, relwidth=1)

app.mainloop()