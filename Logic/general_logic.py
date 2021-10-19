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

def simplifica_rational(rational):
    """
    Simplifica un numar rational.
    :param rational: numarul rational.
    :return: numarul rational rezultat din simplificarea lui rational.
    """

    numarator = get_numarator(rational)
    numitor = get_numitor(rational)
    # cmmdc(a, b) = cmmdc(b, a % b)
    while numitor != 0:
        numarator, numitor = numitor, numarator % numitor
        #r = numarator % numitor
        #numarator = numitor
        #numitor = r
    cmmdc = numarator
    return creeaza_rational(get_numarator(rational) // cmmdc,
                            get_numitor(rational) // cmmdc)
