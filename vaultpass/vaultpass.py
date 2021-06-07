from tkinter import Tk
from TitleFrame import TitleFrame
from BottomFrame import BottomFrame


root = Tk()
root.geometry("700x350")

topFrame = TitleFrame(root)
topFrame.pack()

bottomFrame = BottomFrame(root)
bottomFrame.pack()

# part_text = StringVar()
# part_label = Label(app, text="Working Dir", font=("bold", 14), pady=20)
# part_label.grid(row=0, column=0, sticky=W)
# part_entry = Entry(app, textvariable=part_text)
# part_entry.grid(row=0, column=1)

root.title("Vault Pass")

root.mainloop()
