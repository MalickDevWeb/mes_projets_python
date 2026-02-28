# Projets Python CLI

Ce depot contient 2 projets Python en ligne de commande:

- `bibliotheque/` : gestion simple de livres (ajout, emprunt, retour, recherche).
- `rendez_vous/` : gestion simple de rendez-vous (ajout, recherche par date, suppression).

## Prerequis

- Python 3.10 ou plus recent
- Terminal (Linux, macOS, Windows)

## Lancement rapide

Depuis la racine du depot:

```bash
python bibliotheque/bibliotheque.py
python rendez_vous/rendez_vous.py
```

## Structure du depot

```text
gestion-bibl/
├── README.md
├── bibliotheque/
│   ├── README.md
│   ├── documentation.md
│   ├── bibliotheque.py
│   ├── utils.py
│   └── view.py
└── rendez_vous/
    ├── README.md
    ├── documentation.md
    ├── rendez_vous.py
    ├── utils.py
    └── view.py
```

## Documentation detaillee

- Projet bibliotheque: `bibliotheque/README.md` et `bibliotheque/documentation.md`
- Projet rendez-vous: `rendez_vous/README.md` et `rendez_vous/documentation.md`

## Remarque importante

Les deux projets stockent les donnees en memoire. Les informations sont perdues a la fermeture du programme.
