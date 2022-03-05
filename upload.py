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

# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create the file_menu
file_menu = Menu(
    menubar,
    tearoff=0
)

# add menu items to the File menu
file_menu.add_command(label='Open',
                command=lambda: open()
                )
file_menu.add_command(label='Save',
                command=lambda: save()
                )
file_menu.add_command(label='Close')
file_menu.add_separator()

# add Exit menu item
file_menu.add_command(
    label='Exit',
    command=root.destroy
)

# add the File menu to the menubar
menubar.add_cascade(
    label="File",
    menu=file_menu
)

# create the edit_menu
edit_menu = Menu(
    menubar,
    tearoff=0
)

# add menu items to the File menu
edit_menu.add_command(label='Change Image',
                command=lambda: change_image()
)

# add the File menu to the menubar
menubar.add_cascade(
    label="Edit",
    menu=edit_menu
)

# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label='Welcome')
help_menu.add_command(label='About')

# add the Help menu to the menubar
menubar.add_cascade(
    label="Help",
    menu=help_menu
)

# Functions
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
        global pic_name
        pic_name = root.filename.split('/')[-1]
        global my_image
        my_image = Image.open(root.filename)
        if my_image.width > scr_width or my_image.height > scr_height:
                # only resize image bigger than the screen
                ratio = min(scr_width/my_image.width, scr_height/my_image.height)
                my_image = my_image.resize((int(my_image.width*ratio), int(my_image.height*ratio)), Image.ANTIALIAS)
        my_image = ImageTk.PhotoImage(my_image)  


        #Image Canvas
        image_canvas = Canvas(width=800, height=800, bg="white", highlightthickness=0)
        image_canvas.create_image(400, 400, image=my_image)
        image_canvas.grid(row = 0, column = 0, columnspan=2)


def open():
        get_image()   

def change_image(image_canvas):
        image_canvas.destroy()
        get_image()


# open and ask to save file
def save():
        imgpil = ImageTk.getimage(my_image)
        imgpil.save( os.path.join("/home/lynne/Pictures", pic_name), "png" )
        imgpil.close()  

intro_frame = Frame(root)
# Main window text
intro = Label(intro_frame, text="Brand your Image")
intro.pack(pady=20)   

# Get started button
get_started = Button(intro_frame, text="Get Started", command=open)
get_started.pack()

#Main Window Image       
main_image = Image.open("crayon-image-settings.png")
main_image = main_image.resize((500, 500))
main_image = ImageTk.PhotoImage(main_image) 
image_canvas = Canvas(width=600, height=600, bg="white", highlightthickness=0)
image_canvas.create_image(220, 400, image=main_image)
image_canvas.grid(row = 0, column = 1, rowspan = 2)

intro_frame.grid(row =1, column = 0, padx=100)


# run the application
root.mainloop()

