# Pattern di ragionamento

Come Nick affronta i problemi. Lo aggiornano il mentor (principalmente) e l'assessor (dopo ogni test).
Un pattern = un comportamento osservabile e ripetuto, non un giudizio sulla persona.

Ultimo aggiornamento: 2026-10-11 (mentor, dopo python/002). Occorrenze contate: test d'ingresso Python (2026-10-10) + esercizi.
Tre misure (test, 001, 002), ma 001 e 002 sono dello stesso giorno e 002 è una variante di 001: le tendenze "in miglioramento" vanno riconfermate su un esercizio di formato diverso (003) e a distanza (V1).

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

### P01 — Regola memorizzata al posto del modello; lo scarto archiviato come "cosa del linguaggio"
- Descrizione: decide in base a una categoria (il tipo, il contesto) invece di chiedersi cosa fa la riga che sta leggendo. Quando la previsione fallisce attribuisce la causa a un comportamento del linguaggio che non conosceva, quindi il modello non viene corretto. È il lato "processo" dell'errore E001 in `profile/errors.md`.
- Prima osservazione: 2026-10-10 (test d'ingresso: bug `if "grams" or "food" not in ...` definito "assurdo"; "modello mentale assente, lavora per tentativi")
- Occorrenze: 3
- Tendenza: in miglioramento. La seconda metà del pattern (causa attribuita al linguaggio) non è comparsa in 002; la prima (regola sul tipo come prima mossa) sì, ma ora la riconosce.
- Ultima evidenza: python/002 — a favore: modello scritto come domanda in `design.md` e nella sintesi; sintesi: "considero solo la mutabilità di un tipo" (in 001: "non ho fatto errori di ragionamento"); 4/5 nel contenuto, trasferimento giusto. Contro: `design.md` riga 7, "sono immutabili quindi per forza di cose il += costruisce un nuovo oggetto", scritto prima del modello e nella sezione senza previsioni; 26 voci di "Righe" dicono cosa fa la riga e nessuna dice chi guarda l'oggetto dopo; `snapshot["scores"] = [9]` letta come append mentre la stessa forma è letta bene nello snippet 2 e nel trasferimento (in 001: `x = x + [...]` giusta nel 2, sbagliata nel 7). Nello scarto: "ho letto male il codice", non più "non conoscevo".
- Abitudine correttiva: per le righe con un indice o un attributo a sinistra, o che toccano un contenitore dentro un contenitore, scrivere chi guarda l'oggetto dopo. Sui nomi nudi a un livello il requisito è ridondante (4/4 senza). Si considera rientrato quando lo fa senza che lo schema lo imponga.

### P02 — Ipotesi e spiegazioni non portate alle conseguenze; ciò che ha scritto prima non viene riusato
- Descrizione: formula un'ipotesi ma non ne ricava l'output che ne segue; scrive una spiegazione dello scarto e non la mette davvero alla prova. Dal 002: l'informazione giusta è scritta da lui in un punto del lavoro (design, voce di "Righe") e non arriva al punto successivo (previsione, ipotesi alternativa). Gli esperimenti li sa costruire; sotto fretta sceglie quello che non può fallire.
- Prima osservazione: 2026-10-11 (python/001). Nel test d'ingresso non era osservabile.
- Occorrenze: 2
- Tendenza: stabile, forma diversa. Migliorato un pezzo: due ipotesi distinte producono ora due output distinti (snippet 5), che in 001 era il difetto dello snippet 9.
- Ultima evidenza: python/002 — (1) `design.md`, dubbio 2: "comportamento uguale al copy (NON DEEPCOPY)", `is` → true; in `risposte.md` sceglie come previsione l'ipotesi opposta, `false`. (2) Snippet 5: `snapshot["name"] += "!"` descritta come "nuovo oggetto stringa", poi `original["name"]` previsto `"ada!"` nell'ipotesi 2. (3) Scarto del 5: nomina le due righe lette male, l'esperimento prova `second["key1"] is base["key1"]`, il cui esito era già nell'output incollato; "atteso : True" senza perché. (4) "Aggiornamenti a metà lavoro" vuoto, pur avendo avuto un dubbio nuovo (richiesta di consultare la documentazione di `dict()`).
- Controesempi (da ripetere): scarto dello snippet 9 di 001, rifatto tra le due sessioni senza sollecito: atteso scritto prima, nomi in inglese, `KeyError` previsto. Scarto dello snippet 3 di 001 (contrasto `+=` contro `= ... +`). Nota Django di 001. Tutti e tre fuori dalla pressione di fine sessione.
- Stato dell'abitudine "Atteso prima di eseguire" (proposta dopo 001): adottata nella lettera. Scarto del 9: applicata bene e spontaneamente. 002: 1 esperimento su 1 con la riga, 0 su 1 con il "perché", esperimento non falsificabile.
- Abitudine correttiva per 003 (sostituisce "Atteso ... perché ..."): prima di ogni esecuzione due righe, "Se ho ragione: <output>" e "Se ho torto: <output diverso>". Se la seconda non si riesce a scrivere o è uguale alla prima, l'esperimento va cambiato. Verifica: si contano gli esperimenti con le due righe e con output diversi.

### P03 — "Finito" dichiarato senza controllare la consegna; passi di controllo delegati
- Descrizione: la consegna è letta come contesto e non come elenco da spuntare. Dichiara chiuso il lavoro senza verificarlo contro i requisiti e, se può, fa fare ad altri i passi di controllo. Classifica come "forma" sia l'impaginazione sia la verifica.
- Prima osservazione: 2026-10-10 (test d'ingresso: "si ferma ai test verdi", regole scritte non implementate; risposte inserite nei file degli snippet 03, 08, 09)
- Occorrenze: 3
- Tendenza: stabile, non in miglioramento. La regola concordata dopo 001 ("finito" solo con l'output dei test incollato) non ha retto.
- Ultima evidenza: python/002 — tre "ho finito"/"va bene?" con campi vuoti (modello vuoto in `design.md`; risposte prima della verifica; risposte senza confronto e senza sintesi); review chiesta con verifica, scarti e sintesi da fare. Test di completezza mai incollati; lanciati una volta ("perché 2 test non passano?"), poi più. 7 test rossi alla consegna. Risposte dello snippet 2 scritte dentro il blocco di codice (terza volta: test, 001, 002). Dove la verifica l'ha fatta lui è sbagliata: confronto dello snippet 5 ("tutte sbagliate tranne il primo true": la riga giusta è l'ultima); "Output ottenuto" dello snippet 1 riscritto a mano uguale alla previsione. "Dopo:" chiesto tre volte, rifiutato come forma. Output esatto 0/5 dopo 0/9, con le regole nel README.
- Fattori concorrenti da non confondere con il pattern: (a) l'orchestratore ha di nuovo compilato campi su richiesta, quindi la delega ha funzionato; (b) leggere l'output di pytest e passare testo tra terminale e IDE è ancora un attrito reale per Nick (test d'ingresso; "devo gestire terminale e IDE"); (c) alcuni campi erano derivabili meccanicamente ("no" nell'alternativa con sicurezza 4-5).
- Abitudine correttiva: cancello tecnico, non regola da ricordare. Nessuna review senza l'output di pytest incollato da Nick. Un test può restare rosso con una riga "lo lascio rosso perché ...". Gli output si incollano dal terminale, mai riscritti.

### P04 — Giudizio complessivo più favorevole dei dati
- Descrizione: le stime sul singolo elemento sono accurate; il giudizio d'insieme e le affermazioni a posteriori vanno nel verso dell'ottimismo e ignorano i dubbi che lui stesso ha scritto.
- Prima osservazione: 2026-10-10 (test d'ingresso: "calibrazione asimmetrica"; sicurezza 4/5 con 6/19 e 7/14 nei test nascosti)
- Occorrenze: 2 (in 002 non comparso sull'aggregato)
- Tendenza: in miglioramento, una sola misura a favore e ottenuta con la stima derivata dai campi.
- Ultima evidenza: python/002 — 1 snippet con dubbi, stima 4, ottenuto 4: scarto zero (001: dichiarati 7, ottenuti 5). Sicurezza 5 → 4/4; sicurezza 3 → 0/1; trasferimento sicurezza 5 → giusto. Nessuna affermazione a posteriori del tipo "l'avrei fatta giusta". Residuo: quattro "si" dichiarati a voce ("scontato") su output che non coincidono con la previsione nella forma; il "si" sul contenuto era corretto.
- Abitudine correttiva: la stima complessiva si calcola dai voti per elemento. Da verificare se la mantiene quando lo schema non la impone (003: stima dei test nascosti prima della review).

### P05 — Evita ciò che non sa già fare
- Descrizione: davanti a qualcosa che non conosce lascia vuoto o scrive "non so" senza un tentativo.
- Prima osservazione: 2026-10-10 (test d'ingresso: tre esercizi su cinque saltati, tentativo a tempo rifiutato)
- Occorrenze: 2 (in 002 non comparso sulle previsioni)
- Tendenza: in miglioramento.
- Ultima evidenza: python/002 — nessun "non so", ipotesi su tutti gli snippet al primo passaggio. Snippet 5: ha chiesto di consultare la documentazione su `dict(original)`; alla risposta "no, ipotesi + alternativa" ha scritto due ipotesi esplicite con due output. Residuo: modello in `design.md` lasciato vuoto alla prima consegna.
- Abitudine correttiva: regola del tentativo minimo. Da verificare su un formato in cui deve produrre codice (003) e non solo una previsione.

### P06 — Non argomenta il perché
- Descrizione: produce il risultato senza la motivazione, o con una motivazione che si ferma all'etichetta.
- Prima osservazione: 2026-10-10 (test d'ingresso: 10 sezioni "Spiegazione" vuote su 10)
- Occorrenze: 3
- Tendenza: in miglioramento.
- Ultima evidenza: python/002 — 26 voci di "Righe" compilate, con i nomi del codice; sintesi con una regola scritta come domanda. Limiti: la spiegazione dice cosa fa la riga e si ferma lì (trasferimento: "riassegna la label a una nuova lista" non contiene il motivo per cui `row` vede la modifica); la regola finale non dice cosa si conclude a seconda della risposta; "Atteso" senza "perché".

### P07 — Difficoltà e casi limite previsti per categorie generiche
- Descrizione: quando deve prevedere dove sbaglierà elenca categorie larghe, non casi concreti; i dubbi veri emergono durante il lavoro e non vengono riportati nel design.
- Prima osservazione: 2026-10-10 (test d'ingresso: "casi limite ridotti all'input malformato")
- Occorrenze: 2 (in 002 nettamente ridotto)
- Tendenza: in miglioramento. Nota sul dato: la misura di 001 era in parte un artefatto del formato (design richiesto prima di aver visto gli snippet); l'obiezione di Nick era fondata e l'ordine è stato cambiato.
- Ultima evidenza: python/002 — due dubbi su righe vere (`log = []` nella funzione, `snapshot = dict(original)`), il secondo è lo snippet poi sbagliato. Limiti: il dubbio 1 contiene già la risposta (non ha due esiti); nessun dubbio su `contenitore[chiave] += ...`, che è dove sbaglia; il dubbio nato a metà lavoro non è stato scritto in "Aggiornamenti".
- Abitudine correttiva: un dubbio è una riga di codice con due esiti possibili scritti. Da verificare su codice proprio (003: casi limite di una funzione, non di snippet dati).

### P08 — Naming per tipo e in italiano
- Descrizione: nomi che dicono il tipo e non il ruolo, in italiano contro la convenzione del progetto.
- Prima osservazione: 2026-10-10 (test d'ingresso: `lista`, `dizionario`, `valore`, `mappa_posizione_food`)
- Occorrenze: 3
- Tendenza: in miglioramento sulla lingua, stabile sul ruolo.
- Ultima evidenza: python/002 — esperimenti in inglese: `external_log`, `result_log` dicono il ruolo; `new_dict`, `base`, `second`, `key1` no. `lista` tornato nello scarto del 7 riscritto in 001; `copy = originale.copy()` dopo `import copy` nello scarto del 9.

### P09 — Il feedback ricevuto a metà sessione non diventa revisione (a freddo sì)
- Descrizione: un'osservazione ricevuta mentre lavora, soprattutto se ripetuta, viene trattata come interruzione e il testo resta com'è. La stessa osservazione, ricevuta in una review e ripresa a sessione chiusa, viene applicata.
- Prima osservazione: 2026-10-11 (python/001)
- Occorrenze: 2
- Tendenza: mista; pattern riformulato dopo 002.
- Ultima evidenza: python/002 — contro: "dopo:" chiesto tre volte (la terza con la motivazione), mai scritto; "Atteso" senza perché. A favore: scarti del 7 e del 9 di 001 riscritti tra le due sessioni, il 9 bene e di sua iniziativa nel formato richiesto; due obiezioni argomentate alla review di 001. Non determinabile: in `design.md` il modello ha una terza domanda sull'alias che l'orchestratore aveva sollecitato due volte senza risposta in chat; se aggiunta in silenzio è un caso a favore. Da chiedere a Nick.
- Indicazione di processo: una richiesta a metà sessione si fa una volta, con la motivazione subito; se rifiutata si registra e la valuta il reviewer.

### P10 — Il tempo sforato si recupera tagliando la verifica (candidato)
- Descrizione: non guarda il tempo mentre prevede o progetta; quando si accorge dello sforamento chiede velocità e taglia i passi finali (confronto, scarti, sintesi, controllo di completezza), cioè quelli brevi e quelli che correggono il modello. Collegato all'attenzione per l'avanzamento nel percorso.
- Prima osservazione: 2026-10-11 (python/001: 76 minuti di previsioni contro 30-45, chiusura il giorno dopo)
- Occorrenze: 2
- Tendenza: prima misura esplicita in 002.
- Ultima evidenza: python/002 — 84 minuti alla chiusura delle previsioni (stima totale 60; il README diceva di consegnare a 80 con nota di blocco, non usata); 35 minuti per tutto il resto. Richieste di velocità crescenti nella seconda parte ("sistema tu la formattazione", "scrivi tu i no e compila l'orario e facciamo partire la review", "questo è scontato, non farmi perdere altro tempo"). Ha chiesto se la variante lo teneva fermo al primo esercizio di M01 e cosa insegnano i moduli 1-5.
- Abitudine correttiva: punto di controllo del tempo dichiarato nel README; quando si sfora si riduce il numero di elementi, non la verifica di quelli fatti.

## Punti di forza ricorrenti
(Solo se specifici e osservati più volte.)

- **Segnala ciò che non sa invece di inventare, e quei segnali sono affidabili.** Test d'ingresso: voti 0-1 confermati. python/001: sicurezza 3 → 1/4, sicurezza 1 → 0/1. python/002: l'unico snippet con sicurezza 3 è l'unico sbagliato, ed era nei dubbi di `design.md`. Tre osservazioni.
- **Contesta un requisito con un argomento, e l'argomento regge** (python/001 → 002, due obiezioni): "la trascrizione mi ha solo evitato un copia-incolla"; "se non conoscevo gli esercizi come facevo a prevedere quei dubbi?". Entrambe in parte fondate, hanno cambiato il formato di 002 e il dato di P07 è migliorato di conseguenza. Da coltivare: è il canale giusto per la richiesta di velocità. Il rovescio osservato: quando non ha un argomento usa la fretta ("dopo:" in 002).
- **Chiede in modo diretto quando gli manca un pezzo.** 001: "cosa cavolo è il REPL?". 002: "come faccio a prevedere come funziona il + sulle liste?"; richiesta di consultare la documentazione prima dello snippet 5 invece di farlo senza dirlo. Due osservazioni.
- **Rende meglio a piccoli passi ipotesi → verifica, anche da solo e per iscritto se non è sotto pressione.** Nota Django e scarto del 3 in 001; scarto del 9 rifatto tra le sessioni. In 002, a fine sessione, lo stesso formato è degradato (vedi P02, P10).
- **Diagnosi strutturale autonoma su problemi riconoscibili** (una osservazione, test d'ingresso: L09, D1, D2). Non osservabile in 001 e 002; 003 è il primo esercizio in cui può ricomparire.

## Pattern superati
(Spostati qui quando non compaiono per almeno 3 settimane.)

## 2026-10-10 — Test d'ingresso Python (fonte: assessor)

Osservazioni da un solo test: sono candidati a pattern, da confermare sugli esercizi. Il mentor decide se promuoverli in "Pattern attivi" con un ID. Dettagli ed evidenze in `tracks/python/assessment/2026-10-01-ingresso/risultati.md`.

Stato al 2026-10-11 (mentor): promossi in "Pattern attivi" → "si ferma ai test verdi" (P03), "non argomenta il perché" (P06), "evita ciò che non sa già fare" (P05), "incolpa il linguaggio" (P01), "casi limite" (P07), "naming" (P08), "calibrazione asimmetrica" (P04). Resta candidato, non osservabile in python/001 né in python/002: "risponde al design con uno scheletro di classi". Le voci qui sotto restano come testo originale dell'assessor.

- **Si ferma ai test verdi.** In S01 e S02 dichiara sicurezza 4/5 con tutti i test base passati; nei test nascosti 6/19 e 7/14. Regole scritte nella consegna non implementate (formato del messaggio d'errore, timestamp decrescenti, laziness). La consegna è letta come contesto, non come specifica da spuntare.
- **Non argomenta il perché.** Tutte le sezioni "Spiegazione" della lettura codice vuote; domande di design chiuse in 10 minuti su 40; problemi elencati senza ordine né motivazione. Parole sue: "non so spiegare perché prendere certe scelte".
- **Risponde al design con uno scheletro di classi.** In L08 e L09 scrive gerarchie e factory prima di aver elencato cosa cambia e perché. Usa i nomi dei pattern (Factory, Abstract Factory, da Java) come soluzione, senza verificare che corrispondano al problema.
- **Evita ciò che non sa già fare.** Tre esercizi su cinque saltati, rifiutando un tentativo a tempo di 20 minuti con nota sul punto di blocco. Nessuna nota di design, nessuna firma abbozzata.
- **Davanti a un comportamento inatteso incolpa il linguaggio invece di formulare un'ipotesi.** Bug `if "grams" or "food" not in ...` definito "assurdo"; non scompone l'espressione né prova nel REPL di sua iniziativa. Aiuto necessario per leggere traceback, output di pytest, avvisi del type checker.
- **Casi limite ridotti all'input malformato.** Vede file mancante, riga malformata, divisione per zero. Non considera input vuoto, duplicati, iteratore consumato, valori speciali, volumi grandi.
- **Naming per tipo e non per ruolo**, in italiano contro la convenzione (`lista`, `dizionario`, `valore`, `mappa_posizione_food`); nomi di funzione che non descrivono ciò che la funzione fa (`clean_dict`, `food_exist`).
- **Calibrazione asimmetrica.** Accurata sulle aree mai viste (voti 0-1 confermati). Sovrastima le aree che usa ogni giorno: D1 4 contro 1, D4 4 contro 2, B1 3 contro 1. Scambia la familiarità con la sintassi per comprensione.
- **Punto di forza specifico (una sola osservazione, da confermare):** diagnosi strutturale corretta e autonoma quando il problema è riconoscibile: due assi indipendenti in L09, confine tra API e sistema in D1, direzione delle dipendenze in D2. Scrive "non lo so" invece di inventare.
