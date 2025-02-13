import random
from personne import *
 
noms=['DIOP','NDIAYE','GUEYE','FALL','SARR','DER','GASSAMA','SALL','SONKO','FAYE']
prenom=['Papa','Moussa','Aly','Jean','George','Edouard','Mouhamed','Saliou','Amy','Ndeye']
sexes=['M','F']
lPersonnes=[]
#Créer un objet dont les valeurs sont au hasard dans les lites ci-dessus avec 10<=age<=100
for i in range(100):
    p=Personne(random.choice(noms),random.choice(prenom),random.choice(sexes),random.randint(10,100))
    lPersonnes.append(p)
print("Liste de personnes")

# Affichage de la liste des personnes
print("Liste des personnes générées :")
for personne in lPersonnes:
    print(personne)  