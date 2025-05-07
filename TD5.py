# # from tkinter import Tk, Canvas

# # root = Tk("hello")

# # canvas = Canvas(root, ...)

# # canvas.grid(column = 1, width = 1)

# #1
# from tkinter import Tk, Canvas, Frame, Text
# from tkinter.ttk import Button


# def read_word(canvas, mot, h, w, x, y, couleur: str):
#     for lettre in mot:
#         if lettre != 'H'and lettre != 'U' and lettre != 'D' :
#             print('le mot ne fonctionne pas')
#             return
#         elif lettre == 'H':
#             canvas.create_line(x, y, x + h, y, fill = couleur, width=2)
#             x,y = x + h,y
#         elif lettre == 'U' :
#             canvas.create_line(x, y, x + w, y - h, fill = couleur, width=2)
#             x,y = x + w, y - h
#         elif lettre == 'D' :
#             canvas.create_line(x, y, x + w, y + h, fill = couleur, width=2)
#             x,y = x + w, y + h
    


# #2
# def create_word(n, l):
#     listeMot = ['H' for i in range(n)] 
#     permutation = [ i for i in range(n)]
#     res = [None for i in range(n)]
#     for element in l :
#         for i in range(n) :
#             if i == element :
#                 listeMot[i] += 'DH'
#             elif i == element + 1:
#                 listeMot[i] += 'UH'
#             else :
#                 listeMot[i] += 'HH'
#         listeMot[element] , listeMot[element + 1] = listeMot[element + 1] , listeMot[element]
#         permutation[element] , permutation[element + 1] = permutation[element + 1] , permutation[element]
#     for i in range(n) :
#         res[permutation[i]] = listeMot[i]
#     return res

# # print(create_word(4,  [2, 1, 1, 0, 2]))

# def draw_entrelacs(l: list, canvas, h, w, x, y, fill: list) :
#     for i in range(len(l)) :
#         read_word(canvas, l[i], h, w, x, y, fill[i])
#         y += h
    
from tkinter import Tk, Frame, Text
from tkinter.ttk import Button, Label, Spinbox, Checkbutton, Radiobutton, Entry
root = Tk()
root.geometry('600x400')
window = Frame(root)
window.grid()
Button(window,text="Dis bonjour").grid(row=1,column=1)
Label(window,text="C'est moi").grid(row=2,column=1)
Spinbox(window,values=('One', 'Two', 'Three')).grid(row=3,column=1)
Checkbutton(window, text="Tu n'as rien oublié ?").grid(row=4,column=1)
Radiobutton(window, text="Option 1", value="1").grid(row=5,column=1)
Radiobutton(window, text="Option 2", value="2").grid(row=6,column=1)
Radiobutton(window, text="Option 3", value="4").grid(row=7,column=1)
Entry(window).grid(row=8,column=1)
Text(window).grid(row=1,column=2,rowspan=8)
root.mainloop()

# if __name__ == "__main__":
#     root = Tk()
#     root.geometry('600x600')
#     canvas = Canvas(root, width= 600, height= 600, bg= 'white')
#     canvas.grid()
#     window = Frame
    
#     listeCouleur = ['#00AA00', '#FF0000', '#0000FF', '#000000']
    
#     draw_entrelacs(create_word(4, [2, 1, 1, 0, 2]), canvas, 40, 40, 50, 200, listeCouleur)
    
#     #read_word(canvas,'HUHUHUHUHDDDD', 20, 20, 50, 200, "#000000")

#     root.mainloop()

