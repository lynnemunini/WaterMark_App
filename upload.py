from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image
import os

# create the root window
root = Tk()
root.title('Upload Image')
root.resizable(False, False)
root.geometry("800x800")
root.configure(bg='white') 

# get the screen size
scr_width = root.winfo_screenwidth()
scr_height = root.winfo_screenheight()


def get_image():      
        filetypes = (
                ('png files', '*.png'),
                ('all files', '*.*')
        )
        root.filename = fd.askopenfilename(
                title='Open a file',
                initialdir='/home/lynne/Pictures',
                filetypes=filetypes)

        # Picture name 
        pic_name = root.filename.split('/')[-1]
        my_image = Image.open(root.filename)
        if my_image.width > scr_width or my_image.height > scr_height:
                # only resize image bigger than the screen
                ratio = min(scr_width/my_image.width, scr_height/my_image.height)
                my_image = my_image.resize((int(my_image.width*ratio), int(my_image.height*ratio)))
        # h = my_image.height
        # w = my_image.width
        # my_image = my_image.resize((int(w/2), int(h/2)), Image.ANTIALIAS)
        my_image = ImageTk.PhotoImage(my_image)  


        #Image Canvas
        image_canvas = Canvas(width=800, height=600, bg="white", highlightthickness=0)
        image_canvas.create_image(400, 300, image=my_image)
        image_canvas.place(x=0, y=0)

        change_btn = Button(text='Change Image', command=lambda: change_image(image_canvas))
        save_btn = Button(text='Save', command=lambda: save(my_image, pic_name))
        change_btn.place(x=300, y=700) 
        save_btn.place(x=600, y=700)        

def open():
        btn.destroy()
        get_image()   

def change_image(image_canvas):
        image_canvas.destroy()
        get_image()


# open and ask to save file
def save(image, name):
        imgpil = ImageTk.getimage( image )
        imgpil.save( os.path.join("/home/lynne/Pictures", name), "png" )
        imgpil.close()        

        
btn = Button(root, text="Select File", command=lambda: open())
btn.place(x=400, y=400)


# run the application
root.mainloop()

