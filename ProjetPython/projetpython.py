#fonction numero valide
def Numerovalid(Numero):
    if  len(Numero)== 7 and Numero.isupper() and Numero.isalnum() and not Numero.isalpha() and not Numero.isdigit():
         return True
    else:
        return False
num="GGG0088"
print(Numerovalid(num))

#fonction nom valide
def Nomvalid(Nom):
    if len(Nom)>= 2 and Nom[0].isalpha():
        return True
    else:
        return False
nom="2t"
print(Nomvalid(nom))

#fonction prenom valide
def Prenomvalid(Prénom):
    if len(Prénom)>=3 and Prénom[0].isalpha():
        return True
    else:
        return False
prenom= "yf2"
print(Prenomvalid(prenom))

#fonction date valide
from datetime import date
import re

def DateValide (j,m,a):
    try:
        z=date(a,m,j)
        return True
    except ValueError:
        return False

def formatdate(Date):
    try:
        m = ( re.split("[ -./:;_$@]",Date))
        if len(m)==3 and m[1].isalpha():
            if m[1] in "janvier":
                m1 = 1
            elif m[1] in ["fevrier","février","fev","fév"]:
                    m1 = 2
            elif m[1] in "mars":
                    m1 = 3
            elif m[1] in "avril":
                    m1 = 4
            elif m[1] in "mai":
                    m1 = 5
            elif m[1] in "juin":
                    m1 = 6
            elif m[1] in "juillet":
                    m1 = 7
            elif m[1] in ["Aout", "Aoùt","aout","aoùt"]:
                    m1 = 8
            elif m[1] in "septembre":
                    m1 = 9
            elif m[1] in "octobre":
                    m1 = 10
            elif m[1] in "Novembre":
                    m1 = 11
            elif m[1] in ["decembre","décembre"]:
                    m1 = 12
              
            else:
                return False
            m0=int(m[0])
            m2=int(m[2])
            dateval = DateValide(m0,m1,m2)
        else:
            m0=int(m[0]) 
            m1=int(m[1])
            m2=int(m[2])
            dateval = DateValide(m0,m1,m2)
        return dateval
    except ValueError:
        return False

#fonction classe valide
def Classe(c):
    c = c.strip()
    if c.isspace() == False and len(c) > 1:
        if (c[0] in ['6','5','4','3']) and (c[-1] in ['A','B']):
            return True
        else:
            return False
cl='6emA ' 
R=Classe(cl)
print(R)  

#fonction note valide
def verifnote(note):
    if len(note)<1:
        return 0
    if note is None:
        return 0    
    dico = dict()
    if note[0]=='#':
        note= note[1:]
        note =note.split("#")
    compt = 0
    moyenne_gen = []
    for matiere in note:
      sous_dico = dict()
      matiere = matiere.replace(']','')
      matiere = matiere.split('[')
      if len(matiere)==2:
         nom_matiere = matiere[0]
         dev_comp = matiere[1]
         
      if dev_comp !=None:
            dev_comp = dev_comp.split(':')
        
      
      try:
          compo = float(dev_comp[1].replace(',', '.'))
      except Exception:
         return False
      
      devoir = dev_comp[0]
      devoir = devoir.split(';')
      devoir = [i.replace(',','.') for i in devoir]
      try:
         devoir = list(map(float , devoir))
      except Exception:
         return False 
      
      for dev in devoir:
         if dev < 0 or dev > 20:
            return False
      if compo < 0 or compo > 20:
         return False 
      moyenne = round( (((sum(devoir) / len(devoir) ) + 2 * compo ) / 3),2 )
      moyenne_gen.append(moyenne)
      sous_dico.setdefault('devoir', devoir)
      sous_dico.setdefault('compo', compo)
      sous_dico.setdefault('moyenne',moyenne)
      dico.setdefault(nom_matiere, sous_dico) 
    moyenne_gene = round ( (sum(moyenne_gen) / len(note)) , 2) 
    dico.setdefault('moyenne_gene', moyenne_gene)
    return dico

#projet
from operator import itemgetter
import csv

def Numerovalid(Numero):
    if  len(Numero)== 7 and Numero.isupper() and Numero.isalnum() and not Numero.isalpha() and not Numero.isdigit():
         return True
    else:
        return False
  
def Nomvalid(Nom):
    if len(Nom)>= 2 and Nom[0].isalpha():
        return True
    else:
        return False
  
def Prenomvalid(Prénom):
    if len(Prénom)>=3 and Prénom[0].isalpha():
        return True
    else:
        return False

cpt=0
donnees=open( "DonneesProjet.csv" , 'r')
liste= ['Numero','Nom','Prénom','Date de naissance','Classe','Note']
livre=csv.DictReader(donnees)
cle = 0
dico = dict()
dicovrai = dict()
dicofalse = dict()
for i in livre:
    dico.setdefault(cle, i)
    cle +=1
    #if Numerovalid(i["Numero"])==False:
        #for k in i:
            #print(k, i[k])
    
    cpt =cpt +1
print(cpt)
# print(dico)

compteur = 0
for k in dico:
    #print(dico[k])
    for key in dico[k]:
        verifnote(dico[k]['Note'])
        if key =="Numero": 
            numero=Numerovalid(dico[k][key])
        elif key =="Nom":
            nom = Nomvalid(dico[k][key])
        elif key =="Prénom":
            prenom=Prenomvalid(dico[k][key])            
        elif key =="Date de naissance":
            naiss=formatdate(dico[k][key])
        elif key =="Classe":
            niveau=Classe(dico[k][key]) 
        elif  key =="Note" :
            note=verifnote(dico[k][key])
            dico[k][key] = note
    #print(numero, nom, prenom, naiss, niveau, note) 
    if numero and nom and prenom and naiss and niveau and note:
        dicovrai.setdefault(compteur, dico[k])
        compteur +=1
        #print(dicovrai)
    else:
        dicofalse.setdefault(compteur, dico[k])
        compteur +=1
    
    if compteur ==100:
       break


print(dicovrai)
print()
print(150*'*')
print()
print(dicofalse)
#print(dicovrai[15]['Note']['SVT']['moyenne'])

#for key in dicovrai:
    
    #print(dicovrai[key]['Note']['moyenne_gene']) 
     
                    
     
            

