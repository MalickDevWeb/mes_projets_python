import random

import utils
import view


def generer_isbn():
    return "".join(str(random.randint(0, 9)) for _ in range(13))


def ajouter_livre():
    titre = input("Titre: ").strip()
    auteur = input("Auteur: ").strip()

    if not titre or not auteur:
        print("Le titre et l'auteur sont obligatoires.")
        return

    if utils.livre_existe_deja(titre, auteur):
        print("Ce livre existe deja.")
        return

    livre = {
        "isbn": generer_isbn(),
        "titre": titre,
        "auteur": auteur,
        "disponible": True,
    }
    utils.ajouter_livre(livre)
    print(f"Livre ajoute avec succes. ISBN: {livre['isbn']}")


def supprimer_livre():
    if not utils.livres:
        print("Aucun livre a supprimer.")
        return

    utils.afficher_livres()
    choix = input("Numero du livre a supprimer: ").strip()

    if not choix.isdigit():
        print("Veuillez entrer un numero valide.")
        return

    index = int(choix) - 1
    livre_supprime = utils.supprimer_livre_par_index(index)

    if livre_supprime is None:
        print("Numero invalide.")
        return

    print(f"Livre supprime: {livre_supprime['titre']} ({livre_supprime['isbn']})")


def emprunter_livre():
    livres_disponibles = utils.afficher_livres_disponibles()
    if not livres_disponibles:
        return

    isbn = input("ISBN du livre a emprunter: ").strip()
    _, message = utils.emprunter_livre(isbn)
    print(message)


def rendre_livre():
    isbn = input("ISBN du livre a rendre: ").strip()
    _, message = utils.rendre_livre(isbn)
    print(message)


def afficher_tous_les_livres():
    utils.afficher_livres()


def afficher_livres_disponibles():
    utils.afficher_livres_disponibles()


def rechercher_livres():
    mot_cle = input("Titre ou auteur a rechercher: ").strip()

    if not mot_cle:
        print("La recherche ne peut pas etre vide.")
        return

    resultats = utils.rechercher_livres(mot_cle)
    if not resultats:
        print("Aucun livre trouve.")
        return

    print(f"{len(resultats)} livre(s) trouve(s):")
    utils.afficher_livres(resultats)


def boucle_principale():
    while True:
        view.afficher_accueil()
        view.afficher_menu()
        choix = input("\nVotre choix: ").strip()

        if choix == "1":
            ajouter_livre()
        elif choix == "2":
            supprimer_livre()
        elif choix == "3":
            emprunter_livre()
        elif choix == "4":
            rendre_livre()
        elif choix == "5":
            afficher_tous_les_livres()
        elif choix == "6":
            afficher_livres_disponibles()
        elif choix == "7":
            rechercher_livres()
        elif choix == "0":
            print("Au revoir.")
            break
        else:
            print("Option invalide.")


if __name__ == "__main__":
    boucle_principale()
