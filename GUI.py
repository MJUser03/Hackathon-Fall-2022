import functions
import tkinter
from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.geometry("1000x800")
window.title("Systems of equations girlie")
window.config(bg = '#F8C8DC' )

entry = Entry(window,width = 50)
entry.config(font = ('Comic Sans',20,'bold'))
entry.config(bg='#FEEEEC')
entry.config(fg='#41001f')
entry.pack() #move to be a little higher
entry.place(x=400,y=735)

frame = Canvas(window, width = 0, height=80, highlightthickness= 0)
frame.config(bg = '#F8C8DC')
frame.pack()

sprite = Image.open('spriteseven.png')
img_new = sprite.resize((560,630))
img = ImageTk.PhotoImage(img_new)

label = Label(image=img)
label.config(bg = '#F8C8DC')
sprite.image = img
im = frame.create_image(260,125,anchor=NW,image=img)
label.place(x=2,y=0)
label.pack()

T_Box = Text(window,bg='#F8C8DC',fg='#41001f',height = 3, width = 65, borderwidth=0)

instructions = "    Please type in your equations into the box below.\nAn example looks like: 3x+2y-32z=-2,7x-2y+5z=-14,2x+4y+z=6"
T_Box.pack()

T_Box.insert(tkinter.END,instructions)
T_Box.config(font = ("Courier", 20))
T_Box.place(x=365,y=50)



#lets test out changing sprite and text based on user input

#if output == "smelly!"
#change image to crying

def cancel_check(map):
    if functions.cancel_out(map) != []:
        return 1
    else:
        return 0

def switch():
    Input = entry.get()
    Input = functions.remove_extra_commas(functions.remove_spaces(Input))
    if Input == "":
        Input == " "
    if functions.error_input(Input) == 1:
        T_Box = Text(window,bg='#F8C8DC',fg='#41001f',height = 3, width = 65, borderwidth=0)

        instructions = "\tLooks like you typed in an incorrect input..\n\t\tPlease type in valid equations"
        T_Box.pack()

        T_Box.insert(tkinter.END, instructions)
        T_Box.config(font=("Courier", 20))
        T_Box.place(x=310, y=50)
        return 0
    to_map = functions.eq_to_map(functions.input_to_lst(Input),Input)
    if functions.error_map(to_map) == 1:
        T_Box = Text(window,bg='#F8C8DC',fg='#41001f',height = 3, width = 65, borderwidth=0)

        instructions = "            \tSomethings off with the equation...\n   \t\tDouble check your variables! \n       \tor there isn't a clear solution to this..."
        T_Box.pack()

        T_Box.insert(tkinter.END, instructions)
        T_Box.config(font=("Courier", 20))
        T_Box.place(x=310, y=50)
        functions.lst_of_best_equation = []
        functions.lst_of_variables = []
        return 0

    if cancel_check(to_map) != 0:
        T_Box = Text(window,bg='#F8C8DC',fg='#41001f',height = 3, width = 65, borderwidth=0)

        var1 = str(functions.cancel_out(to_map)[0])
        var2 = str(functions.cancel_out(to_map)[1])

        instructions = "        \tEquations "+ str(functions.lst_of_best_equation[0]) + " and " + str(functions.lst_of_best_equation[1]) + "\n      \tworks best because " + var1+ " cancels out " +  var2
        T_Box.pack()

        T_Box.insert(tkinter.END, instructions)
        T_Box.config(font=("Courier", 20))
        T_Box.place(x=330, y=50)
        functions.lst_of_best_equation = []
        functions.lst_of_variables = []
        return 0
    elif len(functions.Common_factor(to_map))!=0:
        T_Box = Text(window,bg='#F8C8DC',fg='#41001f',height = 3, width = 65, borderwidth=0)

        var1 = str(functions.Common_factor(to_map)[0])
        var2 = str(functions.Common_factor(to_map)[1])

        instructions = "        \tEquations " + str(functions.lst_of_best_equation[0]) + " and " + str(functions.lst_of_best_equation[
            1]) + "\n      \tworks best because " + var2 + " multiplies into " + var1
        T_Box.pack()

        T_Box.insert(tkinter.END, instructions)
        T_Box.config(font=("Courier", 20))
        T_Box.place(x=310, y=50)
        functions.lst_of_best_equation = []
        functions.lst_of_variables = []
        return 0
    else:
        T_Box = Text(window,bg='#F8C8DC',fg='#41001f',height = 3, width = 65, borderwidth=0)
        instructions = "  \tseems like there isn't a best equation..."
        T_Box.pack()

        T_Box.insert(tkinter.END, instructions)
        T_Box.config(font=("Courier", 20))
        T_Box.place(x=365, y=50)
        functions.lst_of_best_equation = []
        functions.lst_of_variables = []
        return 0


enter_eq = Button(window, text="Enter", command=switch )
enter_eq.pack()
enter_eq.place(y=740,x=1170)
enter_eq.config(background='#FD7094')
window.mainloop()

