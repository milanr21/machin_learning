import tkinter as tk
from tkinter import RIGHT, Tk, Button, Label, Entry, Text, Frame, Scrollbar, VERTICAL, Canvas, RAISED, Y
import random


class chatbot:
    def __init__(self, root):
        self.root = root
        self.root.geometry('700x500+300+100')
        self.root.title('Intelligent Chatbot')



        # Title of the Chatbot

        chat_title = Label(self.root, text="Intelligent Chatbot", font=('Times New Roman', 18, 'bold', ))
        chat_title.place(x=250, y=10)

        # main frame with scrollbar

        main_frame = Frame(self.root, bd=2, relief=RAISED, bg="white")
        main_frame.place(x=10, y=60, width=680, height=350)

        # scrollbar 

        self.scroll_y = Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width = 800, height =200, font=('Times New Roman', 18, 'bold'), relief=RAISED, yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()


        # search label

        search_label = Label(self.root,text="Seach Gpt-3", font=('Times New Roman', 14, 'bold'))
        search_label.place(x=10, y=430)

        # search entry

        self.entry = Entry(self.root, width=60, font=('Times New Roman', 14, 'bold'))
        self.entry.place(x=140, y=430)


        # creating button

        self.btn_search = Button(self.root, text="Search", width=10, font=('Times New Roman', 14, 'bold'))
        self.btn_search.place(x=150, y=460, height=30, width=100)

        self.btn_clear = Button(self.root, text="Clear", width=10, font=('Times New Roman', 14, 'bold'))
        self.btn_clear.place(x=290, y=460, height=30, width=100)  # Use self.btn_clear.place instead of self.btn_search.place


       

        


      
        









if __name__ == "__main__":
    root = Tk()
    obj = chatbot(root)
    root.mainloop()