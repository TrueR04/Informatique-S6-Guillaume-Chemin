f=open("C:\\Users\\guill\\OneDrive\\Documents\\1A Mines Nancy\\info S5\\frenchssaccent.dic")

# tirage
# mot
# si la lettre est dans la liste

# fonction qui prend tte la liste des mots
# faire un efonction qui prend en parametre un tirage de lettre et un mot. renvoie true d*si on peux ecrire un mot avec le tirage et false sinon.
# fonction qui donne le mot le plus long parmi ceux qui fonctionnent

l=['a','c','t','e','c']
p=[]

for ligne in f:
    p.append(ligne[0:len(ligne)-1])
f.close()


#1&2
def verifMot(tirage,mot):
    i=0
    while i<len(mot):
        if mot[i] in tirage:
            tirage.remove(mot[i])
        else:
            return False
        i+=1
    return True
        
def motsAutorisés(lexique,tirage):
    m=[]
    for mot in lexique:
        if verifMot(tirage,mot):
            m.append(mot)
    return(m)

def motLePlusLong(liste):
    maxind=0
    maxlen=0
    for i in range(len(liste)-1):
        if len(liste[i])>maxlen:
            maxlen=len(liste[i])
            maxind=i 
        i+=1
    return(liste[maxind])

listedemot=['caca' , 'pipi,' , 'anticonstitutionnellement','popo','mamouth','pet']

#3
points = {'a': 1,'e': 1,'i': 1,'l': 1,'n': 1,'o': 1,'r': 1,'s': 1,'t': 1,
           'u': 1,'d': 2, 'g': 2, 'm': 2, 'b': 3, 'c': 3, 'p': 3, 'f': 4,
           'h': 4, 'v': 4, 'j': 8, 'q': 8, 'k': 10, 'w': 10, 'x': 10,
           'y': 10, 'z': 10}

#on change la fonction motLePlusLong() pour lui permettre de compter le score de chaque mot de la liste et de retenir le meilleur
def motLePlusScorant(liste):
    maxind=0
    scoremot=0
    maxscore=0
    for i in range(len(liste)-1):
        for lettre in liste[i]:
            scoremot += points[lettre]
        if scoremot > maxscore:
            maxscore = scoremot
            maxind = i
        i+=1
    return(liste[maxind])


#4
#on rajoute le joker au dictionnaire qui associe chaque lettre au nb de point qu'elle rapporte
points = {'a': 1,'e': 1,'i': 1,'l': 1,'n': 1,'o': 1,'r': 1,'s': 1,'t': 1,
           'u': 1,'d': 2, 'g': 2, 'm': 2, 'b': 3, 'c': 3, 'p': 3, 'f': 4,
           'h': 4, 'v': 4, 'j': 8, 'q': 8, 'k': 10, 'w': 10, 'x': 10,
           'y': 10, 'z': 10, '?':0}
#on rajoute le cas où il y a un joker dans le tirage. on modifie les conditions d'autorisation de construction du mot à partir d'un tel tirage
def verifMotJoker(tirage,mot):
    i=0
    while i<len(mot):
        if mot[i] in tirage:
            tirage.remove(mot[i])
        elif '?' in tirage:
            tirage.remove('?')
            mot[i] = '?'
        else :
            return False
        i+=1
    return True