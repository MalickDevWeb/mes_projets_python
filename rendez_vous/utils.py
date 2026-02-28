import re
from datetime import datetime

rendez_vous_list = []


def valider_date(date_str, futur_obligatoire=False):
    pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
    if not re.match(pattern, date_str):
        return False, "Format invalide. Utilisez JJ/MM/AAAA (ex: 07/02/2026)."

    jour, mois, annee = map(int, date_str.split("/"))

    try:
        date_verifiee = datetime(annee, mois, jour).date()
    except ValueError:
        return False, f"Date invalide: {date_str} n'existe pas dans le calendrier."

    if futur_obligatoire and date_verifiee < datetime.now().date():
        return False, "La date ne peut pas etre dans le passe."

    return True, ""


def valider_heure(heure_str):
    pattern = r"^([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$"
    if not re.match(pattern, heure_str):
        return False, "Format invalide. Utilisez HH:MM:SS (ex: 14:30:00)."
    return True, ""


def ajouter_rendez_vous(date, heure, description):
    rendez_vous = {"date": date, "heure": heure, "description": description}
    rendez_vous_list.append(rendez_vous)


def rechercher_rendez_vous_par_date(date):
    return [rv for rv in rendez_vous_list if rv["date"] == date]


def lister_rendez_vous():
    return rendez_vous_list


def supprimer_rendez_vous(date, heure):
    for rv in rendez_vous_list:
        if rv["date"] == date and rv["heure"] == heure:
            rendez_vous_list.remove(rv)
            return True
    return False
