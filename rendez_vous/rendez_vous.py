import utils
import view


def menu():
    while True:
        view.afficher_titre()
        view.afficher_menu()

        choix = input("Veuillez choisir une option (1-5): ").strip()
        if choix == "1":
            ajouter_rendez_vous()
        elif choix == "2":
            rechercher_par_date()
        elif choix == "3":
            afficher_tous_les_rendez_vous()
        elif choix == "4":
            supprimer_rendez_vous()
        elif choix == "5":
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez reessayer.")


def saisir_champs(message):
    while True:
        valeur = input(message)
        if valeur.strip():
            return valeur
        print("Ce champ ne peut pas etre vide. Veuillez reessayer.")


def saisir_date(futur_obligatoire=False):
    while True:
        date_str = saisir_champs("Date (JJ/MM/AAAA) : ").strip()
        est_valide, message = utils.valider_date(date_str, futur_obligatoire=futur_obligatoire)
        if est_valide:
            return date_str
        print(message)


def saisir_heure():
    while True:
        heure_str = saisir_champs("Heure (HH:MM:SS) : ").strip()
        est_valide, message = utils.valider_heure(heure_str)
        if est_valide:
            return heure_str
        print(message)


def ajouter_rendez_vous():
    date = saisir_date(futur_obligatoire=True)
    heure = saisir_heure()
    description = saisir_champs("Entrez la description du rendez-vous: ")
    utils.ajouter_rendez_vous(date, heure, description)
    print("Rendez-vous ajoute avec succes.")


def rechercher_par_date():
    date = saisir_date()
    trouves = utils.rechercher_rendez_vous_par_date(date)
    if not trouves:
        print("Aucun rendez-vous trouve pour cette date.")
        return

    for rv in trouves:
        view.afficher_rendez_vous(rv)


def afficher_tous_les_rendez_vous():
    rendez_vous = utils.lister_rendez_vous()
    if not rendez_vous:
        print("Aucun rendez-vous dans l'agenda.")
        return

    for rv in rendez_vous:
        view.afficher_rendez_vous(rv)


def supprimer_rendez_vous():
    date = saisir_date()
    heure = saisir_heure()
    supprime = utils.supprimer_rendez_vous(date, heure)
    if supprime:
        print("Rendez-vous supprime avec succes.")
    else:
        print("Aucun rendez-vous trouve pour cette date et heure.")


if __name__ == "__main__":
    menu()
