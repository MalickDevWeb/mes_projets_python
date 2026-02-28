# Projet Rendez-vous (CLI)

Application Python en ligne de commande pour gerer un agenda simple de rendez-vous.

## Fonctionnalites

- Ajouter un rendez-vous
- Rechercher des rendez-vous par date
- Afficher tous les rendez-vous
- Supprimer un rendez-vous par date + heure

## Prerequis

- Python 3.10+

## Lancer le projet

Depuis la racine:

```bash
python rendez_vous/rendez_vous.py
```

Depuis le dossier `rendez_vous/`:

```bash
python rendez_vous.py
```

## Structure du projet

- `rendez_vous.py`
Point d'entree, menu et saisie utilisateur.
- `utils.py`
Validations (date/heure) et operations metier.
- `view.py`
Affichage du menu et format d'affichage d'un rendez-vous.
- `documentation.md`
Documentation technique detaillee du projet.

## Modele de donnees

Chaque rendez-vous est stocke en memoire sous forme de dictionnaire:

```python
{
    "date": "31/12/2099",
    "heure": "10:30:00",
    "description": "Consultation client"
}
```

## Description du menu

- `1` Ajouter un rendez-vous:
date valide + heure valide + description non vide.
- `2` Rechercher par date:
affiche tous les rendez-vous correspondant a la date.
- `3` Afficher tous les rendez-vous:
liste complete.
- `4` Supprimer un rendez-vous:
suppression par couple `(date, heure)`.
- `5` Quitter:
fermeture du programme.

## Regles de validation

- Date au format `JJ/MM/AAAA`
- Heure au format `HH:MM:SS`
- Lors de l'ajout: la date doit etre aujourd'hui ou future.
- Les champs texte ne peuvent pas etre vides.

## Limitations actuelles

- Pas de persistance des donnees.
- Pas de verification de chevauchement d'horaire.
- Pas de tri automatique par date/heure.

## Documentation detaillee

Consultez `documentation.md` pour les details fonction par fonction.
