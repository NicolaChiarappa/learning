# Test d'ingresso — Python — 2026-10-01

Questo test serve a capire dove sei davvero, non a darti un voto. Una risposta "non lo so" è più utile di una inventata: ti costruisco la roadmap su quello che scrivi qui. Se tiri a indovinare la roadmap verrà sbagliata.

## Regole
- **Niente IA**: niente ChatGPT, Copilot, Claude né autocompletamento IA nell'editor. Disattivalo prima di cominciare.
- **Niente copia-incolla dal web**, niente Stack Overflow, niente ricerche su Google.
- **Documentazione ufficiale** (docs.python.org) ammessa **solo nella parte 4 (scrittura codice)**. Nelle parti 1, 2, 3 e 5 non è ammessa.
- **Parte 3**: niente esecuzione degli snippet. Devi prevedere l'output a mente. Se poi vuoi verificare, fallo **dopo** aver scritto e salvato la risposta, e non correggerla.
- **Non aprire la cartella `_assessor/`.** Contiene i test sui casi limite che userò per la valutazione. Se la apri, il test non misura più niente.
- Non modificare i file di test `test_*.py` dentro `04-scrittura-codice/`.

## Ordine e tempi indicativi

| # | Parte | Dove rispondi | Tempo indicativo |
|---|---|---|---|
| 1 | Autovalutazione | `01-autovalutazione.md` | 10 min |
| 2 | Concetti (20 domande) | `02-concetti.md`, sotto ogni `**Risposta:**` | 60 min |
| 3 | Lettura codice (10 snippet) | `03-lettura-codice/risposte.md` | 60 min |
| 4 | Scrittura codice (5 esercizi) | file `.py` in ogni sottocartella di `04-scrittura-codice/` | 3 h - 3 h 30 |
| 5 | Design (2 domande) | `05-design.md` | 40 min |

Totale: **circa 6 ore**. Dividilo in due sessioni: **sessione A** con le parti 1, 2 e 3 (circa 2 h 10); **sessione B** con le parti 4 e 5 (circa 4 h). Fai l'autovalutazione **per prima**, prima di vedere le domande, e poi non tornarci sopra.

I tempi sono indicativi. Superarli non è un problema, basta che lo annoti. Se una domanda ti blocca per più di 5 minuti scrivi cosa sai, passa oltre e torna dopo.

## Annotazioni obbligatorie per ogni parte
Alla fine delle parti 2, 3 e 5 compila la riga già presente in fondo al file:

```
Tempo impiegato: __ min | Sicurezza (1-5): __
```

Per la parte 4 compila la tabella in `04-scrittura-codice/tempi.md`, una riga per esercizio.

Sicurezza: 1 = ho tirato a indovinare, 3 = abbastanza sicuro, 5 = certo.

## Ambiente per la parte 4

Ti serve Python **3.11 o superiore** (sul Mac hai 3.14). Da terminale, nella cartella del test:

```bash
cd /Users/nicolachiarappa/Desktop/Projects/learning/tracks/python/assessment/2026-10-01-ingresso
python3 -m venv .venv
source .venv/bin/activate
pip install pytest
```

Esegui i test base dalla stessa cartella:

```bash
# tutti gli esercizi
pytest
# un esercizio solo
pytest 04-scrittura-codice/03-ttl-cache
# output dettagliato
pytest -v 04-scrittura-codice/05-meal-import
```

Il `pytest.ini` nella cartella del test limita la raccolta a `04-scrittura-codice/`. **Non lanciare pytest su `_assessor/`.**

Per ogni esercizio:
- leggi il `README.md` della sottocartella;
- scrivi la soluzione nel file scheletro indicato. Puoi aggiungere funzioni, classi e moduli, ma **non cambiare le firme pubbliche** richieste;
- i test base controllano solo il caso normale. **Superarli non vuol dire aver finito.** Io userò altri test sui casi limite descritti nel README. Leggilo con attenzione e, se vuoi, aggiungi test tuoi in un file `test_mine_*.py`;
- puoi usare solo la libreria standard (niente pacchetti esterni oltre a pytest).

L'esercizio 05 chiede anche una breve nota di design (`NOTE.md`) da scrivere **prima** del codice.

## Consegna
Quando hai finito, salva tutto e avvisa l'orchestratore ("test d'ingresso python finito"). Non serve fare commit; se lo fai, escludi `.venv/` (c'è già un `.gitignore`).
