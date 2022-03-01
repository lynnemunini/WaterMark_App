from re import I
from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image

# create the root window
root = Tk()
root.title('Upload Image')
root.resizable(True, True)
root.geometry("1000x800")
root.configure(bg='white') 


def get_image():
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
        w = my_image.width
        my_image = my_image.resize((int(w/2), int(h/2)), Image.ANTIALIAS)
        my_image = ImageTk.PhotoImage(my_image)


        #Image Canvas
        image_canvas = Canvas(width=1000, height=600, bg="white", highlightthickness=0)
        image_canvas.create_image(500, 350, image=my_image)
        image_canvas.place(x=0, y=50)

        change_btn = Button(text='Change Image', command=lambda: change_image(image_canvas))
        save_btn = Button(text='Save Image')
        change_btn.place(x=300, y=700) 
        save_btn.place(x=600, y=700)

        

def open():
        btn.destroy()
        get_image()   

def change_image(image_canvas):
        image_canvas.destroy()
        get_image()

        
btn = Button(root, text="Select File", command=lambda: open())
btn.place(x=450, y=400)


# run the application
root.mainloop()

