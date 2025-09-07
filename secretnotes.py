import tkinter
from PIL import Image
from PIL import ImageTk
import tkinter.font as tkFont

screen = tkinter.Tk()
screen.geometry("800x870")
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
    font = tkFont.Font(family="Arial", size=8)
    forward_jump = font.measure(entry2.get())
    if entry1.get() == "" or text1.get("1.0", "end-1c") == "" or entry2.get() == "":
        label4.config(text="Title, Secret or Master Key cannot be empty!",fg="red")
    else:
        label4.config(text="Saved!",fg="green")
        with open("Cryptography.txt", "a",encoding="utf-8") as text_file:
            text_file.write(entry1.get() + "\n")
            entry1.delete(0,tkinter.END)
            entry2.delete(0, tkinter.END)
            encrypted = ""
            for character in text1.get("1.0", "end-1c"):
                find = alphabet.find(character)
                lock_character = (find+forward_jump)%len(alphabet)
                lock_character = alphabet[lock_character]
                encrypted += lock_character
            text_file.write(encrypted + "\n\n")
            text1.delete("1.0", "end-1c")

def Decrypt():
    alphabet = "qwer1tyuı2opğü3asdf4g hjk5lşiz6xcv7bÆß€₺@nmö8çQWER!'^+%&/()TYUI=OPĞ9#<Ü*?-ASDFGH_JKLŞİZ$½XCVBN>£MÖÇ0"
    font = tkFont.Font(family="Arial", size=8)
    backward_jump = font.measure(entry2.get())
    decrypted = ""
    if entry2.get() == "" or text1.get("1.0", "end-1c") == "":
        label4.config(text="Secret or Master Key cannot be empty!",fg="red")
    else:
        for character in text1.get("1.0", "end-1c"):
            find = alphabet.find(character)
            key_character = (find - backward_jump) % len(alphabet)
            key_character = alphabet[key_character]
            decrypted += key_character
            text1.delete("1.0", "end-1c")
            text1.insert("1.0",decrypted)
        entry2.delete(0, tkinter.END)
        label4.config(text="Decrypted!", fg="green")

#labels&entries&buttons

label1 = tkinter.Label(screen, text="Enter Your Title",font=("Arial", 12, "bold"))
label1.pack(padx=60, pady=0)
entry1 = tkinter.Entry(screen,width=32,font=("Arial",12,"bold"))
entry1.pack(padx=60, pady=5)
label2 = tkinter.Label(screen, text="Enter Your Secret",font=("Arial", 12, "bold"))
label2.pack(padx=60, pady=5)
text1 = tkinter.Text(screen, width=36, height=24,font=("Arial", 12,"bold"))
text1.pack(padx=60, pady=5)
label3 = tkinter.Label(screen, text="Enter Your Master Key",font=("Arial", 12, "bold"))
label3.pack(padx=60, pady=5)
entry2 = tkinter.Entry(screen,width=32)
entry2.pack(padx=60, pady=5)
label4 = tkinter.Label(screen, text="",font=("Arial", 12, "bold"))
button1 = tkinter.Button(screen,width=14,height=1,text="Save&Encrypt",font=("Arial", 8),command=SaveEncrypt)
button1.pack(padx=60, pady=5)
button2 = tkinter.Button(screen,width=8,height=1,text="Decrypt",font=("Arial", 8),command=Decrypt)
button2.pack(padx=60, pady=1)
label4.pack(padx=60, pady=5)

screen.mainloop()