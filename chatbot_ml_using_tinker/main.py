import tkinter as tk
from tkinter import RIGHT, Tk, Button, Label, Entry, Text, Frame, Scrollbar, VERTICAL, Canvas, RAISED, Y, END, StringVar, ttk
import random
import openai
import os

from dotenv import load_dotenv
import openai





load_dotenv()





class chatbot:
    def __init__(self, root):
        self.root = root
        self.root.geometry('700x500+300+100')
        self.root.title('Intelligent Chatbot')
        self.root.bind('<Return>', self.ent_func)



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

        self.ent = StringVar()

        self.entry = Entry(self.root, textvariable=self.ent, width=50, font=('Times New Roman', 14, 'bold'))
        self.entry.place(x=140, y=430)


        # creating button

        self.btn_search = Button(self.root, command=self.search, text="Search", width=10, font=('Times New Roman', 14, 'bold'))
        self.btn_search.place(x=150, y=460, height=30, width=100)

        self.btn_clear = Button(self.root, command=self.clear, text="Clear", width=10, font=('Times New Roman', 14, 'bold'))
        self.btn_clear.place(x=290, y=460, height=30, width=100)  # Use self.btn_clear.place instead of self.btn_search.place


# function to search the query
        
    def ent_func(self, event):
        self.btn_search.invoke()
        self.ent.set("")
        
        
    def search(self):
        user_input = "  " + "You: " + self.entry.get().lower()
        self.text.insert(END, "\n\n" + user_input)

        input_text = self.entry.get()

        api_key = os.getenv("myAPI")

        openai.api_key = api_key

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=input_text,
            max_tokens=100
        )

        try:
            msg_reply = response["choices"][0]["text"]
            self.text.insert(END, "\n\n" + "Bot: " + msg_reply)
        except (KeyError, IndexError):
            self.text.insert(END, "\n\n" + "Bot: No response")

        
                      
        
  

    def clear(self):
        self.text.delete('1.0', END)
        self.ent.set("")











if __name__ == "__main__":
    root = Tk()
    obj = chatbot(root)
    root.mainloop()