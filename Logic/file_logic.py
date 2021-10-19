import json


def read_total(filename):
    """
    Citeste fisierul care contine totalul.
    :param filename: numele fisierului.
    :return: totalul
    """
    with open(filename, 'r') as f:
        return json.load(f)


def save_total(filename, total):
    """
    Salveaza totalul intr-un fisier.
    :param filename: fisierul in care se face salvarea.
    :param total: numar rational, totalul care se salveaza.
    """
    with open(filename, 'w') as f:
        json.dump(total, f)