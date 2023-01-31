class ExamException(Exception):
        pass

class CSVFile(): 
    def __init__(self, name): 
        self.name = name

    def get_data(self):
        pass
        
class CSVTimeSeriesFile(CSVFile):
    def get_data(self):
        time_series = []
# apro il file in modalità di sola lettura, gestendo il caso di un file non esistente
        try:
            time_series_file = open(self.name, 'r')
        except:
            raise ExamException('Errore nell apertura/lettura del file')
        if time_series_file == []:
            raise ExamException('Errore: file vuoto')
# altrimenti opero su ogni riga del file
        for line in time_series_file:
            elements = line.strip('\n').split(',')
# mi assicuro di scartare la prima linea del file in cui ho solo le intestazioni
            if elements[0] != 'epoch':
                try:
                    elements[0] = int(elements[0])
                except:
                    continue
                try:
                    elements[1] = float(elements[1])
                except:
                    continue
                time_series.append(elements)
        return time_series

time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()


def compute_daily_max_difference(time_series):
    #inizializzo con dati prima riga
    day_start_epoch = time_series[0][0] - (time_series[0][0]%86400)
    #creo lista risultati
    result = []
    #creo lista dei giorni
    days = []
    #creo lista dei singoli giorni delle temperature
    day_list = []
    for j in range(len(time_series)):
        #gestisco tutte le righe diverse dall'ultima
        if j < len(time_series) - 1:
            epoch = time_series[j][0]
            temperature = time_series[j][1]
            #caso dello stesso giorno
            if epoch - day_start_epoch < 86400:
                day_list.append(temperature)
            #caso di giorno diverso
            else:
                days.append(day_list)                    
                day_start_epoch = epoch - epoch%86400
                day_list = []
                day_list.append(temperature)
        #gestisco l'ultima riga
        else:
            if epoch - day_start_epoch < 86400:
                day_list.append(temperature)
                days.append(day_list)
            else:
                days.append(day_list)
                day_list = []
                day_list.append(temperature)
                days.append(day_list)
    for i in range(len(days)):
        if len(days[i]) == 1: 
            result.append(None)
        else:
            massimo = max(days[i])
            minimo = min(days[i])
            result.append(round((massimo-minimo),3))
    return result

res = compute_daily_max_difference(time_series)

print(res)

                
        
            
        
    


