# LEZIONE 6 

# creare una classe CSV file che ha come attributo il nome del file (name) e una funzione get_data() che salva ciascuna riga del file in una lista di due elementi e salva ciascuna sottolista in una lista più grande che poi verrà stampata in output
# Estendere la classe CSVFile e creare una funziona che converte a float i valori di tutte le colonne esclusa la prima, gestendo i possibili errori
# Modificare la classe madre in modo che alzi un'eccezione se il nome del file non è una stringa nell'init e modificare la funzione get_data in modo da leggere solo un intervallo di righe, aggiugendo due paramentri opzionali start e end, controllando la correttezza degli input

class CSVFile(): # oggetto CSVFile

# funzione di inizializzazione in cui dichiaro l'attributo name, quindi il nome del file
    def __init__(self, name):
# se il nome non è una stringa alzo un'eccezione
        if not type(name) == str:
            raise Exception('Errore: Il nome del file non è una stringa')
        self.name = name
        
# funzione get_data()
    def get_data(self, start=None, end=None):
# creo la lista "grande" values
        values = []
# apro il file in modalità di sola lettura, gestendo il caso di un file non esistente
        try:
            my_file = open(self.name, 'r')
        except:
            print('Errore in apertura del file') 
        my_file = my_file.read()
# se il file è vuoto ritorno None
        if my_file == []:
            return None
# altrimenti opero su ogni riga del file
        for line in my_file:
# creo una nuova lista elements in cui salvo i valori di ciascuna linea, separandoli a livello della virgola, quindi elements[0] conterrà le date, elements[1] conterrà il numero di shampoo venduti
            elements = line.strip('\n').split(',')
            if elements[0] != 'Date':
# carico elementi sulla lista values 
                values.append(elements)
# PRIMO CASO: 
# sia start che end sono None, allora come da richiesta ritorno values[1:]
            if start == None and end == None:
                return values
# se start vale 0 c'è un errore, alzo un'eccezione
            if start == 0:
                raise Exception('Errore: start vale 0')
                return None
            dim = len(my_file)
# SECONDO CASO:
# se SOLO start vale None
            if start == None:
# provo a convertire end a intero e faccio altri controlli
                try:
                    end_int = int(end)
# se non sono riuscito a convertire a intero alzo un'eccezione
                except: 
                    raise Exception('Errore di conversione di end a intero')
                    return None
# se end negativo alzo un'eccezione
                if end_int < 0:
                    raise Exception('Errore: end negativo')
                    return None
# altrimenti controllo che end sia anche minore della dimensione del file
                else:
                    if end_int < dim:
                        return values[0:end_int]
                    else:
                        raise Exception('Errore: end maggiore del numero                                      di righe del file')
                        return None
# TERZO CASO
# se SOLO end vale None
            if end == None:
# provo a convertire start a intero
                try:
                    start_int = int(start)
# se non riesco a convertire start a intero alzo un'eccezione
                except:
                    raise Exception('Errore di conversione di start a                                     intero')
                    return None 
# se start negativo alzo un'eccezione
                if start_int < 0:
                    raise Exception('Errore: start negativo')
                    return None
# altrimenti controllo che start sia anche minore di dim
                else:
                    if start_int < dim:
                        return values[start_int:]
                    else:
                        raise Exception('Errore: start maggiore del                                           numero di righe del file')
                        return None
# QUARTO CASO
# sia start che end NON sono None
            if not start == None and end == None:
# provo a convertire start e end a intero
                try:
                    start_int = int(start)
                    end_int = int(end)
                except:
                    raise Exception('Errore nella conversione')
                    return None
# se sono negativi alzo un'eccezione
                if start_int < 0 or end_int < 0:
                    raise Exception('Errore: start e/o end negativi')
                    return None
# se start e/o end sono maggiori della lunghezza del file alzo un'eccezione
                if start_int > dim or end_int > dim:
                    raise Exception('Errore: start e/o end maggiori di dim')
                    return None
# se start è maggiore di end alzo un'eccezione
                if start_int > end_int:
                    raise Exception('Errore: start maggiore di end')
                    return None
                return values[start_int:end_int]

class NumericalCSVFile(CSVFile):
    def get_data(self, *args, **kwargs):
        var = super().get_data(*args, **kwargs) 
        # var contiene la lista values della funzione madre get_data
        for item in var: # itero su ogni sottolista della lista var
            for i, element in enumerate(item): 
            # itero su ogni elemento della sottolista
                # devo valutare solo le colonne diversa dalla prima
                if(i != 0):
                    try:
                        valore = float(element) # converto a float
                        item[i] = valore
                        # carico il valore convertito a float nella lista
                    except TypeError:
                        print('Errore: Non posso                                                              convertire a valore numerico')
                        print('Ho avuto un errore di tipo.                                                    "valore" valeva "{}"'.format(valore))
                    except Exception:
                        print('Errore: non posso                                                              convertire a valore numerico')
                        print('Ho avuto un errore di                                                          valore. "valore" valeva "{}"'.format(valore))
# ritorno la lista con i valori convertiti a float
        return var 


#file_name = 'shampoo_sales.csv'
#num_csv_file = CSVFile(file_name)
#start = 5
#end = 10
#print('{}'.format(num_csv_file.get_data(start, end)))