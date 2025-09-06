import tkinter
from PIL import Image, ImageTk

from PIL import ImageTk

screen = tkinter.Tk()
screen.geometry("800x800")
screen.title("Secret Notes")

#label of image

image = Image.open("topsecret.png")
resized_image = image.resize((100, 100))
img = ImageTk.PhotoImage(resized_image)
img_label = tkinter.Label(screen, image=img)
img_label.pack(padx=60, pady=20)

#labels&entries&buttons

label1 = tkinter.Label(screen, text="Enter Your Title",font=("Arial", 12, "bold"))
label1.pack(padx=60, pady=0)
entry1 = tkinter.Entry(screen,width=32)
entry1.pack(padx=60, pady=5)
label2 = tkinter.Label(screen, text="Enter Your Secret",font=("Arial", 12, "bold"))
label2.pack(padx=60, pady=5)
text1 = tkinter.Text(screen, width=36, height=24)
text1.pack(padx=60, pady=5)
label3 = tkinter.Label(screen, text="Enter Your Master",font=("Arial", 12, "bold"))
label3.pack(padx=60, pady=5)
entry2 = tkinter.Entry(screen,width=32)
entry2.pack(padx=60, pady=5)
button1 = tkinter.Button(screen,width=14,height=1,text="Save&Encrypt",font=("Arial", 8))
button1.pack(padx=60, pady=5)
button2 = tkinter.Button(screen,width=8,height=1,text="Decrypt",font=("Arial", 8))
button2.pack(padx=60, pady=1)

screen.mainloop()