
def creeaza_rational(numarator: int, numitor: int):
    """
    Creeaza un numar rational ca fractie.
    :param numarator: numaratorul fractiei
    :param numitor: numitorul fractiei
    :return: un numar rational
    """
    #return (numarator, numitor)
    return {'numarator': numarator, 'numitor': numitor}

def get_numarator(nr_rational):
    """
    Getter pentru numarator
    :param nr_rational: numarul rational.
    :return: numaratorul lui nr_rational
    """
    #return nr_rational[0]
    return nr_rational['numarator']

def get_numitor(nr_rational):
    """
    Getter pentru numitor
    :param nr_rational: numarul rational
    :return: numitorul lui nr_rational
    """
    #return nr_rational[1]
    return nr_rational['numitor']

def get_str(nr_rational):
    """
    Determina reprezentarea ca string a numarului rational.
    :param nr_rational: numarul rational.
    :return: numarator / numitor
    """
    return f'{get_numarator(nr_rational)} / {get_numitor(nr_rational)}'