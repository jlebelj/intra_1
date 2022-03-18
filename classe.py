
class Etudiant:
    def __init__(self, nom_etudiant: str, numero_etudiant: int, programme_etudiant, age_etudiant):
        self.nom = nom_etudiant
        self.num = numero_etudiant
        self.programme = programme_etudiant
        self.age = age_etudiant



    def __str__(self):
        output = ("*************************\n")
        output += (f"Numero etudiant: {self.num}\n")
        output += (f"Nom de l`etudiant: {self.nom}\n")
        output += (f"Programme de l'etudiant: {self.programme}\n")
        output ++ (f"Age de l'etudiant: {self.age}\n")
        output += ("*************************\n")
        return output
