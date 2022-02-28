from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image

# create the root window
root = Tk()
root.title('Upload Image')
root.resizable(True, True)



def open():
        global my_image
        
        filetypes = (
                ('png files', '*.png'),
                ('all files', '*.*')
        )
        root.filename = fd.askopenfilename(
                title='Open a file',
                initialdir='/home/lynne/Pictures',
                filetypes=filetypes)

        my_image = Image.open(root.filename)
        h = my_image.height
        print(h)
        w = my_image.width
        print(w)
        my_image = my_image.resize((int(w/2), int(h/2)), Image.ANTIALIAS)
        my_image = ImageTk.PhotoImage(my_image)
        my_image_label = Label(image=my_image).pack()        

btn = Button(root, text="Select File", command=open).pack()


# run the application
root.mainloop()