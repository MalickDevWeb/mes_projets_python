# Projet Bibliotheque (CLI)

Application Python en ligne de commande pour gerer une petite bibliotheque locale.

## Fonctionnalites

- Ajouter un livre
- Supprimer un livre
- Emprunter un livre
- Rendre un livre
- Rechercher un livre par mot cle
- Afficher tous les livres
- Afficher uniquement les livres disponibles

## Prerequis

- Python 3.10+

## Lancer le projet

Depuis la racine:

```bash
python bibliotheque/bibliotheque.py
```

Depuis le dossier `bibliotheque/`:

```bash
python bibliotheque.py
```

## Structure du projet

- `bibliotheque.py`
Point d'entree, boucle du menu et gestion des interactions utilisateur.
- `utils.py`
Logique metier (stockage en memoire, recherche, ajout, suppression, emprunt, retour).
- `view.py`
Affichage du titre et du menu.
- `documentation.md`
Documentation technique detaillee du projet.

## Modele de donnees

Chaque livre est un dictionnaire Python:

```python
{
    "isbn": "1234567890123",
    "titre": "Le Petit Prince",
    "auteur": "Antoine de Saint-Exupery",
    "disponible": True
}
```

## Description du menu

- `1` Ajouter un livre:
demande `titre` et `auteur`, verifie les champs, genere un ISBN a 13 chiffres.
- `2` Supprimer un livre:
affiche les livres et supprime par numero de ligne.
- `3` Emprunter un livre:
affiche les livres disponibles, puis bascule `disponible` a `False`.
- `4` Rendre un livre:
bascule `disponible` a `True` pour l'ISBN saisi.
- `5` Afficher tous les livres:
liste complete.
- `6` Afficher les livres disponibles:
filtre sur `disponible == True`.
- `7` Rechercher un livre:
recherche sur titre et auteur (insensible a la casse).
- `0` Quitter:
fermeture du programme.

## Regles de validation

- Le titre et l'auteur sont obligatoires.
- Le doublon est detecte sur le couple `(titre, auteur)` normalise en minuscules.
- L'ISBN est genere aleatoirement (13 chiffres).

## Limitations actuelles

- Pas de persistance (pas de fichier JSON, pas de base de donnees).
- L'ISBN n'est pas garanti unique (collision aleatoire possible).
- Pas de pagination ni tri pour les grands volumes.

## Documentation detaillee

Consultez `documentation.md` pour la description de toutes les fonctions et des flux internes.
