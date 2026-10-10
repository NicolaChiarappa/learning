# Pattern di ragionamento

Come Nick affronta i problemi. Lo aggiornano il mentor (principalmente) e l'assessor (dopo ogni test).
Un pattern = un comportamento osservabile e ripetuto, non un giudizio sulla persona.

## Pattern attivi
<!--
### P01 — titolo (es. "Parte dal codice prima di aver chiarito l'input")
- Descrizione: ...
- Prima osservazione: YYYY-MM-DD (fonte)
- Occorrenze: n
- Tendenza: in miglioramento | stabile | in peggioramento
- Ultima evidenza: track/NNN — ...
- Abitudine correttiva concordata: ...
-->

## Punti di forza ricorrenti
(Solo se specifici e osservati più volte.)

## Pattern superati
(Spostati qui quando non compaiono per almeno 3 settimane.)

## 2026-10-10 — Test d'ingresso Python (fonte: assessor)

Osservazioni da un solo test: sono candidati a pattern, da confermare sugli esercizi. Il mentor decide se promuoverli in "Pattern attivi" con un ID. Dettagli ed evidenze in `tracks/python/assessment/2026-10-01-ingresso/risultati.md`.

- **Si ferma ai test verdi.** In S01 e S02 dichiara sicurezza 4/5 con tutti i test base passati; nei test nascosti 6/19 e 7/14. Regole scritte nella consegna non implementate (formato del messaggio d'errore, timestamp decrescenti, laziness). La consegna è letta come contesto, non come specifica da spuntare.
- **Non argomenta il perché.** Tutte le sezioni "Spiegazione" della lettura codice vuote; domande di design chiuse in 10 minuti su 40; problemi elencati senza ordine né motivazione. Parole sue: "non so spiegare perché prendere certe scelte".
- **Risponde al design con uno scheletro di classi.** In L08 e L09 scrive gerarchie e factory prima di aver elencato cosa cambia e perché. Usa i nomi dei pattern (Factory, Abstract Factory, da Java) come soluzione, senza verificare che corrispondano al problema.
- **Evita ciò che non sa già fare.** Tre esercizi su cinque saltati, rifiutando un tentativo a tempo di 20 minuti con nota sul punto di blocco. Nessuna nota di design, nessuna firma abbozzata.
- **Davanti a un comportamento inatteso incolpa il linguaggio invece di formulare un'ipotesi.** Bug `if "grams" or "food" not in ...` definito "assurdo"; non scompone l'espressione né prova nel REPL di sua iniziativa. Aiuto necessario per leggere traceback, output di pytest, avvisi del type checker.
- **Casi limite ridotti all'input malformato.** Vede file mancante, riga malformata, divisione per zero. Non considera input vuoto, duplicati, iteratore consumato, valori speciali, volumi grandi.
- **Naming per tipo e non per ruolo**, in italiano contro la convenzione (`lista`, `dizionario`, `valore`, `mappa_posizione_food`); nomi di funzione che non descrivono ciò che la funzione fa (`clean_dict`, `food_exist`).
- **Calibrazione asimmetrica.** Accurata sulle aree mai viste (voti 0-1 confermati). Sovrastima le aree che usa ogni giorno: D1 4 contro 1, D4 4 contro 2, B1 3 contro 1. Scambia la familiarità con la sintassi per comprensione.
- **Punto di forza specifico (una sola osservazione, da confermare):** diagnosi strutturale corretta e autonoma quando il problema è riconoscibile: due assi indipendenti in L09, confine tra API e sistema in D1, direzione delle dipendenze in D2. Scrive "non lo so" invece di inventare.
