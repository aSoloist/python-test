from zzuutils import zzu_select
from tkinter import *


class SearchFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create()

    def create(self):
        self.helloLable = Label(self, text='hello')
        self.helloLable.pack()
        self.quitButton = Button(self, text='quit', command=self.quit)
        self.quitButton.pack()


search = SearchFrame()
search.master.title('aaaaaaaaaaa')
search.mainloop()
