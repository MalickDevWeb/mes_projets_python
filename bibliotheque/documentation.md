# Documentation technique - Bibliotheque

## 1. Objectif

Ce projet propose une gestion minimale de bibliotheque en mode console:
ajout, suppression, emprunt, retour, affichage et recherche de livres.

## 2. Architecture

Le projet suit une separation simple en 3 modules:

- `bibliotheque.py`
Controleur principal (menu, saisies, orchestration).
- `utils.py`
Logique metier et stockage en memoire.
- `view.py`
Affichage des ecrans et options de menu.

## 3. Donnees et structure interne

Le stockage est en memoire via une variable globale:

```python
livres = []
```

Chaque element de `livres` est un dictionnaire:

```python
{
    "isbn": "13_chiffres",
    "titre": "Texte",
    "auteur": "Texte",
    "disponible": True | False
}
```

## 4. Detail des fonctions

### 4.1 `bibliotheque.py`

- `generer_isbn()`
Genere une chaine aleatoire de 13 chiffres.

- `ajouter_livre()`
Lit le titre et l'auteur, verifie les champs, verifie les doublons,
cree le dictionnaire livre puis appelle `utils.ajouter_livre`.

- `supprimer_livre()`
Affiche la liste, lit un numero, convertit en index et supprime via
`utils.supprimer_livre_par_index`.

- `emprunter_livre()`
Affiche les livres disponibles, lit un ISBN, puis appelle
`utils.emprunter_livre`.

- `rendre_livre()`
Lit un ISBN et appelle `utils.rendre_livre`.

- `afficher_tous_les_livres()`
Relais vers `utils.afficher_livres`.

- `afficher_livres_disponibles()`
Relais vers `utils.afficher_livres_disponibles`.

- `rechercher_livres()`
Lit un mot cle, appelle `utils.rechercher_livres`, puis affiche les resultats.

- `boucle_principale()`
Boucle interactive du menu et routage par choix utilisateur.

### 4.2 `utils.py`

- `afficher_livres(liste_livres=None)`
Affiche une liste formatee. Si aucun parametre, affiche tout `livres`.

- `afficher_livres_disponibles()`
Filtre les livres disponibles et les affiche.

- `ajouter_livre(livre)`
Ajoute un dictionnaire livre dans la liste globale.

- `livre_existe_deja(titre, auteur)`
Controle doublon par comparaison normalisee (minuscules + trim).

- `rechercher_livres(mot_cle)`
Retourne les livres dont le titre ou l'auteur contient le mot cle.

- `supprimer_livre_par_index(index)`
Supprime et retourne le livre si l'index est valide, sinon `None`.

- `chercher_par_isbn(isbn)`
Retourne le livre correspondant ou `None`.

- `emprunter_livre(isbn)`
Passe `disponible` a `False` si possible.
Retourne `(succes, message)`.

- `rendre_livre(isbn)`
Passe `disponible` a `True` si possible.
Retourne `(succes, message)`.

### 4.3 `view.py`

- `afficher_accueil()`
Affiche le titre de l'application.

- `afficher_menu()`
Affiche les options de menu.

## 5. Flux utilisateur principal

1. L'utilisateur lance `python bibliotheque/bibliotheque.py`.
2. Le menu s'affiche.
3. L'utilisateur choisit une option.
4. Le controleur appelle la logique metier dans `utils.py`.
5. Resultat affiche en console.

## 6. Regles metier

- Un livre doit avoir `titre` et `auteur` non vides.
- Un doublon est detecte sur `(titre, auteur)`.
- Seuls les livres disponibles peuvent etre empruntes.
- Seuls les livres empruntes peuvent etre rendus.

## 7. Limites connues

- Donnees non persistantes.
- ISBN potentiellement duplique (aleatoire).
- Aucun export/import.

## 8. Pistes d'amelioration

- Persistance JSON ou SQLite.
- Verification stricte d'unicite ISBN.
- Ajout d'un historique d'emprunts.
- Tests unitaires (`pytest`).
