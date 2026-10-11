# 001 — Prevedi e verifica
Modulo: M01 (Nomi, oggetti, riferimenti) | Difficoltà: 1-2 | Tempo stimato: 30-45 min per 9 snippet (la sfida finale è facoltativa)
Tipo: nuovo

## Teoria essenziale

**Il modello: nome → oggetto.** In Python una variabile non è una scatola che contiene un valore. È un'etichetta (un *nome*) attaccata a un *oggetto* che vive da qualche parte in memoria. Due conseguenze, che userai in ogni riga di questo esercizio:

1. `x = <espressione>` non copia niente: calcola un oggetto (o ne trova uno già esistente) e attacca il nome `x` a quell'oggetto. Se `x` era attaccato a un altro oggetto, l'etichetta si sposta.
2. Un oggetto può avere più etichette. Se tramite una etichetta *cambi l'oggetto stesso*, lo vedi anche dalle altre.

Per ogni riga di codice chiediti: "questa riga **sposta un'etichetta** oppure **modifica un oggetto**?". La maggior parte degli errori di previsione nasce dallo scambiare le due cose.

**Strumenti per guardare.** `id(x)` restituisce un numero che identifica l'oggetto a cui `x` è attaccato (finché l'oggetto esiste). `a is b` chiede "stesso oggetto?" (stesso `id`). `a == b` chiede "stesso valore?". Sono domande diverse: due oggetti distinti possono essere uguali. `is` serve davvero per `x is None`; per tutto il resto, di solito, vuoi `==`. Non usare `is` su numeri o stringhe per "provare" qualcosa: il risultato dipende da ottimizzazioni dell'implementazione. In questo esercizio `is` compare solo su liste e dict.

**Mutabile e immutabile.**
- Immutabili: `int`, `float`, `bool`, `str`, `tuple`, `frozenset`, `bytes`, `None`. Un oggetto immutabile non cambia mai: ogni operazione che sembra "modificarlo" ne produce un altro. I metodi di `str` (`.strip()`, `.upper()`, ...) **restituiscono** una nuova stringa, non toccano la vecchia.
- Mutabili: `list`, `dict`, `set`, e la maggior parte degli oggetti che definisci tu. Alcuni metodi (`.append`, `.sort`, `.update`) cambiano l'oggetto e restituiscono `None`.

**Esempio 1: etichette su oggetti immutabili.**
```python
price = 10
old_price = price      # two labels, same object (the int 10)
price = price + 2      # builds a NEW int 12 and moves the label "price" to it
# old_price still points to the int 10: nothing could have changed it
```

**Esempio 2: un oggetto mutabile con due etichette.**
```python
settings = {"debug": False}
config = settings                 # no copy: the dict now has two labels
config["debug"] = True            # modifies the dict object itself
print(settings)                   # {'debug': True}
print(id(settings) == id(config)) # True
```

**Esempio 3: "sembra una modifica" ma è un nuovo oggetto.**
```python
title = "report"
title.upper()           # builds "REPORT" and throws it away: nobody holds a label on it
print(title)            # report
title = title.upper()   # now the label "title" is moved to the new string
```

Quando usarlo e quando no: il modello nome → oggetto non è una scelta, è come funziona il linguaggio. Ciò che scegli tu è *se vuoi condividere* un oggetto (alias) o *averne uno tuo* (copia). Entrambe sono legittime; l'errore è condividere senza accorgertene.

Documentazione ufficiale (non obbligatoria adesso, utile dopo): Language Reference, "Data model", sezione 3.1 "Objects, values and types"; Tutorial, "Data Structures" (liste). Per visualizzare: pythontutor.com (usalo solo *dopo* aver scritto le previsioni).

## Il problema

Hai 9 snippet brevi nella cartella `snippets/` (`s01.py` ... `s09.py`), in ordine di difficoltà crescente, più uno snippet facoltativo di sfida (`s10_challenge.py`). Per ciascuno devi:

1. **Prevedere per iscritto** l'output esatto, riga per riga, **senza eseguire nulla**.
2. **Spiegare** la previsione con il modello nome → oggetto: per ogni riga rilevante, "sposta un'etichetta" o "modifica un oggetto"? Quali nomi puntano allo stesso oggetto dopo quella riga? Una previsione senza spiegazione non vale: anche se indovini l'output.
3. Dichiarare la **sicurezza** della previsione (1-5).
4. **Solo dopo aver finito tutte le previsioni**: eseguire ogni snippet (`python snippets/s01.py`, o incollandolo nel REPL) e confrontare.
5. Per ogni snippet in cui la previsione era sbagliata (anche solo in una riga): scrivere cosa pensavi, cosa succede davvero, **perché**, e quale prova hai fatto nel REPL per convincertene (per esempio un `print(id(...))`, un `is`, un `print(x)` intermedio).

Tutto va scritto in `risposte.md` (c'è già lo schema da compilare). Non modificare i file in `snippets/` se non per aggiungere `print` di prova *dopo* aver scritto le previsioni.

Alla fine c'è una nota facoltativa di aggancio a Django.

## Vincoli
- Niente esecuzione, niente pythontutor, niente ricerche prima di aver scritto **tutte** le previsioni. Scrivi in `risposte.md` l'ora in cui finisci le previsioni e l'ora in cui inizi a verificare.
- Se non sai prevedere uno snippet, non lasciarlo vuoto: scrivi la tua ipotesi migliore e metti sicurezza 1. Un "non lo so" senza ipotesi non conta come previsione.
- La spiegazione è obbligatoria per ogni snippet, anche quelli che ti sembrano ovvi. Scrivi frasi con i nomi veri del codice ("`backup` e `scores` sono due etichette sullo stesso oggetto").
- Nomi, codice e commenti di prova che aggiungi: in inglese. Le spiegazioni in `risposte.md` in italiano.
- Non usare `is` su numeri o stringhe per verifiche tue: usa liste e dict.

## Prima di scrivere codice
Compila `design.md` (poche righe). Non iniziare le previsioni senza.

## Come lanciare i test
I test **non controllano che le previsioni siano corrette**: controllano che la consegna sia completa (design compilato, previsione e spiegazione presenti per ogni snippet, verifica fatta, scarti motivati). Per la correttezza ci pensa il reviewer.

Dalla cartella dell'esercizio:

```bash
cd /Users/nicolachiarappa/Desktop/Projects/learning/tracks/python/exercises/001-predict-and-verify
/Users/nicolachiarappa/Desktop/Projects/learning/.venv/bin/python -m pytest -q
```

All'inizio falliscono tutti: è normale. Il test sulla fase di verifica può passare solo dopo che hai finito le previsioni.

## Cosa conta come "consegnato"
Consegnato = `design.md` compilato + `risposte.md` con, per gli snippet 1-9, previsione, spiegazione e sicurezza compilate, verifica eseguita e scarti motivati. Lo snippet 10 e la nota Django sono facoltativi.

**Regola del tentativo minimo.** Se ti blocchi, lavora almeno 20 minuti, poi consegna comunque: in `risposte.md`, sezione "Nota di blocco", scrivi lo snippet esatto e il punto esatto in cui non sai andare avanti, e cosa hai provato a ragionare. Una consegna parziale con questa nota è valida e viene valutata. Un esercizio saltato senza tentativo no.

## Consegna
Quando hai finito, scrivi all'orchestratore: "consegno 001".
