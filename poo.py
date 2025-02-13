class Personne:
    # Constructeur
    def __init__(self, nom, prenom, genre, age):
        self.__nom = nom   
        self.__prenom = prenom
        self.__genre = genre
        self.__age = age

    # Getters
    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_genre(self):
        return self.__genre

    def get_age(self):
        return self.__age

    # Setters (Mutateurs)
    def set_nom(self, nom):
        self.__nom = nom

    def set_prenom(self, prenom):
        self.__prenom = prenom

    def set_genre(self, genre):
        self.__genre = genre

    def set_age(self, age):
        if age > 0:  
            self.__age = age
        else:
            print("L'âge doit être un nombre positif !")

    # Méthode pour afficher les informations
    def __str__(self):
        return f"Nom: {self.__nom}, Prénom: {self.__prenom}, Genre: {self.__genre}, Âge: {self.__age}"


if __name__ == "__main__":
    # Création d'un objet Personne
    personne1 = Personne("Mantsouaka", "Arthur", "Masculin", 30)

    print(personne1)
   

   
