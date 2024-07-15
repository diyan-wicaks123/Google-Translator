from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator
import textblob

root = Tk()
root.title("Google Translator")
root.geometry("1080x400")

def Label_change():
    c = combo1.get()
    c1 = combo2.get()
    Label1.configure(text=c)
    Label2.configure(text=c1)
    root.after(1000, Label_change)

def translate_now():
    global language
    try:
        text_ = text1.get(1.0, END)
        c2 = combo1.get()
        c3 = combo2.get()
        if text_:
            translator = Translator()
            words = translator.translate(text_, src=c2, dest=c3)
            text2.delete(1.0, END)
            text2.insert(END, words.text)
    except Exception as e:
        messagebox.showerror("Googletrans", "Please try again")

# icon
image_icon = PhotoImage(file="logo1.png")
root.iconphoto(False, image_icon)

# arrow
arrow_image = PhotoImage(file="logo2.png")
Image_label = Label(root, image=arrow_image, width=150)
Image_label.place(x=460, y=50)

language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("ENGLISH")

Label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
Label1.place(x=10, y=50)

f = Frame(root, bg="Black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

Scrollbar1 = Scrollbar(f)
Scrollbar1.pack(side="right", fill="y")

Scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=Scrollbar1.set)

combo2 = ttk.Combobox(root, values=languageV, font="Robot 14", state="r")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")

Label2 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
Label2.place(x=620, y=50)

f1 = Frame(root, bg="Black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

Scrollbar2 = Scrollbar(f1)
Scrollbar2.pack(side="right", fill="y")

Scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=Scrollbar2.set)

# translate button
translate = Button(root, text="Translate", font="Roboto 15 bold italic", activebackground="purple", cursor="hand2",
                   bd=5, bg="red", fg="white", command=translate_now)
translate.place(x=480, y=250)

Label_change()

root.configure(bg="white")
root.mainloop()
