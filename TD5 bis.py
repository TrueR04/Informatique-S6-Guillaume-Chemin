

#1
from tkinter import Tk, Canvas, Frame, Text, Button,Label



def read_word(canvas, mot, h, w, x, y, couleur: str):
    for lettre in mot:
        if lettre != 'H'and lettre != 'U' and lettre != 'D' :
            print('le mot ne fonctionne pas')
            return
        elif lettre == 'H':
            canvas.create_line(x, y, x + h, y, fill = couleur, width=2)
            x,y = x + h,y
        elif lettre == 'U' :
            canvas.create_line(x, y, x + w, y - h, fill = couleur, width=2)
            x,y = x + w, y - h
        elif lettre == 'D' :
            canvas.create_line(x, y, x + w, y + h, fill = couleur, width=2)
            x,y = x + w, y + h
    


#2
def create_word(n, l):
    listeMot = ['H' for i in range(n)] 
    permutation = [ i for i in range(n)]
    res = [None for i in range(n)]
    for element in l :
        for i in range(n) :
            if i == element :
                listeMot[i] += 'DH'
            elif i == element + 1:
                listeMot[i] += 'UH'
            else :
                listeMot[i] += 'HH'
        listeMot[element] , listeMot[element + 1] = listeMot[element + 1] , listeMot[element]
        permutation[element] , permutation[element + 1] = permutation[element + 1] , permutation[element]
    for i in range(n) :
        res[permutation[i]] = listeMot[i]
    return res


def draw_entrelacs(l: list, canvas, h, w, x, y, fill: list) :
    for i in range(len(l)) :
        read_word(canvas, l[i], h, w, x, y, fill[i])
        y += h
    
def permutColor(l : list):
    l.append(l.pop(0))
    return l
    


if __name__ == "__main__":
    listeCouleur = ['#00AA00', '#FF0000', '#0000FF', '#000000']
    listeCroisements = [2, 1, 1, 0, 2]
    root = Tk()
    root.geometry('500x600')
    canvas = Canvas(root, width= 600, height= 300, bg= 'light grey')
    interface = Canvas(root, width = 600, height = 150, bg= 'black')
    quitter = Button(root, text = 'quitter', command = root.destroy, bg= 'dark grey', relief= 'raised')
    croisements = Label(root, text = 'Croisements', fg= 'white', bg= 'black', font= ('Arial', 15))
    liste = Label(root, text= (' '+str(listeCroisements)+' '), fg= 'white', bg= 'black', relief= 'raised', font= ('Arial', 15))
    interface.grid(row= 2, column= 1, rowspan= 2, columnspan= 2)
    quitter.grid(row= 3, column= 1)
    croisements.grid(row= 2, column= 1)
    colors = Button(root, text= 'Colors', command=lambda: draw_entrelacs(create_word(4, [2, 1, 1, 0, 2]), canvas, 40, 40, 50, 100, permutColor(listeCouleur)), fg= 'white', bg= 'dark grey', relief= 'raised')
    colors.grid(row= 3, column= 2)
    liste.grid(row= 2, column= 2)
    canvas.grid(row= 1, column= 1, columnspan= 2)
    
    
    
    draw_entrelacs(create_word(4, [2, 1, 1, 0, 2]), canvas, 40, 40, 50, 100, listeCouleur)

    root.mainloop()

