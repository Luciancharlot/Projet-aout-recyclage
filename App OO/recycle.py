import re

class Dechet:
    def __init__(self, nom, type_poubelle):
        self.__nom = nom
        self.__type_poubelle = type_poubelle

    def obtenir_type_poubelle(self):
        return self.__type_poubelle

    def __str__(self):
        return self.__nom


class DechetSpecial(Dechet):
    """ Représente un déchet avec une propriété spéciale. """
    
    def __init__(self, nom, type_poubelle, propriete_speciale):
        super().__init__(nom, type_poubelle)
        self.__propriete_speciale = propriete_speciale

    def obtenir_propriete(self):
        return self.__propriete_speciale


class Poubelle:
    def __init__(self, type_poubelle):
        self.__type_poubelle = type_poubelle

    def obtenir_type(self):
        return self.__type_poubelle

    def __str__(self):
        return self.obtenir_type()


def verifie_existence(func):
    def wrapper(*args, **kwargs):
        gestionnaire = args[0]
        
        if 'dechet_obj' in kwargs:
            dechet_nom = kwargs['dechet_obj']._Dechet__nom
        else:
            dechet_nom = args[1]

        if any(d for d in gestionnaire._GestionDechet__dechets if d._Dechet__nom.lower() == dechet_nom.lower()):
            print("Ce déchet existe déjà!")
            return

        return func(*args, **kwargs)
    return wrapper


class GestionDechet:
    """ Gère une collection de déchets et de poubelles. """
    TYPES_POUBELLES_VALABLES = [
        "PMC (bleue)", "Papier-Carton (jaune)", "Verre", "Déchets verts (verte)",
        "Parc à conteneurs", "Résiduels (grise/noir)", "Radioactif"
    ]

    def __init__(self):
        self.__dechets = []
        self.__poubelles = []

    @verifie_existence
    def ajouter_dechet(self, nom=None, type_poubelle=None, propriete_speciale=None, dechet_obj=None):
        if dechet_obj and isinstance(dechet_obj, Dechet):
            self.__dechets.append(dechet_obj)
        elif nom and type_poubelle:
            if type_poubelle not in self.TYPES_POUBELLES_VALABLES:
                raise ValueError(f"Type de poubelle {type_poubelle} non valide.")
            if propriete_speciale:
                dechet = DechetSpecial(nom, type_poubelle, propriete_speciale)
            else:
                dechet = Dechet(nom, type_poubelle)
            self.__dechets.append(dechet)
        else:
            raise ValueError("Informations invalides pour ajouter un déchet.")

    def generer_liste_dechets(self):
        for dechet in self.__dechets:
            yield dechet

    def lister_dechets(self):
        for dechet in sorted(self.generer_liste_dechets(), key=lambda x: x._Dechet__nom.lower()):
            print(f"{dechet} -> {dechet.obtenir_type_poubelle()}")

    """def chercher_dechet(self, fragment_nom):
        dechets_trouves = []
        for dechet in self.__dechets:
            if fragment_nom.lower() in dechet._Dechet__nom.lower():
                dechets_trouves.append(dechet)           
        return dechets_trouves"""

    def chercher_dechet(self, fragment_nom):
        return list(filter(lambda d: fragment_nom.lower() in d._Dechet__nom.lower(), self.__dechets))

    def trier_dechet(self, dechet):
        for poubelle in self.__poubelles:
            if dechet.obtenir_type_poubelle() == poubelle.obtenir_type():
                return poubelle
        return None

    def ajouter_poubelle(self, type_poubelle):
        if type_poubelle not in self.TYPES_POUBELLES_VALABLES:
            raise ValueError(f"Type de poubelle {type_poubelle} non valide.")
        poubelle = Poubelle(type_poubelle)
        self.__poubelles.append(poubelle)


if __name__ == "__main__":
    gestionnaire = GestionDechet()

    types_poubelles = map(lambda type_: gestionnaire.ajouter_poubelle(type_), GestionDechet.TYPES_POUBELLES_VALABLES)
    list(types_poubelles)
    

    dechets = [
        ("Bouteille en plastique", "PMC (bleue)"),
        ("Canette", "PMC (bleue)"),
        ("Carton de lait", "PMC (bleue)"),
        ("Journal", "Papier-Carton (jaune)"),
        ("Boîte en carton", "Papier-Carton (jaune)"),
        ("Bouteille en verre", "Verre"),
        ("Feuilles mortes", "Parc à conteneurs"),
        ("Herbe de tondeuse", "Parc à conteneurs"),
        ("Restes de nourriture", "Déchets verts (verte)"),
        ("Brique", "Parc à conteneurs"),
        ("Sachet de chips", "PMC (bleue)"),
        ("Papier aluminium", "Résiduels (grise/noir)"),
        ("Frigolite", "Parc à conteneurs"),
        ("Uranium", "Radioactif", "Mettre des gants avant de trier!"),
    ]
    for dechet in dechets:
        gestionnaire.ajouter_dechet(*dechet)

    while True:
        try:
            print("\nApplication de Tri des Déchets")
            print("1. Trier un déchet")
            print("2. Ajouter un nouveau type de déchet")
            print("3. Lister tous les déchets")
            print("4. Chercher un type de déchet dans une poubelle")
            print("5. Quitter")
            pattern = re.compile(r'^[1-5]$')
            choix = input("> ")

            if not pattern.match(choix):
                raise ValueError("Choix invalide!")

            

            if choix == "1":
                nom_dechet = input("\nEntrez le nom du déchet: ")
                dechets_trouves = gestionnaire.chercher_dechet(nom_dechet)
                dechets_trouves = sorted(dechets_trouves, key=lambda x: x._Dechet__nom.lower()) 

                if dechets_trouves:
                    if len(dechets_trouves) == 1:
                        poubelle_recommandee = gestionnaire.trier_dechet(dechets_trouves[0])
                        print(f"\nJetez le {dechets_trouves[0]} dans la poubelle {poubelle_recommandee}.")
                    else:
                        print("\nPlusieurs déchets correspondent à votre recherche :")
                        for index, dechet in enumerate(dechets_trouves, start=1):
                            print(f"{index}. {dechet}")

                        while True:
                            try:
                                selection = int(input("\nSélectionnez le numéro correspondant à votre déchet: "))
                                if 1 <= selection <= len(dechets_trouves):
                                    poubelle_recommandee = gestionnaire.trier_dechet(dechets_trouves[selection-1])
                                    print(f"\nJetez le {dechets_trouves[selection-1]} dans la poubelle {poubelle_recommandee}.")
                                    break
                                else:
                                    print("Numéro invalide, veuillez réessayer.")
                            except ValueError:
                                print("Entrée invalide, veuillez réessayer.")
                else:
                    print("Type de déchet non trouvé.")
            elif choix == "2":
                nom_dechet = input("\nEntrez le nom du déchet: ")
                if not nom_dechet.strip():
                    raise ValueError("Le nom du déchet ne peut pas être vide.")
                
                nom_poubelle = input("\nEntrez le type de poubelle: ")
                gestionnaire.ajouter_dechet(nom_dechet, nom_poubelle)
            elif choix == "3":
                gestionnaire.lister_dechets()
            elif choix == "4":
                print("\nSélectionnez une poubelle pour voir les déchets associés:")
                
                types_poubelles_tries = sorted(GestionDechet.TYPES_POUBELLES_VALABLES)
                
                for index, type_poubelle in enumerate(types_poubelles_tries, start=1):
                    print(f"{index}. {type_poubelle}")
                
                try:
                    choix_poubelle = int(input("> "))
                    if 1 <= choix_poubelle <= len(types_poubelles_tries):
                        type_poubelle_choisi = types_poubelles_tries[choix_poubelle - 1]
                        
                        dechets_associés = sorted(
                            [dechet for dechet in gestionnaire.generer_liste_dechets() if dechet.obtenir_type_poubelle() == type_poubelle_choisi],
                            key=lambda x: x._Dechet__nom.lower()
                        )
                        
                        print(f"\nVoici les déchets qui vont dans la poubelle {type_poubelle_choisi}:")
                        for dechet in dechets_associés:
                            print(f"- {dechet}")
                    else:
                        print("\nChoix invalide!")
                except ValueError:
                    print("\nEntrée invalide, veuillez entrer un numéro.")
            elif choix == "5":
                print("\nMerci d'avoir utilisé l'Application de Tri des Déchets!")
                break
            else:
                print("\nChoix invalide, veuillez réessayer.")
        except ValueError as e:
            print(f"\nErreur : {e}")
        except Exception as e:
            print(f"\nUne erreur inattendue est survenue : {e}")