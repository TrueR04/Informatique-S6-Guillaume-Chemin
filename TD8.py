
import struct as st


f = open('the_wall.wav', 'rb')           # sauter l'en-tête
data = f.read()  

nb_bytes = st.unpack('I', data[40: 44])[0]
nb_channels = st.unpack('H', data[22: 24])[0]
nb_bytes_per_sample = st.unpack('H', data[35: 37])[0]
nb_samples_per_channel = nb_bytes / (nb_channels * nb_bytes_per_sample)
nb_samples = nb_bytes / (nb_bytes_per_sample)
freq = 44100 
delta = int(freq / 5)

def récupData(data):
    listeEchantillons = []
    for i in range(int(nb_bytes//4)):
        listeEchantillons.append((st.unpack_from("hh", data, 44 + 4 * i)))
    return listeEchantillons

def create_file(filename: str, liste):
    size = 36 + len(liste) * 2 *2
    with open (filename, "wb") as f:
        f.write(b'RIFF')
        f.write(st.pack('I', size))
        f.write(b'WAVE')
        f.write(b'fmt ')
        f.write(st.pack("I",16))
        f.write(st.pack("H",1))
        f.write(st.pack("H",2))
        f.write(st.pack("I", freq))
        f.write(st.pack("I",176400))
        f.write(st.pack("H",4))
        f.write(st.pack("H",16))
        f.write(b'data')
        f.write(st.pack('I', size - 36))
        
        for i in range(len(liste)):
            f.write(st.pack("hh", *liste[i]))
            
            
def create_file_cut_half(filename: str, liste):
    size = 36 + len(liste) * 2 *2
    with open (filename, "wb") as f:
        f.write(b'RIFF')
        f.write(st.pack('I', size))
        f.write(b'WAVE')
        f.write(b'fmt ')
        f.write(st.pack("I",16))
        f.write(st.pack("H",1))
        f.write(st.pack("H",2))
        f.write(st.pack("I",freq))
        f.write(st.pack("I",176400))
        f.write(st.pack("H",4))
        f.write(st.pack("H",16))
        f.write(b'data')
        f.write(st.pack('I', size - 36))
        
        for i in range(len(liste)):
            f.write(st.pack("hh", *liste[i]))
            
def create_file_allonge(filename: str, liste, coeff):
    size = 36 + len(liste) * 2 * 2 * 2
    with open (filename, "wb") as f:
        f.write(b'RIFF')
        f.write(st.pack('I', size))
        f.write(b'WAVE')
        f.write(b'fmt ')
        f.write(st.pack("I",16))
        f.write(st.pack("H",1))
        f.write(st.pack("H",2))
        f.write(st.pack("I",freq * coeff))
        f.write(st.pack("I",176400))
        f.write(st.pack("H",4))
        f.write(st.pack("H",16))
        f.write(b'data')
        f.write(st.pack('I', size - 36))
        
        for i in range(len(liste) - 1):
            f.write(st.pack("hh", *liste[i]))
            f.write(st.pack("hh", (int((liste[i][0] + liste[i + 1][0]) * 0.5)), int((liste[i][1] + liste[i + 1][1]) * 0.5)))
        f.write(st.pack("hh", *liste[-1]))
            
def create_file_accélère(filename: str, liste, coeff):
    size = 36 + len(liste) * 2
    with open (filename, "wb") as f:
        f.write(b'RIFF')
        f.write(st.pack('I', size))
        f.write(b'WAVE')
        f.write(b'fmt ')
        f.write(st.pack("I",16))
        f.write(st.pack("H",1))
        f.write(st.pack("H",2))
        f.write(st.pack("I",freq * coeff))
        f.write(st.pack("I",176400))
        f.write(st.pack("H",4))
        f.write(st.pack("H",16))
        f.write(b'data')
        f.write(st.pack('I', size - 36))
        
        for i in range(len(liste)//2):
            f.write(st.pack("hh", *liste[2 * i]))

def create_file_echo(filename: str, liste, coeff):
    size = 36 + len(liste) * 2 * 2 
    with open (filename, "wb") as f:
        f.write(b'RIFF')
        f.write(st.pack('I', size))
        f.write(b'WAVE')
        f.write(b'fmt ')
        f.write(st.pack("I",16))
        f.write(st.pack("H",1))
        f.write(st.pack("H",2))
        f.write(st.pack("I",44100 * coeff))
        f.write(st.pack("I",176400))
        f.write(st.pack("H",4))
        f.write(st.pack("H",16))
        f.write(b'data')
        f.write(st.pack('I', size - 36))
        
        for j in range(delta):
            f.write(st.pack("hh", *liste[j]))
            
        for i in range(delta, len(liste)):
            f.write(st.pack("h", int(liste[i][0] + liste[i - delta][0] * 0.7)))
            f.write(st.pack("h", int(liste[i][1] + liste[i - delta][1] * 0.7)))
            

create_file_echo('musique_copiée_echo.wav', récupData(data), 1)

# for i in range(nb_bytes//4):
#     st.pack(listeEchantillons[i])
# with open("music_copiée", "wb") as f:
#     f.write(texte)

# chunksize = 36 + len(liste) * 2 *2