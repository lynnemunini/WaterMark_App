from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image

# create the root window
root = Tk()
root.title('Upload Image')
root.resizable(True, True)

filetypes = (
        ('png files', '*.png'),
        ('all files', '*.*')
    )
root.filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/home/lynne/Pictures',
        filetypes=filetypes)

# my_label = Label(root, text=root.filename).pack()
my_image = ImageTk.PhotoImage(Image.open(root.filename))
my_image_label = Label(image=my_image).pack()

# run the application
root.mainloop()