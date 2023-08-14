from recycle import *
import unittest

class TestDechetMethods(unittest.TestCase):

    def test_init(self):
        dechet = Dechet("Bouteille en plastique", "PMC (bleue)")
        self.assertEqual(str(dechet), "Bouteille en plastique")
        self.assertEqual(dechet.obtenir_type_poubelle(), "PMC (bleue)")


class TestDechetSpecialMethods(unittest.TestCase):

    def test_init(self):
        dechet_special = DechetSpecial("Uranium", "Radioactif", "Haute radioactivité")
        self.assertEqual(str(dechet_special), "Uranium")
        self.assertEqual(dechet_special.obtenir_type_poubelle(), "Radioactif")
        self.assertEqual(dechet_special.obtenir_propriete(), "Haute radioactivité")


class TestPoubelleMethods(unittest.TestCase):

    def test_init(self):
        poubelle = Poubelle("PMC (bleue)")
        self.assertEqual(str(poubelle), "PMC (bleue)")


class TestGestionDechetMethods(unittest.TestCase):

    def setUp(self):
        self.gestionnaire = GestionDechet()

    def test_ajouter_dechet(self):
        self.gestionnaire.ajouter_dechet("Journal", "Papier-Carton (jaune)")
        self.assertEqual(str(self.gestionnaire.chercher_dechet("Journal")[0]), "Journal")

    def test_ajouter_dechet_existence(self):
        self.gestionnaire.ajouter_dechet("Journal", "Papier-Carton (jaune)")
        self.gestionnaire.ajouter_dechet("Journal", "Papier-Carton (jaune)")

    def test_ajouter_dechet_via_objet(self):
        dechet = Dechet("Pomme", "Déchets verts (verte)")
        self.gestionnaire.ajouter_dechet(dechet_obj=dechet)
        self.assertEqual(str(self.gestionnaire.chercher_dechet("Pomme")[0]), "Pomme")

    def test_ajouter_dechet_special(self):
        self.gestionnaire.ajouter_dechet("Uranium", "Radioactif", "Haute radioactivité")
        dechet = self.gestionnaire.chercher_dechet("Uranium")[0]
        self.assertIsInstance(dechet, DechetSpecial)
        self.assertEqual(dechet.obtenir_propriete(), "Haute radioactivité")

    def test_chercher_dechet(self):
        self.gestionnaire.ajouter_dechet("Bouteille en plastique", "PMC (bleue)")
        self.assertEqual(len(self.gestionnaire.chercher_dechet("Bouteille")), 1)

    def test_lister_dechets(self):
        self.gestionnaire.ajouter_dechet("Bouteille en plastique", "PMC (bleue)")
        self.gestionnaire.ajouter_dechet("Journal", "Papier-Carton (jaune)")
        self.gestionnaire.lister_dechets() 

    def test_ajouter_poubelle(self):
        self.gestionnaire.ajouter_poubelle("PMC (bleue)")
        with self.assertRaises(ValueError):
            self.gestionnaire.ajouter_poubelle("Poubelle non valide")

    def test_trier_dechet(self):
        dechet = Dechet("Journal", "Papier-Carton (jaune)")
        self.gestionnaire.ajouter_dechet(dechet_obj=dechet)
        self.gestionnaire.ajouter_poubelle("Papier-Carton (jaune)")
        poubelle_trouvee = self.gestionnaire.trier_dechet(dechet)
        self.assertEqual(str(poubelle_trouvee), "Papier-Carton (jaune)")


if __name__ == '__main__':
    unittest.main()
