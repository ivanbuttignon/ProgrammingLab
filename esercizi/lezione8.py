# LEZIONE 8

class Model():
    def fit(self, data):
        #Fit non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        #Predict non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):

    def avg_increment(self, data):
        if not type(data) == list:
            raise Exception('Errore: argomento della funzione non è una                   lista')
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
                    raise Exception('Errore: trovato un valore negativo nella                     lista')
                if prev_value == None:
                    prev_value = item
                variazione = variazione + (item - prev_value)
                prev_value = item
            variazione = variazione / n
            return variazione
        
    def predict(self, data):
        variazione = self.avg_increment(data)
        prediction = data[-1] + variazione
        return prediction
        
class FitIncrementModel(IncrementModel):
    
    def fit(self, data):
        variazione = super().avg_increment(data)
        return variazione
        
    def predict(self, lista1, lista2): 
    #lista1 valori degli ultimi 3 mesi
    #lista2 valori da passare al fit
        avg_incr_1 = self.fit(lista2)
        avg_incr_2 = super().avg_increment(lista1)
        prediction = lista1[-1] + ((avg_incr_1 + avg_incr_2)/2)
        return prediction
        


lista1 = [50, 52, 60]
lista2 = [8, 19, 31, 41]
fit_increment_model = FitIncrementModel()
previsione = fit_increment_model.predict(lista1, lista2)
print('Previsione: {}'.format(previsione))