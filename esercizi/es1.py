# definisco una lista e sommo i suoi elementi

lista = [1,3,4,7]

def sum_list(lista):
    if len(lista) == 0:
        return None
    else:
        somma = 0
        for item in lista:
            somma = somma + item
        return somma

risultato = sum_list(lista)
print('La somma è: {}'.format(risultato))