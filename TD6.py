from tkinter import Tk, Canvas, Frame, Text, Label, Button


class App:
    #on définit tous les éléments nécessaire au tracé et à l'affichage qu'on souhaite obtenir
    def __init__(self,Data):
        self.listeCouleur = ['#00AA00', '#FF0000', '#0000FF', '#000000']
        self.data = Data
        self.h = 40
        self.w = 40
        self.root = Tk()
        self.canvas = Canvas(self.root, width= 600, height= 300, bg= 'light grey')
        self.interface = Canvas(self.root, width = 600, height = 150, bg= 'black')
        self.quitter = Button(self.root, text = 'quitter', command = self.root.destroy, fg= 'white', bg= 'dark grey', relief= 'raised')
        self.croisements = Label(self.root, text= 'Croisements', fg= 'white', bg= 'black', relief= 'raised', font= ('Arial', 15))
        self.liste = Label(self.root, text= (' '+str(self.listeCouleur)+' '), fg= 'white', bg= 'black', relief= 'raised', font= ('Arial', 15))
        self.x = 50
        self.y0 = 100
        self.y = 100
        self.colors = Button(self.root, text= 'Colors', command= lambda: self.update_drawing(), fg= 'white', bg= 'dark grey', relief= 'raised')
        self.quitter.grid(row= 3, column= 1)
        self.colors.grid(row= 3, column= 2)
        self.window = Frame(self.root)
        self.canvas.grid(row= 1, column= 1, columnspan= 2)
        self.interface.grid(row= 2, column= 1, rowspan= 2, columnspan= 2)
        self.croisements.grid(row= 2, column= 1)
        self.liste.grid(row= 2, column= 2)
        self.c = 0
        self.draw = self.draw_entrelacs()
     
    #on définit les méthodes permettant d'afficher et d'utiliser les boutons comme on l'entend
    
    # on lit un mot grâce à cette fonction
    def read_word(self, mot):
        self.x = 50
        self.y = self.y0
        for lettre in mot:
            if lettre != 'H'and lettre != 'U' and lettre != 'D' :
                print('le mot ne fonctionne pas')
                return
            elif lettre == 'H':
                self.canvas.create_line(self.x, self.y, self.x + self.h, self.y, fill = self.listeCouleur[self.c], width=2)
                self.x,self.y = self.x + self.h,self.y
            elif lettre == 'U' :
                self.canvas.create_line(self.x, self.y, self.x + self.w, self.y - self.h, fill = self.listeCouleur[self.c], width=2)
                self.x,self.y = self.x + self.w, self.y - self.h
            elif lettre == 'D' :
                self.canvas.create_line(self.x, self.y, self.x + self.w, self.y + self.h, fill = self.listeCouleur[self.c], width=2)
                self.x,self.y = self.x + self.w, self.y + self.h
        
    # on dessine un ensemble d'entrelacements à partir des données
    def draw_entrelacs(self) : #cette fonction remplie le rôle de la fonction 'redraw' dont il est question dans l'énoncé
        for mot in self.data.res :
            self.read_word(mot)
            self.c += 1 
            self.y0 += self.h
            
    # on effectue une permutation circulaire sur la liste de couleur en plaçant le premier élément en dernière position
    def permutColor(self):
        self.listeCouleur.append(self.listeCouleur.pop(0))
        return self.data.croisements
    
    # on met à jour le dessin en applicant la permutation des couleurs
    def update_drawing(self):
        self.canvas.delete("all")                
        self.permutColor()                     
        self.data.create_word()              
        self.c = 0                              
        self.y0 = 100                          
        self.draw_entrelacs() 
    
    def run_forever(self):
        self.root.mainloop()
        
        

class Data:
    # on définit les données nécessaires au tracé que l'on cherche à obtenir
    def __init__(self, croisements, nbFils):
        self.croisements = croisements
        self.nbFils = nbFils
    
    # on crée une listre de mot caractérisant l'entrelacement que l'on veut tracé
    def create_word(self):
        listeMot = ['H' for i in range(self.nbFils)] 
        permutation = [ i for i in range(self.nbFils)]
        self.res = [None for i in range(self.nbFils)]
        for element in self.croisements :
            if element < 0 or element + 1 >= self.nbFils:
                print(f"Croisement invalide: {element} (nbFils = {self.nbFils})")
                continue
            for i in range(self.nbFils) :
                if i == element :
                    listeMot[i] += 'DH'
                elif i == element + 1:
                    listeMot[i] += 'UH'
                else :
                    listeMot[i] += 'HH'
            listeMot[element] , listeMot[element + 1] = listeMot[element + 1] , listeMot[element]
            permutation[element] , permutation[element + 1] = permutation[element + 1] , permutation[element]
        for i in range(self.nbFils) :
            self.res[permutation[i]] = listeMot[i]
            
            
    
     
if __name__ == "__main__":
    data = Data([2, 1, 1, 0, 2],4)
    data.create_word()
    app = App(data)
    app.run_forever()
    
 # Je n'ai pas pu avancer plus car arriver jusqu'ici m'a pris entre 5 et 6 heures, le temps de tout comprendre.
