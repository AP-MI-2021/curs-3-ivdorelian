from Domain.numar_rational import creeaza_rational, get_numarator, get_numitor
from Logic.general_logic import aduna_rationale, simplifica_rational


def test_aduna_rationale():
    r1 = creeaza_rational(5, 4)
    r2 = creeaza_rational(2, 7)
    r3 = creeaza_rational(8, 3)

    r1_plus_r2 = aduna_rationale(r1, r2)
    expected_numarator = get_numarator(r2)*get_numitor(r1) + get_numitor(r2)*get_numarator(r1)
    expected_numitor = get_numitor(r1) * get_numitor(r2)
    assert get_numarator(r1_plus_r2) == expected_numarator
    assert get_numitor(r1_plus_r2) == expected_numitor

    # TODO ...

def test_simplifica_rational():
    r1 = creeaza_rational(20, 4)
    simplificat = simplifica_rational(r1)
    assert get_numarator(simplificat) == 5
    assert get_numitor(simplificat) == 1

