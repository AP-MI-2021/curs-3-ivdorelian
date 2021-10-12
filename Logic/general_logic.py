from Domain.numar_rational import get_numitor, get_numarator, creeaza_rational


def aduna_rationale(rational1, rational2):
    """
    Aduna doua numere rationale.
    :param rational1: primul numar rational.
    :param rational2: al doilea numar rational.
    :return: rational1 + rational2, ca numar rational nesimplificat.
    """

    numitor_comun = get_numitor(rational1) * get_numitor(rational2)
    numarator = get_numarator(rational1) * get_numitor(rational2) + \
                get_numarator(rational2) * get_numitor(rational1)
    return creeaza_rational(numarator, numitor_comun)