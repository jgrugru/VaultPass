from tkinter import Frame, Listbox, Scrollbar, E


class BottomFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        vault_list = Listbox(self, height=8, width=50, border=0)
        vault_list.grid(row=0, column=0, sticky='')

        vault_list_scrollbar = Scrollbar(self)
        vault_list_scrollbar.grid(row=0, column=3, sticky=E)
        vault_list.configure(yscrollcommand=vault_list_scrollbar.set)
        vault_list_scrollbar.configure(command=vault_list.yview)
