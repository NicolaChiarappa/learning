# Review — 002 — 2026-10-11

## Esito
Test base: 37/44 (solo completezza; 7 rossi lasciati per scelta) | Test nascosti: 38/63 (`test_hidden.py`) | Indizi usati: 0 sul contenuto (aiuto su ambiente e formato: molto, vedi "Processo")

| Correttezza | Casi limite | Design | Leggibilità | Idiomaticità | Processo |
|---|---|---|---|---|---|
| 3 | 3 | 2 | 3 | 2 | 2 |

In 001 erano tutti 2. L'esercizio non ha codice: la rubrica è applicata come in 001 (correttezza = previsioni contro output; casi limite = dubbi di `design.md` contro ciò che hai sbagliato; design = il modello e gli esperimenti; leggibilità = le spiegazioni; idiomaticità = strumenti, nomi, forma dell'output; processo = `design.md` e rispetto della consegna).

### Previsioni: i numeri
| Misura | 002 | 001 |
|---|---|---|
| Snippet giusti nel contenuto | **4/5** (1, 2, 3, 4) | 5/9 |
| Righe di output giuste nel contenuto | 19/22 | 22/31 |
| Snippet giusti come output esatto (richiesto dal README) | **0/5** | 0/9 |
| Riga di trasferimento | giusta, ed esatta anche nella forma | — |

Nota sullo snippet 1: lo conto giusto, con una riserva sul dato. A un controllo intermedio la previsione aveva 3 righe per 4 `print`; la quarta c'è nel file finale ma non si può stabilire quando è stata aggiunta. Il contenuto è coerente con ciò che avevi scritto in "Righe" (riga 41), quindi non cambio il conteggio.

### Calibrazione
| Sicurezza | Snippet | Giusti |
|---|---|---|
| 5 | 1, 2, 3, 4 | 4 su 4 |
| 3 | 5 | 0 su 1 |

Snippet con dubbi dichiarati: 1. Stima: 4. Ottenuto: 4. **Scarto zero.** È la prima volta che il numero complessivo coincide con i dati: la stima derivata dai campi funziona, tienila. Trasferimento: sicurezza 5, giusto. Il limite è lo stesso di 001: la calibrazione è sul contenuto. Sulla forma hai dichiarato "si" quattro volte su output che non coincidono con la previsione.

## Il punto più importante
**Sai dire cosa fa una riga. Non scrivi chi vede l'oggetto dopo. È la metà del modello che decide l'output, ed è quella che hai liquidato come forma.**

Ti è stato chiesto tre volte di aggiungere "dopo: quali nomi guardano lo stesso oggetto". Hai risposto che lo avevi già scritto "in maniera informale". Ho contato: 26 voci di "Righe", zero con il "dopo". E non è un difetto di impaginazione, perché si vede nei risultati:

- **Snippet 5, ipotesi alternativa (riga 388).** In "Righe" (riga 368) scrivi che `snapshot["name"] += "!"` "costruisce un nuovo oggetto stringa". Giusto. Poi, nell'ipotesi con i riferimenti condivisi, prevedi `"name": "ada!"` dentro `original`. Hai detto cosa fa la riga e non ti sei chiesto chi guarda la stringa nuova. Con quella domanda la risposta era immediata. Conseguenza: delle tue due ipotesi su `dict(original)`, quella giusta porta comunque a un output sbagliato su 3 righe su 4. Nessuna delle due prevedeva l'output reale.
- **Trasferimento (riga 486).** "Questa riga sta riassegnando la label ad una nuova lista". Quale label? A sinistra non c'è un nome, c'è `record["tags"]`. La previsione è giusta, ma la spiegazione non contiene il motivo per cui `row` vede la modifica. Se la riga fosse stata `record = {"tags": record["tags"] + [tag]}`, la tua frase resterebbe identica e l'output cambierebbe. Una spiegazione che non cambia quando cambia l'output non sta spiegando.
- **Snippet 1, riga 39.** "Essendo immutabile crea una nuova tupla". Vero. Ma l'output di `print(ids_alias)` dipende da un'altra cosa: dopo quella riga, `ids` e `ids_alias` guardano ancora lo stesso oggetto? Lo sai (la previsione è giusta), non lo scrivi.

Finché gli snippet hanno nomi nudi e un solo livello, la mezza frase basta: 4/4. Appena compare un contenitore dentro un contenitore (snippet 5) non basta più. Il prossimo esercizio è una matrice, cioè solo contenitori dentro contenitori.

## Casi limite
**Previsti in design.md:** due dubbi, entrambi su righe vere: `log = []` dentro una funzione (snippet 3) e `snapshot = dict(original)` (snippet 5). Rispetto a 001 ("alias, immutabili") è un passo netto: hai indicato in anticipo lo snippet che poi hai sbagliato.

**Mancati:**
- `snapshot["scores"] = [9]` letta come "aggiunge in coda il 9" (riga 369). Non è un `append`: è la stessa forma di `menu["lunch"] = [99]`, che nello snippet 2 (riga 122) hai letto bene, e di `record["tags"] = ...`, che nel trasferimento hai letto bene. Tre righe uguali, una letta diversamente. In 001 era successo con `x = x + [...]` tra lo snippet 2 e il 7.
- `+=` con un indice a sinistra (`snapshot["tags"] += ...`, `snapshot["name"] += ...`): nessun dubbio scritto, e nell'ipotesi alternativa lo sbagli.
- Il dubbio 1 non è un dubbio: scrivi già la risposta giusta ("in teoria... resta com'era"). Un dubbio vero ha due esiti possibili.

**Il dato più importante di questa sezione:** in `design.md` (righe 44-48) sul dubbio 2 avevi scritto l'ipotesi giusta: "comportamento uguale al copy (NON DEEPCOPY)", `original["key"] is new_dict["key"]` torna true. Mezz'ora dopo, in `risposte.md`, scegli l'ipotesi opposta ("copie dei valori") e prevedi `false`. Poco prima, nello scarto del 9 di 001, avevi dimostrato nel REPL che `.copy()` condivide i valori. Avevi l'ipotesi e la prova, e la previsione non le ha usate.

**Cosa avrebbe dovuto farteli vedere:** rileggere `design.md` prima di scegliere tra le due ipotesi. La nota di design non serve a superare un cancello: serve a essere consultata quando arrivi alla riga di cui avevi dubitato. E la sezione "Aggiornamenti a metà lavoro" è vuota, mentre un dubbio nuovo a metà lavoro lo hai avuto (hai chiesto di consultare la documentazione di `dict()`).

## Osservazioni sul codice
Le righe si riferiscono a `risposte.md`, salvo dove indicato.

**1. Snippet 5, scarto (righe 416-441): l'esperimento non può fallire.**
Provi che `second["key1"] is base["key1"]` dà `True`. Lo sapevi già: è la terza riga dell'output che avevi appena incollato. Un esperimento serve quando l'esito può smentirti. Le due righe che hai letto male (`snapshot["name"] += "!"` e `snapshot["scores"] = [9]`) le nomini nella spiegazione e non le provi. La riga "Atteso" (435) non ha il "perché": senza, non si sa quale spiegazione stavi mettendo alla prova. La spiegazione inoltre non dice perché `'y'` compare in `original`. Confronta con lo scarto del 9 di 001, parte su `desserts`: ipotesi, tre output attesi compreso un `KeyError`, poi l'output reale. Quello era il formato. Lo sai fare e qui non l'hai fatto.

**2. Snippet 5, confronto (riga 410): l'unico confronto scritto da te è sbagliato.**
"Le righe sono tutte sbagliate tranne il primo true". La tua previsione è `false`, `false`; l'output è `True`, `False`. La riga giusta è l'ultima, e nella tua previsione non c'è nessun `true`. Stai guardando l'output o la previsione? Il confronto si fa mettendo le due colonne una accanto all'altra, riga per riga. Per gli snippet 1-4 hai dichiarato "si" a voce, chiamandolo "scontato". Per lo snippet 1, nel campo "Output ottenuto" avevi scritto a mano un testo identico alla previsione (virgolette doppie, `"ab"`) al posto dell'output reale: l'ha sostituito l'orchestratore. Un output riscritto a mano coincide sempre con la previsione. Non è una verifica.

**3. "Essendo immutabile" (righe 39, 368; `design.md` riga 7).**
Su `+=` il tipo conta davvero: l'operatore modifica sul posto se l'oggetto lo consente, altrimenti crea un oggetto nuovo e sposta l'etichetta. Quindi la frase non è sbagliata. È incompleta nel punto che ti serve: non dice quale etichetta si sposta. In `design.md` la frase "sono immutabili quindi per forza di cose il `+=` costruisce un nuovo oggetto" sta nella sezione dove non dovevano esserci previsioni, ed era lì prima che scrivessi il modello. È ancora la tua prima mossa. La seconda, ora, è giusta: il modello è scritto come domanda e la tua sintesi (riga 460) nomina l'errore con precisione. Va invertito l'ordine.

**4. Sintesi, regola (riga 467): è una domanda, manca cosa fai con la risposta.**
"La label la stiamo spostando, o stiamo aggiornando l'oggetto che referenzia?" Bene come domanda. Mancano due pezzi che il campo chiedeva: cosa concludi a seconda della risposta, e come riconosci i due casi guardando la riga. Il README dava l'indizio (cosa c'è a sinistra dell'`=`: nome nudo o indice). Nella tua regola `record["tags"] = ...` è "spostare la label": con quella lettura, applicata alla lettera a una funzione, il trasferimento verrebbe `{'tags': ['a']}`. Lo hai previsto giusto nonostante la regola, non grazie a essa.

**5. Forma dell'output: 0/5 dopo 0/9, con le regole scritte nel README.**
Virgolette doppie, niente spazio dopo le virgole, `false` e `true` minuscoli (righe 221, 377-378, 390-391), `"ab"` tra virgolette per una stringa stampata da sola (riga 49). I primi tre sono disattenzione verso una regola scritta, con un esempio, quattro paragrafi sopra. L'ultimo è diverso: una stringa stampata da sola e una stringa dentro una lista si mostrano in due modi, e tu le scrivi uguali (in 001 era `[milk, eggs, tea]` senza apici). Lì manca un pezzo di conoscenza, e l'ho registrato come E006. Perché conta: dal prossimo modulo l'output di un test fallito ti mostra `'5'` contro `5`, e quella differenza è il bug.

**6. Nomi negli esperimenti.**
In inglese, questa volta: `external_log`, `result_log` (design) dicono il ruolo. Restano per tipo o generici `new_dict`, `base`, `second`, `key1`. In `design.md` riga 47 c'è `orignal`: un esperimento con un refuso nel nome non gira. Miglioramento reale rispetto a `dizionario`, `lista`, `Oggetto` di 001; nello scarto del 7 riscritto dopo la review, però, `lista` è tornato.

### Gli scarti riscritti in 001
- **Snippet 7: regge sul meccanismo, non come scarto.** Ora attribuisci la differenza alla riga (`append` sull'oggetto ricevuto contro riassegnazione con `+`) e la provi con `id` prima e dopo: è la correzione che serviva, e lo scope è passato da causa a dettaglio. Tre difetti. (a) Descrivi l'errore al contrario: scrivi di "aver pensato che le due funzioni si comportassero diversamente", ma la tua previsione diceva che si comportavano uguale (`[milk, eggs, tea]` in `shopping`, `True`). (b) La spiegazione vecchia con lo scope è rimasta sopra, non ritirata. (c) Nessuna riga "Atteso" prima di eseguire, `id` stampato in due funzioni su tre, e "`+=` si comporta come append" detto senza il limite (vale per le liste). Non va rifatto.
- **Snippet 9: regge.** Atteso scritto prima, output reale incollato, e il punto su `desserts` trattato con un esperimento che poteva fallire (`KeyError` previsto). Un dettaglio che ti avrebbe morso: dopo `import copy` scrivi `copy = originale.copy()`. Da quella riga in poi il nome `copy` non guarda più il modulo. È il tema di questo modulo, applicato a te.

### Processo
- `design.md`: alla prima consegna il modello era vuoto; scritto dopo il blocco. La forma dei dubbi l'ha sistemata l'orchestratore. Nel file il modello ha una terza domanda sull'alias ("oppure sta creando una seconda etichetta per lo stesso oggetto?"); all'orchestratore risulta che la domanda sull'alias sia rimasta senza risposta. Non so quando è stata aggiunta: se l'hai aggiunta tu dopo, andava detto.
- "Ho finito" con campi vuoti: tre volte. Controllo di completezza mai lanciato da te, output mai incollato. Era la condizione concordata dopo 001. 7 test rossi alla consegna per scelta.
- Tempo: 132 minuti contro 60 stimati (il README diceva di consegnare a 80 con nota di blocco). Hai chiesto velocità saltando i campi, ma i campi saltati non sono dove è andato il tempo: 84 minuti sono passati prima della chiusura delle previsioni.
- Due obiezioni tue alla review di 001 erano fondate e hanno cambiato il formato (dubbi concreti solo dopo aver scorso gli snippet; trascrizione meccanica ammessa). Contestare un requisito con un argomento funziona. Ignorarlo no: sul "dopo:" non hai portato un argomento, hai portato fretta.

## Domande per te
1. Dopo questa riga, quali nomi (o quali posizioni dentro un contenitore) guardano l'oggetto che è appena stato creato o modificato? Se non so elencarli, ho finito di leggere la riga?
2. A sinistra dell'`=` c'è un nome nudo o qualcosa con un indice? Nel secondo caso, quale oggetto sto modificando, e chi altro lo guarda?
3. Il mio esperimento può dare un esito che mi smentisce? Se conosco già la risposta, cosa sto verificando?

## Esito modulo
**PASSATO CON RISERVA**

Passi al prossimo esercizio di M01 ("La griglia condivisa"). Non serve una terza serie di snippet: prevedere l'output su nomi nudi, parametri e contenitori a un livello ora lo sai fare (4/5 con sicurezza calibrata, trasferimento giusto, zero indizi), e un'altra variante uguale misurerebbe solo la tua pazienza.

La riserva:
1. **Il modello è passato per metà.** Prevedi bene; non scrivi chi vede l'oggetto dopo, e sul contenitore annidato sbagli proprio lì. E001 resta aperto. Nel prossimo esercizio quella domanda non è un campo da compilare: è il bug da trovare.
2. **E004 (copia superficiale) è ricaduto**, con l'ipotesi giusta scritta in `design.md` e non usata.
3. **Prima di iniziare il prossimo esercizio**, 10-15 minuti: completa lo scarto dello snippet 5 con un esperimento che può fallire sulle due righe lette male (`snapshot["name"] += "!"` e `snapshot["scores"] = [9]`), ciascuno con la riga "Atteso: ... perché ..." scritta prima, e con l'elenco di chi guarda cosa dopo.
4. **"Consegno" vale solo con l'output dei test incollato da te.** Terza volta che viene chiesto.

M01 resta in corso: questo non era l'esercizio del criterio di uscita. Il criterio (10 snippet nuovi, almeno 8 giusti, senza REPL) verrà valutato sull'output esatto.
