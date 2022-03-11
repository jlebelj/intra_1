
class Etudiant:
    def __init__(self, nom_etudiant: str, numero_etudiant: int):
        self.nom = nom_etudiant
        self.num = numero_etudiant


    def __str__(self):
        output = ("****************************************")
        output += (" ")
        output += (f"Numero etudiant: {self.num}")
        output += (" ")
        output += (f"Nom de l`etudiant: {self.nom}")
        output += (" ")
        output += ("****************************************")
        return output
