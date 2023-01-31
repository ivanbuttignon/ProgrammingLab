# creo la classe per la gestione delle eccezioni
class ExamException(Exception):
        pass

# creo la classe madre CSVFile
class CSVFile():
# metodo init con il nome del file CSV
    def __init__(self, name): 
        self.name = name
        
# metodo get_data che verrà implementato in seguito        
    def get_data(self):
        pass

# credo la sottoclasse CSVTimeSeriesFile che eredita da CSVFile
class CSVTimeSeriesFile(CSVFile):
    
#implemento il metodo get_data
    def get_data(self):
# creo la lista che verrà data in output
        time_series = []
# apro il file in modalità lettura, gestendo il caso di un file non esistente
        try:
            time_series_file = open(self.name, 'r')
        except:
            raise ExamException('Errore nell apertura/lettura del file')
# gestisco il caso di un file vuoto, alzando al caso un'eccezione
        if time_series_file.readline() == '':
            raise ExamException('Errore: file vuoto')
# se non ho avuto problemi con il file, opero su ogni sua riga
        for line in time_series_file:
# creo delle sottoliste eseguendo lo split di ciascuna riga a livello della virgola ed eliminando il carattere \n
            elements = line.strip('\n').split(',')
# scarto la prima linea del file in cui ci sono solo le intestazioni
            if elements[0] != 'epoch':
# converto i timestamp a interi, se dovessi avere problemi nel cast proseguo silenziosamente ignorando la riga in questione
                try:
                    elements[0] = int(elements[0])
                except:
                    continue
# converto i valori di temperatura a float, se dovessi avere problemi nel cast proseguo silenziosamente ignorando la riga in questione
                try:
                    elements[1] = float(elements[1])
                except:
                    continue
# aggiungo alla lista time_series le sottoliste elements, formate dalla coppia epoch - temperatura
                time_series.append(elements)
# una volta creata la lista di liste controllo che non ci siano timestamp duplicati o fuori ordine. In caso contrario alzo un'eccezione
        for i in range(len(time_series) -1):
            if time_series[i+1][0] <= time_series[i][0]:
                raise ExamException('Errore: timestamp duplicato/fuori ordine')
# se il check è andato a buon fine, ritorno la lista di liste
        return time_series

time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()

# implemento il metodo per il calcolo dell'escursione termica giornaliera
def compute_daily_max_difference(time_series):
# controllo se in input ho una lista
    if type(time_series) != list:
        raise ExamException('Errore: in input non ho una lista')
# controllo se la lista in input è vuota
    if time_series == []:
        raise ExamException('Errore: lista in input vuota')
# trovo il giorno di partenza
    day_start_epoch = time_series[0][0] - (time_series[0][0] % 86400)
# creo la lista che conterrà le escursioni termiche giornaliere
    result = []
# creo la lista che conterrà le misurazioni di temperatura (sottoforma di lista) per ogni singolo giorno
    days = []
# creo lista che conterrà tutte le misurazioni di temperatura di un giorno 
    day_list = []
# itero su tutta la lunghezza della lista time_series
    for j in range(len(time_series)):
# gestisco tutte le righe diverse dall'ultima
        if j < len(time_series) - 1:
# variabile di appoggio, epoch 
            epoch = time_series[j][0]
# variabile di appoggio, temperature
            temperature = time_series[j][1]
# gestisco il caso di misurazioni di temperatura appartenenti a uno stesso giorno
            if epoch - day_start_epoch < 86400:
# aggiugno a day_list le temperature di quello specifico giorno
                day_list.append(temperature)
# gestisco il caso in cui trovo una misurazione di temperatura di un giorno nuovo
            else:
# aggiungo alla lista days tutti i valori di temperatura raccolti per un intero giorno
                days.append(day_list)  
# aggiorno la variabile che mi determina il giorno di partenza 
                day_start_epoch = epoch - (epoch % 86400)
# setto nuovamente day_list a lista vuota perchè ora devo raccogliere tutte le misurazioni di temperatura per un giorno nuovo
                day_list = []
# aggiungo a day_list la prima temperatura del nuovo giorno
                day_list.append(temperature)
# gestisco l'ultima riga
        else:
# se la misurazione di temperatura dell'ultima riga è dello stesso giorno di quella precedente, aggiugno la rilevazione di temperatura a day_list e infine chiudo aggiungendo day_list alla lista days
            if epoch - day_start_epoch < 86400:
                day_list.append(temperature)
                days.append(day_list)
# se la misurazione di temperatura dell'ultima riga appartiene a un giorno nuovo rispetto a quella della penultima riga, aggiungo day_list a days, setto day_list a vuoto per salvare la misurazione di temperatura dell'ultima riga e solo dopo aggiungo day_list a days
            else:
                days.append(day_list)
                day_list = []
                day_list.append(temperature)
                days.append(day_list)
                
# alla fine del ciclo for ho ottenuto una lista di liste: days infatti è una lista che contiene tutte le misurazioni di temperatura (raccolte in una lista) per ogni singolo giorno

# devo ora trovare l'escursione termica di ogni singolo giorno e aggiungere tali valori alla lista result. Itero quindi su tutta la lunghezza della lista days, cioè vado a considerare ogni suo elemento (sottolista)                
    for i in range(len(days)):
# se la lunghezza della sottolista è pari a 1, quindi la sottolista ha 1 solo elemento, non posso trovare l'escursione termica e quindi aggiungo None a result
        if len(days[i]) == 1: 
            result.append(None)
# se la sottolista ha più di 1 elemento, trovo il massimo e il minimo con le rispettive funzioni built in
        else:
            massimo = max(days[i])
            minimo = min(days[i])
# aggiungo a result l'escursione termica di un giorno facendo la differenza tra la temperatura massima e quella minima
            result.append(massimo-minimo)
# ritorno la lista result con tutte le escursioni termiche giornaliere
    return result

res = compute_daily_max_difference(time_series)
print(res)

                
        
            
        
    


