def afficher_titre():
    print("\n--- Menu de l'Agenda de Rendez-vous ---")


def afficher_menu():
    print("1. Ajouter un rendez-vous")
    print("2. Rechercher les rendez-vous par date")
    print("3. Afficher tous les rendez-vous")
    print("4. Supprimer un rendez-vous")
    print("5. Quitter")


def afficher_rendez_vous(rendez_vous):
    print(
        f"Rendez-vous le {rendez_vous['date']} a {rendez_vous['heure']}: "
        f"{rendez_vous['description']}"
    )
