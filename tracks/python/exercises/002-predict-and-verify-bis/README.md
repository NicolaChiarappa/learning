# 002 — Prevedi e verifica, bis
Modulo: M01 (Nomi, oggetti, riferimenti) | Difficoltà: 2 | Tempo stimato: circa 60 minuti (5 snippet; se arrivi a 80 consegna con la nota di blocco)
Tipo: ripasso (E001, E002, E003, E004, E005 di `profile/errors.md`)

Questa è la variante breve di 001. Gli snippet sono nuovi e riguardano solo i meccanismi che in 001 sono rimasti sbagliati. Cambia anche l'ordine del lavoro e cambia chi fa cosa: **tutto in `risposte.md`, tutto scritto da te**, confronto compreso.

## Teoria essenziale

La teoria ampia (nome → oggetto, `id`, `is`, `==`) è nel README di 001: se ti serve, rileggila. Qui solo il richiamo e ciò che serve per questi snippet.

**La domanda, riga per riga.** Per ogni riga che leggi: *questa riga sposta un'etichetta o modifica un oggetto? E dopo, quali nomi guardano lo stesso oggetto?* Non ti chiedere "di che tipo è?": ti chiedi cosa fa **quella riga**. Lo stesso tipo di dato può subire righe di entrambe le specie.

**Due indizi per leggere una riga.**
- Guarda cosa c'è a sinistra di un `=`. Un nome nudo (`x = ...`) è un'etichetta che si sposta. Qualcosa con un indice o un punto (`x[...] = ...`, `x.attr = ...`) agisce sull'oggetto a cui `x` è attaccato, e non sposta `x`.
- Quando chiami `f(a)`, prima della prima riga del corpo avviene l'equivalente di `parametro = a`. Il parametro è un nome che appartiene alla funzione.

Esempio minimo (non è uno degli snippet):
```python
stock = {"apples": 3}
shelf = stock                   # one dict, two labels
shelf = {"apples": 5}           # name on the left: the label "shelf" moves to a new dict
shelf["pears"] = 1              # index on the left: modifies the dict "shelf" points to now
print(stock)                    # {'apples': 3}
```

**`+=`.** Compare in più snippet. Non dare per scontato cosa faccia: è uno dei punti da scoprire. Dopo aver verificato, leggi Language Reference, "Augmented assignment statements".

**Quando usare l'alias e quando la copia** non è oggetto di questo esercizio: qui si impara solo a prevedere cosa succede. Documentazione utile dopo: Library Reference, modulo `copy`.

## Il problema

Hai 5 snippet in `snippets/` (`s01.py` ... `s05.py`), già riportati dentro `risposte.md`, più una "riga nuova" per la sintesi finale (`snippets/transfer.py`, anch'essa già in `risposte.md`). Per ogni snippet devi prevedere l'output esatto, spiegarlo riga per riga con la domanda del modello, dichiarare la sicurezza, poi verificare, confrontare e, se sbagli, fare uno scarto strutturato.

### Ordine di lavoro (rispettalo, i test non lo vedono ma il reviewer sì)
1. **Teoria**: leggi la sezione qui sopra.
2. **Scorri tutti gli snippet senza prevedere**: serve solo a vedere quali operazioni compaiono. Non scrivere previsioni, non eseguire.
3. **Compila `design.md`**: operazioni che hai visto, il modello come domanda sulla riga, almeno due dubbi concreti (ciascuno una riga di codice con l'esperimento che lo scioglierebbe). Senza `design.md` non si procede.
4. **Previsioni**, snippet per snippet, in `risposte.md`: sezione `Righe` (una voce per riga significativa, nella forma "sposta un'etichetta / modifica un oggetto (quale); dopo: quali nomi guardano lo stesso oggetto"), `Previsione`, `Sicurezza`. Con sicurezza 3 o meno, `Ipotesi alternativa e output che produrrebbe` è obbligatoria: due ipotesi diverse devono dare due output diversi.
5. **Chiusura delle previsioni**: sezione `Chiusura delle previsioni`, i due campi derivati, e l'ora in testa al file. Da qui non si cambia più nessuna previsione.
6. **Verifica e confronto, fatti da te**: esegui (`python snippets/s01.py`, ...), incolla `Output ottenuto`, scrivi quali righe differiscono, scrivi `si`/`no`.
7. **Scarti** per ogni `no`, nei campi, nell'ordine: spiegazione → esperimento → **Atteso (scritto prima di eseguire)** → ottenuto → la spiegazione regge? Se non regge: nuova spiegazione con il suo esperimento.
8. **Sintesi e prova di trasferimento**: la tua regola, poi la riga nuova (previsione, poi verifica).

`design.md` si può e si deve aggiornare: se a metà lavoro ti nasce un dubbio nuovo, scrivilo in "Aggiornamenti a metà lavoro" (riga di codice + esperimento) **prima** di proseguire.

### Output esatto
L'output va scritto carattere per carattere come lo stampa Python. In 001 nessuna risposta era esatta per sola forma: qui conta. Regole di forma:
- una riga per `print`;
- liste con virgola e spazio, stringhe tra apici singoli dentro i contenitori; tuple tra parentesi tonde; dict con `{'chiave': valore}`;
- una stringa stampata da sola non ha apici;
- `True` e `False` con la maiuscola.

Esempio di sola forma, che non c'entra con gli snippet:
```python
print({"k": [1.5, None]}, "ok", True)     # prints one line:  {'k': [1.5, None]} ok True
```
Se per te una riga solleverebbe un errore, scrivi il nome dell'eccezione al posto dell'output.

## Vincoli
- Niente esecuzione, niente pythontutor, niente ricerche prima di aver chiuso **tutte** le previsioni (passo 5).
- Niente esecuzione, né degli snippet né nel REPL, senza una riga `Atteso: <output esatto> perché <la spiegazione che stai mettendo alla prova>` scritta prima in `risposte.md`. Vale per gli esperimenti degli scarti e per ogni prova extra: si conta.
- Se non sai prevedere uno snippet, scrivi la tua ipotesi migliore con sicurezza 1. Un "non so" senza ipotesi non conta.
- Una voce `Righe` con un "non so" fa contare lo snippet tra quelli "con dubbi" nella chiusura. È voluto.
- Nomi, codice e commenti di prova che aggiungi (anche nel REPL, anche usa e getta): in inglese e **per ruolo, non per tipo** (`pending_orders`, non `lista`; `session`, non `dizionario`). Le spiegazioni in italiano.
- Non modificare i file in `snippets/` né il codice riportato in `risposte.md`: un test lo confronta.
- Non usare `is` su numeri o stringhe per prove tue: usa liste e dict.

## Prima di scrivere codice
Compila `design.md` (passo 3). Non iniziare le previsioni senza. I test controllano la forma: modello scritto come domanda, almeno due dubbi con riga di codice ed esperimento.

## Come lanciare i test
I test non controllano che le previsioni siano giuste: controllano che la consegna sia completa (design compilato, tutti i campi, scarti strutturati con la riga "Atteso", conti derivati coerenti). Per la correttezza ci pensa il reviewer.

```bash
cd /Users/nicolachiarappa/Desktop/Projects/learning/tracks/python/exercises/002-predict-and-verify-bis
/Users/nicolachiarappa/Desktop/Projects/learning/.venv/bin/python -m pytest -q test_delivery.py
```

All'inizio falliscono quasi tutti: è normale. Lanciali anche a metà lavoro per vedere cosa manca; i campi dopo la verifica passano solo dopo che li hai compilati.

## Cosa conta come "consegnato"
Consegnato = `design.md` e `risposte.md` compilati da te e `pytest -q test_delivery.py` incollato nel messaggio di consegna. **Senza l'output dei test incollato, "finito" non vale.**

**Regola del tentativo minimo.** Se ti blocchi, lavora almeno 20 minuti, poi consegna comunque: in `risposte.md`, "Nota di blocco", scrivi lo snippet esatto, il punto esatto in cui non sai andare avanti e cosa hai provato. Una consegna parziale con questa nota è valida e viene valutata. Un esercizio saltato senza tentativo no.

## Consegna
Quando hai finito, lancia `pytest -q test_delivery.py` e incolla l'output all'orchestratore insieme alla frase: "consegno 002".
