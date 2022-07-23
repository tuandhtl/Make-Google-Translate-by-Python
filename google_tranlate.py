from cProfile import label
from gettext import translation
from tkinter import *
from turtle import clear
import googletrans
from googletrans import Translator

window = Tk()
window.title("Google Translate")
window.geometry("400x500")
window.resizable(False,False)

def clear():
    text_input.delete(1.0,END)
    text_output.delete(1.0,END)

def trans():
    src_lang = 'en'
    dest_lang = 'vi'
    if (x.get()) == 0:
        src_lang = 'en'
        dest_lang = 'vi'
    elif (x.get()) == 1:
         src_lang = 'vi'
         dest_lang = 'en'
    else:
        pass        
    in_put = text_input.get(1.0,END)
    trans_late = Translator()
    out_put = trans_late.translate(text=in_put, src=src_lang, dest=dest_lang)
    text_output.insert(END, out_put.text)


lbl = Label(window, text="Google Translate", font='arial 20', fg='black')
lbl.place(x=90,y=20)

frame_input = LabelFrame(window, text= "Input")
frame_input.place(x=40,y=70)

text_input = Text(frame_input, width= 35, height=6, font='arial 12')
text_input.pack()

frame_output = LabelFrame(window, text= "Output")
frame_output.place(x=40,y=200)

text_output = Text(frame_output, width= 35, height=6, font='arial 12')
text_output.pack()

frame_option = LabelFrame(window, text="Options")
frame_option.place(x=40,y=350)

lang = ["English to Vietnamese", "Vietnamese to English"]
x= IntVar()
x.set('0')

for index in range(len(lang)):
    radiobutton = Radiobutton(frame_option, text=lang[index], variable=x, value=index, font='arial 10')
    radiobutton.pack(anchor= W)


btn_trans = Button(window, text="Translate", width=15, command=trans)
btn_trans.place(x=247,y=358)

btn_clear = Button(window, text="Clear", width=15, command=clear)
btn_clear.place(x=249,y=395)


window.mainloop()
