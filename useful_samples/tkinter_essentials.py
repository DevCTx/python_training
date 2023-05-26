import tkinter as tk

# Creation of a simple windows
win = tk.Tk()
# Title of the windows
win.title("Windows Title")
# Size of the windows
win.geometry("380x320")
# Icon of the windows
win.iconbitmap("./python.ico")
# Background of the windows
win.config(background="#888888")
# Possible resizing of the windows
win.resizable(width=True, height=False)

# # Create a Button
# quit_button = tk.Button(
#     win,
#     text="Quitter",
#     command=win.destroy,
#     font=("Calibri", 12),
#     fg="#000055",
#     bg="#CCCCCC",
#     relief=tk.GROOVE,
# )
# quit_button.pack(expand=tk.YES)
#
# # Create a Canva
# width = 300
# height = 200
# image_canva = tk.Canvas(
#     win,
#     width=width,
#     height=height,
#     bg="white",
# )
# image_canva.pack()
# # Insert an Image into Canva (Can not be on win)
# image = tk.PhotoImage(file="./CanadaFlag.png")
# image_canva.create_image(width//2,height//2,image=image)

# Create a Label
title_label = tk.Label(
    win,
    text="Studies of firstnames",
    height=1,
    relief=tk.SOLID,
    font=("Calibri",18),
    fg="white",
    bg="#550000",
    padx='20'
)
# title_label.pack()        # Stack the Label

# Add a Canva
width = 250
height = 100
canva_vide = tk.Canvas(
    win,
    width=width,
    height=height,
    bg="white"
)
# canva_vide.pack(
#     side=tk.TOP,
#     padx='5',
#     pady='5'
# )     # Stack the canva

# Create a Button
quit_button = tk.Button( win, text="BACK", command=win.destroy)
#quit_button.pack(side=tk.LEFT,padx='10',pady='10')  # Stack the button
search_button = tk.Button( win, text="Search", command=win.bell)
#search_button.pack(side=tk.RIGHT,padx='10',pady='10')   # Stack the button

help_button = tk.Button( win, text="Help", command=win.bell)
reset_button = tk.Button( win, text="Reset", command=win.bell)
save_button = tk.Button( win, text="Save", command=win.bell)

# Display the elements into a grid
title_label.grid( row=0, columnspan=2, padx='10', pady='10')
# canva_vide.grid( row=1, columnspan=2, padx='10')
# quit_button.grid( row=2, column=0, ipadx='10')
# help_button.grid( row=2, column=1, pady='10', ipadx='10', ipady='10')
# reset_button.grid( row=3, column=0)
# save_button.grid( row=3, column=1)


# Title Firstname
firstname_label = tk.Label(
    win,
    text="Firstname to search:",
    justify="right",
    width="20",
    fg="black",
    bg="#888888",
)
firstname_label.grid(row=1, column=0, pady="20")

# Definition of a string variable
firstname_choice = tk.StringVar()
firstname_choice.set("Write here a firstname")

# Definition of an Entry
firstname = tk.Entry(
    win,
    textvariable=firstname_choice,
    justify="left",
    width="30",
    fg="#00FFFF",
    bg="#000000",
)
firstname.grid(row=1, column=1)

# Add a Frame
color_frame = tk.LabelFrame(
    win,
    width=200,
    height=50,
    text="Color",
    font=("Colibri",11,'italic'),
    bg="#888888",
    labelanchor='nw',
)
color_frame.grid(row=2, column=1, padx='10')

# Add radio button into Frame "Color"
values = ["red", "green", "blue", "orange"]
texts = ["red", "green", "blue", "orange"]
color_choice = tk.StringVar()
color_choice.set(values[1])
for i in range(len(values)):
    radio_buttons = tk.Radiobutton(
        color_frame,
        variable=color_choice,
        text=texts[i],
        value=values[i],
        bg='#888888',
    )
    radio_buttons.pack(side=tk.LEFT, expand=True)

search_button.grid( row=3, columnspan=2, ipadx='10', pady="30")

# Event Manager
win.mainloop()