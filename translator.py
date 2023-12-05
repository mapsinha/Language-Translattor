from tkinter import *
from tkinter import ttk, messagebox
from translate import Translator
import googletrans
import textblob

window = Tk()
window.title("DataFlair Language Translator")
window.minsize(600,500)
window.maxsize(600,500)

def translate():
    try:
        txt = text1.get(1.0, END)
        c1 = combo1.get()
        c2 = combo2.get()
        if txt:
            translator = Translator(from_lang=c1, to_lang=c2)
            translation = translator.translate(txt)
            text2.delete(1.0, END)
            text2.insert(END, translation)
    except Exception as e:
        messagebox.showerror("Error", "An error occurred during translation. Please try again.")




language=googletrans.LANGUAGES
lang_value=list(language.values())
lang1=language.keys()
    
combo1=ttk.Combobox(window,values=lang_value,state='r')
combo1.place(x=100,y=20)
combo1.set("choose a language")



f1=Frame(window,bg='black',bd=4)
f1.place(x=100,y=100,width=150,height=150)

text1=Text(f1,font="Roboto 14",bg='white',relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=140,height=140)

combo2=ttk.Combobox(window,values=lang_value,state='r')
combo2.place(x=300,y=20)
combo2.set("choose a language")

f2=Frame(window,bg='black',bd=4)
f2.place(x=300,y=100,width=150,height=150)

text2=Text(f2,font="Roboto 14",bg='white',relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=140,height=140)

button = Button(window,text='Translate',font=('normal',15), bg='yellow', command=translate)
button.place(x=230,y=300)# button which when triggered performs translation


window.configure
window.mainloop()