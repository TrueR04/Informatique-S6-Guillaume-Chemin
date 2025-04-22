
#1

class polynomial:
    def __init__ (self,l):
        self.coefs = l
    

    def __str__(self):
        p=[]
        for i in range(len(self.coefs)):
            p.append(str(self.coefs[i])+'X^'+str(len(self.coefs)-1-i))
            i=i+1
        return(str(p))
        
    def __add__(self,pol):
        c1=self.cpefs
        c2=pol.coefs
        p=[]
        if len(c1)>len(c2):
            for i in range(len(len(c1)-len(c2))):
                c2.insert(0,0)
                i+=1
        elif len(c2)>len(c1):
            for i in range(len(len(c2)-len(c1))):
                c1.insert(0,0)
                i+=1
        for i in range(len(c1)):
           p.append(c1[i]+c2[i])
           i+=1
        return(p)
   
        
   
    
   
q=polynomial([1,2,3])
print(str(q))

#p += "X"+str(self.coefs[i])
 for i in range(len(c1)):
    p.append(c1[i]+c2[i])
    

#2

class Zq:
    def __init__(self,l):
        self.coefs=l