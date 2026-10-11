# Nota di design — 002
(Questo file è un cancello: i test controllano la forma. Si compila dopo aver scorso gli snippet senza prevedere, e prima delle previsioni. Aggiornalo ogni volta che a metà lavoro emerge un dubbio nuovo, prima di proseguire.)

## Cosa vedo negli snippet (dopo averli solo scorsi, senza prevedere)
<!-- Quali operazioni compaiono: almeno 4 righe o operatori copiati dagli snippet, ciascuno tra apici inversi `così`. Nessuna previsione qui. -->

ho visto una operazione mai vista ovvero il `+=`usato sulle tuple, e sulle stringhe ma come sappiamo sono immutabili quindi per forza di cose il += costruisce un nuovo oggetto

snapshot = `dict(original)`
`+= ["y"]`

`collection += (5,)`

## Il modello con cui ragionerò
<!-- Scrivilo come DOMANDA da farti su ogni riga, non come regola sul tipo di dato. Deve contenere la domanda (con il punto interrogativo) e usare le parole "etichetta" e "oggetto". 2-3 righe. -->
questa riga che sto leggendo modifica l'oggetto indicizzato dall'etichetta oppure ne crea uno nuovo e sposta l'etichetta? oppure sta creando una seconda etichetta per lo stesso oggetto?
## Dubbi concreti (almeno due)
<!-- Ogni dubbio: numero, la riga di codice (copiata da uno snippet, tra apici inversi), e l'esperimento che lo scioglierebbe. Formato:
1. Dubbio sulla riga `...`: non so se ... . Esperimento che lo scioglie: ... (cosa scrivo nel REPL e cosa mi aspetto di vedere)
-->
1. Dubbio sulla riga `log = []`: un altra operazione ambigua
def restart(log):
    log = []
    log.append("x")
    return log

in teoria qui il log interno alla funzione viene assegnato a una nuova lista vuota ma il log che vive fuori dalla funzione e viene passato resta com'era

Esperimento che lo scioglie: 

external_log = [1,2,3]

def restart(log):
    log = []
    log.append("x")
    return log

result_log = restart (external_log)
mi aspetto che result_log is external_log ritorna False

altro dubbio è:
2. Dubbio sulla riga `snapshot = dict(original)`: costruttore del dict che usa un dict esistente come argomento

io credo che gli oggetti saranno diversi ma non i valori, mi aspetto un comportamento uguale al copy (NON DEEPCOPY) è una ipotesi da verificare
quindi 
Esperimento che lo scioglie: 
orignal["key"] is new_dict["key"] torna true 
ma original is new_dict torna false


## Come userò il REPL
<!-- Cosa fai prima di ogni esecuzione (la riga "Atteso") e quali strumenti usi per guardare (id, is, ==, print intermedio). 1-2 righe. -->
il repl lo uso per sperimentare le mie ipotesi e corregere il modello che ho di come gira python
uso is per capire se due label puntano allo stesso oggetto, == per confrontare i valori, id per stampare l'id di un oggetto
## Aggiornamenti a metà lavoro
<!-- Facoltativo: ogni dubbio nuovo, con la riga e l'esperimento, con l'ora. Aggiungili qui prima di proseguire. -->

## Tempo: inizio 18:15 / fine 20:27 / indizi usati 0
<!-- Solo tempo di lavoro. L'aiuto su ambiente (terminale, IDE, comandi) non è un indizio e va contato a parte in risposte.md. -->
