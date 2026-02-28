livres = []


def afficher_livres(liste_livres=None):
    livres_a_afficher = livres if liste_livres is None else liste_livres

    if not livres_a_afficher:
        print("Aucun livre enregistre.")
        return

    for index, livre in enumerate(livres_a_afficher, start=1):
        disponibilite = "Oui" if livre["disponible"] else "Non"
        print(
            f"{index}. {livre['isbn']} | {livre['titre']} | {livre['auteur']} | "
            f"Disponible: {disponibilite}"
        )


def afficher_livres_disponibles():
    livres_disponibles = [livre for livre in livres if livre["disponible"]]

    if not livres_disponibles:
        print("Aucun livre disponible.")
        return []

    afficher_livres(livres_disponibles)
    return livres_disponibles


def ajouter_livre(livre):
    livres.append(livre)


def livre_existe_deja(titre, auteur):
    titre_normalise = titre.strip().lower()
    auteur_normalise = auteur.strip().lower()

    return any(
        livre["titre"].strip().lower() == titre_normalise
        and livre["auteur"].strip().lower() == auteur_normalise
        for livre in livres
    )


def rechercher_livres(mot_cle):
    mot_cle = mot_cle.strip().lower()

    return [
        livre
        for livre in livres
        if mot_cle in livre["titre"].lower() or mot_cle in livre["auteur"].lower()
    ]


def supprimer_livre_par_index(index):
    if 0 <= index < len(livres):
        return livres.pop(index)
    return None


def chercher_par_isbn(isbn):
    for livre in livres:
        if livre["isbn"] == isbn:
            return livre
    return None


def emprunter_livre(isbn):
    livre = chercher_par_isbn(isbn)

    if livre is None:
        return False, "Aucun livre avec cet ISBN."
    if not livre["disponible"]:
        return False, "Ce livre n'est pas disponible."

    livre["disponible"] = False
    return True, "Livre emprunte avec succes."


def rendre_livre(isbn):
    livre = chercher_par_isbn(isbn)

    if livre is None:
        return False, "Aucun livre avec cet ISBN."
    if livre["disponible"]:
        return False, "Ce livre est deja disponible."

    livre["disponible"] = True
    return True, "Livre rendu avec succes."
