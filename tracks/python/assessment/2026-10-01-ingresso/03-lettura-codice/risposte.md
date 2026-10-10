# Parte 3 — Lettura codice: risposte

Il compito preciso è nel commento `TASK` in cima a ogni file. Non eseguire gli snippet prima di aver risposto.
Per le previsioni dell'output scrivi l'output **riga per riga** in un blocco di codice, poi la spiegazione.

---

## 01_defaults_and_class_attrs.py — prevedi l'output e spiega

**Output previsto / problemi trovati:**

```
print(a.items) Errore, non è definito items
print(b.items) ["water"]
print(Basket.items) []
print(b.tags) []
print(c.tags) ["new"]
print(a.tags is b.tags) False
```

**Spiegazione:**


---

## 02_closures_and_iterators.py — prevedi l'output e spiega

**Output previsto / problemi trovati:**

```
** NON LO SO **
multipliers = [lambda x: x * i for i in range(1, 4)]
print([m(10) for m in multipliers])


first, *middle, last = "abcde"
print(first, middle, last)

data = [3, 8, 1]
if (n := len(data)) > 2:
    print(f"{n} items")

** CREDO DI SAPERLO **

squares = (n * n for n in range(5))
print(sum(squares)) 1+4+9+16 = 30
print(sum(squares)) 30
print(4 in squares) TRUE

```

**Spiegazione:**


---

## 03_find_the_bugs_shares.py — trova i problemi, ordinali per gravità, proponi correzioni

**Output previsto / problemi trovati:**

```
Qui se il totale è zero avremo un errore grave perché la divisione per zero non è ammessa quindi farei 

for category, amount in expenses:
    if amount > 0:
        shares[category] = round(amount / total * 100, 1)
    else:
        shares[category] = 0
return shares


qui i problemi sono:
1. inglobare tutto in un try except perché l'apertura del file può fallire
2. ogni linea del csv va validata e bisogna accertarsi che veramente contiene quelle due colonne, in caso negativo skippare e andare alla prossima senza bloccare le prossime

come si risolve in codice? non saprei provo a dare la soluzione

try :
    with open(path) as f:
        for line in f:
            commas = line.count(",")
            if commas>1:
                continue
            category, amount = line.strip().split(",")
            yield category, float(amount)
except FileNotFoundError as e:
    print("file non trovato")
except Exception as e:
    print(e)

```

**Spiegazione:**


---

## 04_equality_and_hashing.py — prevedi l'output e spiega

**Output previsto / problemi trovati:**

```
QUI NON SO NULLA

```

**Spiegazione:**


---

## 05_exceptions_flow.py — prevedi l'output, spiega, rispondi su `risky()`

**Output previsto / problemi trovati:**

```
il problema di parse è che stampa parsed anche quando l'eccezione si presenta, tipo in print(parse("x")), OPPURE NO PERCHé NELL'EXCEPT C'è IL RETURN... TRABOOCCHETTO MI SA
ANZI questo è esattamente il problema di risky(). ora ho capito


try:
    load({})
except RuntimeError as e:
    print(type(e.__cause__).__name__, e.__suppress_context__)
try:
    load({"port": 1})["x"]
except Exception as e:
    print(type(e).__name__)
    
qui il primo try fallisce e va in except, cosa stampa non lo so, non conosco gli attributi delle exception, 
il secondo try fallisce ma non perché load fallisce ma perché load torna il valore 1 e noi proviamo ad accedere alla chiave x su un intero

```

**Spiegazione:**


---

## 06_dates_and_timezones.py — giudica le tre funzioni e prevedi l'output

**Output previsto / problemi trovati:**

```
il day_bounds non ho capito come funziona,

created = datetime(2026, 10, 1, 9, 0, tzinfo=ROME)
print(is_expired(created, 2))
questa è False perché se la lanciassi ora che sono le 17.33 è false di sicuro


```

**Spiegazione:**


---

## 07_decorators_and_cache.py — prevedi l'output e trova i problemi di design di `PriceList`

**Output previsto / problemi trovati:**

```

def logged(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@logged
def total(values):
    """Sum the values."""
    return sum(values)


print(total.__name__, total.__doc__)
print(total([1, 2]))


QUESTO è ABBASTANZA SEMPLICE, DECORATORE DELLE FUNZIONE CHE printa (""calling {func.__name__}"") ogni volta che la funzione decorata viene lanciata

total.__doc__ non so cosa sia
total.__name__ immagino sia total

print(total([1, 2]))-> "calling total", "3"

```

**Spiegazione:**


---

## 08_design_order_processing.py — design: problemi, ristrutturazione, test

**Output previsto / problemi trovati:**

```
"""
    lista dei problemi:
    - OVVIAMENTE IL DB NON PUò ESSERE TRATTATO COME UNA VARIABILE
    - funzione che fa più cose
    - se il csv è formattato male non ce ne accorgiamo
    - invece di printare bad format facciamo un raise
    - posso passare un csv ma scrivere dentro fmt "json" e si rompe tutto
"""


class Processor:
    
    def __init__(self, data):
        self.data = data
        self.d = {}
        #self.db = connessione al db
        

    def to_dict(self):
        raise NotImplementedError
    
    def validate_dict(self):
        """Logica di validazione del dizionario"""
    
    def save(self):
        """Deve salvare nel DB quindi usare un ORM non in una variabile
            questo gestisce anche il progressivo processed sempre nel db
        """
        
        
    
    def send(self):
        """invia una mail al cliente"""
        

    def process(self, data, send=True):
        self.d=self.to_dict()
        self.validate_dict()
        t = 0
        for i in d["items"]:
            t += i["price"] * i["qty"]
        if t > 100:
            t = t * 0.9
        logger.debug("total.....")
        self.save()
        if send:
            self.send()
        
class CsvProcessor(Processor):
    def to_dict(self):
        """
            qui inserirei la logica di conversione da csv a dict, considerando casi limite ecc
        
        """

class JsonProcessor(Processor):
    def to_dict(self):
        """
           qui inserirei la logica di conversione da csv a dict, considerando casi limite ecc

       """

class ProcessorFactory:
    def get_processor(self, data):
        """
        se il data è csv ritorni un CSVProcessor, se Json un JSON Processor altrimenti raise Exception...
        """
```

**Spiegazione:**


---

## 09_design_exporters.py — design: problemi, estendibilità, ristrutturazione, bug latenti

**Output previsto / problemi trovati:**

```
""" 
    il problema che vedo è che all'aumentare degli exporter e dei compressor le combinazioni crescono e il numero di classi esplode, e quindi bisogna anche mantenere molte classi
    Una soluzione poterebbe essere implementare un Abstract Factory quindi avere su due assi indipendenti le due variabili ovvero l'exporter e il compressor
    
    oppure una soluzione più semplice sarebbe quella di dare come parametro del costruttore dell'exporter il tipo di compressor, ovviamente la classe Exporter che scrivo di seguito deve essere estesa per il Json e il csv
"""



class Exporter:
    
    compressor = None
    
    def __init__(self, compressor):
        self.compressor = compressor
    
    def _export(self, data):
        """
        qui mettiamo la logica di esportazione
        
        """
    def export(self):
        if self.compressor is None:
            self._export("dati non compressi")
        else:
            self._export(compressor.compress(data))


```

**Spiegazione:**


---

## 10_asyncio_timing.py — prevedi l'output (con i tempi) e spiega

**Output previsto / problemi trovati:**

```
QUESTO ARGOMENTO NON LO SO
```

**Spiegazione:**


---

Tempo impiegato: 150 min | Sicurezza (1-5): 3
