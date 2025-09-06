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

#commands

def SaveEncrypt():
    alphabet = "qwer1tyuı2opğü3asdf4g hjk5lşiz6xcv7bÆß€₺@nmö8çQWER!'^+%&/()TYUI=OPĞ9#<Ü*?-ASDFGH_JKLŞİZ$½XCVBN>£MÖÇ0"
    jump = 5
    if entry1.get() == "" or text1.get("1.0", "end-1c") == "":
        label4.config(text="Title or Secret cannot be empty!",fg="red")
    else:
        label4.config(text="Saved!",fg="green")
        with open("Cryptography.txt", "a",encoding="utf-8") as text_file:
            text_file.write(entry1.get() + "\n")
            entry1.delete(0,tkinter.END)
            encrypted = ""
            for character in text1.get("1.0", "end-1c"):
                find = alphabet.find(character)
                create_character = (find+jump)%len(alphabet)
                new_character = alphabet[create_character]
                encrypted += new_character
            text_file.write(encrypted + "\n\n")
            text1.delete("1.0", "end-1c")

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
label4 = tkinter.Label(screen, text="",font=("Arial", 12, "bold"))
button1 = tkinter.Button(screen,width=14,height=1,text="Save&Encrypt",font=("Arial", 8),command=SaveEncrypt)
button1.pack(padx=60, pady=5)
button2 = tkinter.Button(screen,width=8,height=1,text="Decrypt",font=("Arial", 8))
button2.pack(padx=60, pady=1)
label4.pack(padx=60, pady=5)

screen.mainloop()