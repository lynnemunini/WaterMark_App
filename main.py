from tkinter import *
from tkinter.font import Font
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
menubar = Menu(root, background="#464646", borderwidth=0, fg="white", activebackground='#464646', activeforeground='#e5dedc')
root.config(menu=menubar)

# Add image file
bg_image = ImageTk.PhotoImage(file = "background.png")
# create the file_menu
file_menu = Menu(
    menubar,
    tearoff=0,
    background="#646463",
    activebackground='#e46c4e',
    fg="white",
    activeforeground='white'
)

# add menu items to the File menu
file_menu.add_command(label='Open',
                command=lambda: open()
                )
file_menu.add_command(label='Save',
                command=lambda: save()
                )
file_menu.add_command(label='Close',
                command=lambda: close()
)
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
    tearoff=0,
    background="#646463",
    fg="white",
    activebackground='#e46c4e',
    activeforeground='white'
)

# add menu items to the File menu
edit_menu.add_command(label='Change Image',
                command=lambda: change_image()
)
edit_menu.add_command(label='Add WaterMark')


# add the File menu to the menubar
menubar.add_cascade(
    label="Edit",
    menu=edit_menu
)

# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0,
    background="#646463",
    fg="white",
    activebackground='#e46c4e',
    activeforeground='white'
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
        edit_menu.entryconfig("Change Image", state="normal")#Enable Menu Option
        edit_menu.entryconfig("Add WaterMark", state="normal")#Enable Menu Option
        file_menu.entryconfig("Save", state="normal")#Enable Menu Option
        file_menu.entryconfig("Close", state="normal")#Enable Menu Option  
         
        filetypes = (
                ('png files', '*.png'),
                ('all files', '*.*')
        )
        root.filename = fd.askopenfilename(
                title='Open a file',
                initialdir='~',
                filetypes=filetypes)
        # print(root.filename)
        if root.filename is not None and root.filename != "" and root.filename != ():
            main_window.destroy()
            get_started.destroy()

            # Picture name 
            global pic_name, my_image, image_canvas
            pic_name = root.filename.split('/')[-1]
            my_image = Image.open(root.filename)
            if my_image.width > scr_width or my_image.height > scr_height:
                    # only resize image bigger than the screen
                    ratio = min(scr_width/my_image.width, scr_height/my_image.height)
                    my_image = my_image.resize((int(my_image.width*ratio), int(my_image.height*ratio)), Image.ANTIALIAS)
            my_image = ImageTk.PhotoImage(my_image)  

            #Image Canvas
            image_canvas = Canvas(width=800, height=800, bg="white", highlightthickness=0)
            image_canvas.create_image(400, 400, image=my_image)
            image_canvas.pack()


def open():
    # Remove from screen:
    for label in root.grid_slaves():
        # Remove all widgets with row numbers < 4
        if int(label.grid_info()["row"]) < 4:
            label.grid_forget()
    get_image()   

def change_image():
    try:
        image_display = image_canvas
    except:
        pass
    else:
        get_image()
        image_display.destroy()


# open and ask to save file
def save():
        imgpil = ImageTk.getimage(my_image)
        imgpil.save( os.path.join("/home/lynne/Pictures", pic_name), "png" )
        imgpil.close()  

def window():
    global main_window, get_started
    edit_menu.entryconfig("Change Image", state="disabled")#Disable Menu Option
    edit_menu.entryconfig("Add WaterMark", state="disabled")#Enable Menu Option
    file_menu.entryconfig("Save", state="disabled")#Disable Menu Option
    file_menu.entryconfig("Close", state="disabled")#Disable Menu Option
    
    main_window = Label(
        root,
        image=bg_image
    )
    main_window.place(x=0, y=0)

    # Get started button
    get_started = Button(root, height=2, width=10, text="Get Started", fg="black", background='#e46c4e', activebackground='#464646', font=("Poppins"), command=open)
    get_started.place(x = 50, y = 450)

def close():
    try:
        if pic_name is not None:
            image_canvas.destroy()
    except:
        pass
    else:
        window()

if __name__ == "__main__":
    window()
    # run the application
    root.mainloop()

