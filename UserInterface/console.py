from Domain.numar_rational import creeaza_rational, get_str
from Logic.general_logic import aduna_rationale, simplifica_rational


def show_menu():
    print('1. Adunare')
    print('2. Scadere')
    print('3. Inmultire')
    print('4. Impartire')
    print('s. Simplificare')
    print('x. Iesire')

def handle_add(total):
    try:
        numarator = int(input('Dati numaratorul: '))
        numitor = int(input('Dati numitorul: '))
        rational = creeaza_rational(numarator, numitor)

        return aduna_rationale(total, rational)
    except ValueError as ve:
        print('Nu ati dat un numar valid! Detalii:', ve)
        return total


def run_ui():

    total = creeaza_rational(0, 1)
    while True:
        try:
            print(f'Totalul este: {get_str(total)}')
            show_menu()
            opt = input('Optiunea voastra: ')
            if opt == '1':
                total = handle_add(total)
            elif opt == 's':
                total = simplifica_rational(total)
            elif opt == 'x':
                break
            else:
                print('Optiune invalida, reincearca.')
        except Exception as ex:
            print('Eroare:', ex)