# LEZIONE 5 eserizio B

# creare una classe CSV file che ha come attributo il nome del file (name) e una funzione get_data() che salva ciascuna riga del file in una lista di due elementi e salva ciascuna sottolista in una lista più grande che poi verrà stampata in output
# Estendere la classe CSVFile e creare una funziona che converte a float i valori di tutte le colonne esclusa la prima, gestendo i possibili errori

class CSVFile(): # oggetto CSVFile

# funzione di inizializzazione in cui dichiaro l'attributo name, quindi il nome del file
    def __init__(self, name): 
        self.name = name

# funzione get_data()
    def get_data(self):
# creo la lista "grande" values
        values = []
# apro il file in modalità di sola lettura, gestendo il caso di un file non esistente
        try:
            my_file = open(self.name, 'r')
        except:
            print('Errore')       
# se il file è vuoto ritorno None
        if my_file == []:
            return None
# altrimenti opero su ogni riga del file
        for line in my_file:
# creo una nuova lista elements in cui salvo i valori di ciascuna linea, separandoli a livello della virgola, quindi elements[0] conterrà le date, elements[1] conterrà il numero di shampoo venduti
            elements = line.strip('\n').split(',')
# mi assicuro di scartare la prima linea del file in cui ho solo le intestazioni
            if elements[0] != 'Date':
# carico elementi sulla lista values 
                values.append(elements)
        return values

class NumericalCSVFile(CSVFile):
    def get_data(self):
        var = super().get_data() 
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
                        print('Errore: Non posso                                                    convertire a valore numerico')
                        print('Ho avuto un errore di tipo.                                          "valore" valeva "{}"'.format(valore))
                    except Exception:
                        print('Errore: non posso                                                    convertire a valore numerico')
                        print('Ho avuto un errore di                                                valore. "valore" valeva "{}"'.format(valore))
        return var # ritorno la lista con i valori convertiti a float

