from tkinter import Tk, Canvas, Frame, Text, Label, Button
import numpy as np
import random as rd



class Graph_App:
    def __init__(self, graph: list,label: list, w, h, Raideur, mass):
        self.root = Tk()
        self.h = h
        self.w = w
        self.canvas = Canvas(self.root, width= self.w, height= self.h, bg= 'light grey')
        self.graph = graph
        self.label = label
        self.pos = [np.array([rd.randint(0, self.w), rd.randint(0, self.h)], dtype=(float)) for i in range(len(self.graph))]
        self.l0 = 100
        self.Raideur = Raideur
        self.mass = mass
        self.t = 1
        self.force = []
        self.E = 0.05
        self.v = [np.array([10 * (rd.random() - 0.5), 10 * (rd.random() - 0.5)]) for i in range(len(self.graph))]
        self.root.bind("<f>", self.déplacement)
        
    def déplacement(self, event=None):
        n = len(self.graph)
        self.force = [np.zeros(2) for _ in range(n)]

    # Attraction par les ressorts entre les noeuds connectés
        for i in range(n):
            for j in self.graph[i]:
                delta = self.pos[j] - self.pos[i]
                distance = np.linalg.norm(delta) + 1e-4  # Évite division par zéro
                direction = delta / distance
                f = self.Raideur * (distance - self.l0) * direction
                self.force[i] += f

    # Répulsion entre tous les noeuds
        for i in range(n):
            for j in range(n):
                if i != j:
                    delta = self.pos[i] - self.pos[j]
                    distance = np.linalg.norm(delta) + 1e-4
                    direction = delta / distance
                    f_rep = self.E / (distance ** 2) * direction
                    self.force[i] += f_rep

    # Mise à jour des vitesses et positions
        for i in range(n):
            self.v[i] = 0.9 * (self.v[i] + (self.force[i] / self.mass) * self.t)
            self.pos[i] += self.v[i] * self.t
            
        self.draw()
    
    #méthode pour tracer le graphe à partir des données 
    def draw(self):
        p = 0
        self.canvas.delete('all')
        for i in range(len(self.graph)):
            for j in self.graph[i]:  
                self.canvas.create_line(self.pos[i][0], self.pos[i][1], self.pos[j][0], self.pos[j][1])
        for (x, y) in self.pos: 
            self.canvas.create_oval(x-10,y-10,x+10,y+10,fill="#f3e1d4")
            self.canvas.create_text(x, y, text= str(self.label[p]), font= 24)
            p += 1
        self.canvas.grid()
        
    def run_forever(self):
        self.draw()
        self.root.mainloop()

        
if __name__ == "__main__":
    app = Graph_App([[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], [3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]], [i for i in range(11)], 600, 600, 10, 1000)
    app.run_forever()
