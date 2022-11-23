#LEZIONE 3

# leggo valori file shampoo_sales, li salvo e li sommo

def sum_csv(file_name):
# lista che contiene i valori degli shampoo venduti
    values = [] # inizialmente vuota
# apro il file in modalità sola lettura 'r'
    my_file = open(file_name, 'r') 
# se il file è vuoto ritorno None
    if my_file == []:
        return None
# altrimenti opero su ogni linea del file
    for line in my_file:
# creo una lista elements facendo lo split di        ciascuna riga del file a livello della virgola 
        elements = line.split(',') 
# mi assicuro di non fare nulla se sono sulla          prima riga del file
        if elements[0] != 'Date':
# salvo le date in una variabile che pongo quindi uguale a elements[0]
            date = elements[0] 
# salvo il numero degli shampoo venduti in una variabile value, convertendoli a float
            value = float(elements[1])
# "carico" ciascun value nella lista values inizializzata in precedenza
            values.append(value)
# calcolo la somma degli elementi di values
    sum = 0
    for item in values:
        sum = sum + item
    if sum == 0:
        return None
    else:
        return sum
        
#print('La somma dei valori di shampoo_sales è {}'.format(sum_csv('shampoo_sales.csv')))

    
        
        
        
