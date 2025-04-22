
#1

#2
from __future__ import annotations
import unittest


class Tree:
    def __init__(self, label, *children):
        self.__label = label
        self.__children = children
    
    def label(self):
        return (self.__label)
    
    def children(self): 
        return (self.__children)
    
    def nb_children(self):
        return(len(self.__children))
        
    def is_leaf(self):
        if len(self.children)==0:
            return(True)
        return(False)
    
    def child(self, i):
        return(Tree(self.__children[i]))
#3   
    def depth(self):
        if self.is_leaf:
            return(0)
        else:
            return 1 + max(self.depth() for i in range(len(self.nb_children())))

#4
    def __str__(self):
        if self.is_leaf():
            return self.label()
        else:
            return self.label() + ( + self.children() )
    
    def __eq__(self, arbre: Tree) -> bool:
        return self.__label() == arbre.__label() and self.__children() == arbre.__children()
         
#5
    def deriv(self, var: str) -> Tree:
        if self.is_leaf():
            if self == Tree(var):
                return Tree('1')
            else:
                return Tree('0')
        else:
            if self.__label() == '+':
                return Tree('+', self.child(0).deriv(var), self.child(1).deriv(var))
            else: 
                return Tree('*', self.child(0) * self.child(1).deriv(var), self.child(1) * self.child(0).deriv(var))


class testTree(unittest.TestCase):
    
    def test(self):
        t=Tree('d')
        T=Tree('a',t)
        TO=Tree('s',T)
        T1=Tree('+', Tree('7'), Tree('+', Tree('*', Tree('5'), Tree('X')), Tree('*', Tree('3'), Tree('*', Tree('X'), Tree('X')))))
        self.assertEqual(t.label(),'d')
        self.assertEqual(T.nb_children(),1)
        self.assertEqual(T.child(0),'d')
        self.assertEqual(t.is_leaf(),True)
        self.assertEqual(T.depth(),1)
        self.assertEqual(str(TO),'s(a(d))')
        self.assertEqual(t,Tree('d'))
        self.assertEqual(T1.deriv() == Tree('+', Tree('5'), Tree('*', Tree('6'), Tree('X'))))

if __name__ == '__main__' : 
    unittest.main()