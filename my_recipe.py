from tkinter import *
import tkinter as tk

root = Tk()
root.title('Recipe Book')
account_frame = tk.Frame(root, width=600, height=700, bg='#9dd7f5')
account_frame.pack(side='top')
label1 = tk.Label(account_frame, text="Welcome to my recipe book...", font='helvetica 20')
label1.place(relx=.21, rely=0.03
label3 = tk.Label(account_frame, text='how many layers would you like?', font='helvetica 16')
label3.place(relx=.25, rely=0.13)

entry1 = tk.Entry(account_frame, font=('calibre', 10, 'normal'))
entry1.place(relx=0.38, rely=0.23)

label2 = tk.Label(account_frame, text='what would you like to bake?', font='helvetica 16')
label2.place(relx=.29, rely=0.3)

def getVictoriaRecipe():
    name_var = entry1.get()
    name_var = int(name_var)
    s = name_var * 112
    f = name_var * 112
    b = name_var * 112
    eg = name_var * 2
    c = name_var * 200
    j = name_var * 3

    label3 = tk.Label(root, text="For Victoria Sponge you will need: ", font='helvetica 15')
    label3.place(relx=.25, rely=0.55)

    label4 = tk.Label(root, text= str(s) + "g of sugar", font='helvetica 12')
    label4.place(relx=.25, rely=0.63)

    label5 = tk.Label(root, text= str(f) + "g of flour", font='helvetica 12')
    label5.place(relx=.25, rely=0.68)

    label6 = tk.Label(root, text= str(b) + "g of butter", font='helvetica 12')
    label6.place(relx=.25, rely=0.73)

    label7 = tk.Label(root, text= str(eg) + " eggs", font='helvetica 12')
    label7.place(relx=.25, rely=0.78)

    label8 = tk.Label(root, text="1tsp of baking powder, 1tsp of vanilla extract", font='helvetica 12')
    label8.place(relx=.25, rely=0.83)

    label9 = tk.Label(root, text= str(c) + "ml of double cream", font='helvetica 12')
    label9.place(relx=.25, rely=0.88)

    label10 = tk.Label(root, text= str(j) + "tbsp of your choice of jam & some icing sugar to dust", font='helvetica 12')
    label10.place(relx=.25, rely=0.93)

def getChocolateRecipe():
    name_var = entry1.get()
    name_var = int(name_var)
    s = name_var * 65
    f = name_var * 52
    b = name_var * 70
    eg = name_var * 5
    c = name_var * 150
    j = name_var * 5

    label3 = tk.Label(root, text="For Chocolate Cake you will need: ", font='helvetica 15')
    label3.place(relx=.25, rely=0.55)

    label4 = tk.Label(root, text=str(s) + "g of sugar", font='helvetica 12')
    label4.place(relx=.25, rely=0.63)

    label5 = tk.Label(root, text=str(f) + "g of flour", font='helvetica 12')
    label5.place(relx=.25, rely=0.68)

    label6 = tk.Label(root, text=str(b) + "g of butter", font='helvetica 12')
    label6.place(relx=.25, rely=0.73)

    label7 = tk.Label(root, text=str(eg) + " eggs", font='helvetica 12')
    label7.place(relx=.25, rely=0.78)

    label8 = tk.Label(root, text="1tsp of baking powder, 1tsp of vanilla extract", font='helvetica 12')
    label8.place(relx=.25, rely=0.83)

    label9 = tk.Label(root, text=str(c) + "ml of double cream", font='helvetica 12')
    label9.place(relx=.25, rely=0.88)

    label10 = tk.Label(root, text=str(j) + "tbsp of your choice of jam & some icing sugar to dust", font='helvetica 12')
    label10.place(relx=.25, rely=0.93)


add_account_button = tk.Button(account_frame, text="Victoria Sponge", command=getVictoriaRecipe, font='Courier 15',
                               bg='brown', fg='white')
add_account_button.place(relx=0.33, rely=0.38)

add_account_button = tk.Button(account_frame, text="Chocolate Cake", command=getChocolateRecipe, font='Courier 15',
                               bg='brown', fg='white')
add_account_button.place(relx=0.34, rely=0.45)


root.mainloop()
