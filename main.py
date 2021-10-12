"""
Scrieți un program care implementează un calculator de
numere raționale:
- Identificați posibile cerințe
- Scrieți scenarii de rulare pentru fiecare funcționalitate
- Lucrați test-driven
- Scrieți documentație

Cerinte:
- F1: programul va afisa intotdeauna un total
- F2: adunarea unui numar rational la total
- F3: inmultirea unui numar rational la total
- F4: simplificarea totalului
- F5: clear total

Scenarii de rulare:
F1:
    aplicatie   utilizator  explicatii
1   0 / 1       -           programul afiseaza totalul

F2:
    aplicatie     utilizator    explicatii
1   0 / 1         -             programul afiseaza totalul - 0 initial
2   Dati un nr    -             programul cere utilizatorului un nr rational
3.                3 / 2         utilizatorul da nr. rational 3/2
4.  3 / 2         -             programul aduna nr. dat la total
...

Lista de activitati:
- F1:
    - a1: implementarea afisarii totalului
- F2:
    - a1: citirea unui numar rational
    - a2: adunarea a doua numere rationale
    - a3: actualizarea totalului cu numarul citit
...
"""
from Domain.numar_rational import creeaza_rational, get_str
from Logic.general_logic import aduna_rationale

nr1 = creeaza_rational(3, 2)
nr2 = creeaza_rational(4, 3)

print(get_str(aduna_rationale(nr1, nr2)))