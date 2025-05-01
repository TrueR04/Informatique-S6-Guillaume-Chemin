from __future__ import annotations
import unittest
import matplotlib.pyplot as plt

#1

#2

def hashNaive(s: str) -> int:
    return sum([ord(c) for c in s])

def hashHorner(s: str) -> int:
    h = 0
    for c in s:
        h = 33*h + ord(c)

class Hashtable:
    def __init__(self, h, length):
        self.__h = h
        self.__length = length
        self.values = [None for i in range(length)]
        
    def values(self):
        return self.values
    
    def put(self, key, value):
        index = self.__h(key) % self.__length # un problème survient ici lorsque j'utilise la fonction hashHorner au lieu de hashNaive mais je ne sais pas le résoudre.
        if self.values[index] == None:
            self.values[index] = [(key, value)]
        else:
            vérifClé = False 
            for i in range(len(self.values[index])):            
                if key == self.values[index][i][0]:
                    vérifClé = True
                    self.values[index][i][1] == value
            if not vérifClé :
                self.values[index].append((key, value))
        
                    
#3
    def get(self, key):
        index = self.__h(key) % self.__length
        for i in range(len(self.values[index])):
            if key == self.values[index][i][0]:
                return self.values[index][i][1]
        raise Exception('haaaaaaaa')
    
#4
    def repartition(self) :
        p = []
        for i in range(self.__length) :
            p.append(len(self.values[i]))
        N = len(p)
        x = range(N)
        width = 1/1.5
        plt.bar(x, p, width, color="blue")
        plt.show()
        
#6       
    # def resize(self) :
        

#5

f=open("C:\\Users\\guill\\OneDrive\\Documents\\1A Mines Nancy\\info S6\\frenchssaccent.dic")

j = Hashtable(hashNaive, 320)
p = []
for ligne in f:
    p.append(ligne[0:len(ligne)-1])
f.close()

for mot in p :
    j.put(mot, len(mot))
        
j.repartition()

class testHashtable(unittest.TestCase):
    
    def test(self):
        l = Hashtable(hashNaive, 5)
        l.put('abc', 3)
        self.assertEqual(hashNaive('abc'), 294)
        self.assertEqual(l.get('abc'), 3)
        


if __name__ == '__main__' : 
    unittest.main()
