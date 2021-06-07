from tkinter import Frame, Label


class TitleFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        vault_label = Label(self,
                            text="VaultPass",
                            font=("bold", 17),
                            pady=20)
        vault_label.pack()
