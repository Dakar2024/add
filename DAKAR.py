
class personne:
    def _init_(self,nom,prenom,genre,age):
        self.nom=nom
        self.prenom=prenom
        self.genre=genre
        self.age=age
# creation des setter

def setNom(self,nom):
  self.nom=nom

def setPrenom(self,prenom):
  self.prenom=prenom

def setGenre(self,genre):
  self.genre=genre    

def setAge(self,age):
  self.age=age     

#creattion des getter  

def getNom(self,nom):
  return self.nom

def setPrenom(self,prenom):
  return self.prenom

def setGenre(self,genre):
  return self.genre   

def setAge(self,age):
  return self.age    

personne1= personne ("mantsouaka","arthur","masculin", "20 ans" )
#print(f"nom:{personne1.nom},prenom:{personne1.prenom},genre:{personne1.genre},age:{personne1.age}")
print(personne1)
