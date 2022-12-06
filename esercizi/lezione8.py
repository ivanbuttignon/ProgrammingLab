# LEZIONE 8



class Model():
    def fit(self, data):
        #Fit non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        #Predict non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):
    
    def predict(self, data):
        if not type(data) == list:
            raise Exception('Errore: argomento della funzione non è una lista')
            return None
        if data == []:
            raise Exception('Errore: lista vuota')
            return None
        else:
            prev_value = None
            variazione = 0
            n = len(data) - 1 
            for item in data:
                try:
                    item = float(item)
                except TypeError:
                    raise Exception('Ho avuto un errore di tipo durante la                                 conversione')
                except ValueError:
                    raise Exception('Ho avuto un errore di valore durante la                               conversione')
                if item < 0:
                    raise Exception('Errore: trovato un valore negativo nella lista')
                if prev_value == None:
                    prev_value = item
                variazione = variazione + (item - prev_value)
                prev_value = item
            variazione = variazione / n
            prediction = data[-1] + variazione
            return prediction
        

#prova = [50, 52, 60]
#increment_model = IncrementModel()
#previsione = increment_model.predict(prova)
#print('Previsione: {}'.format(previsione))