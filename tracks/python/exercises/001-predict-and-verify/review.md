# Review — 001 — 2026-10-11

## Esito
Test base: 38/38 (solo completezza) | Test nascosti: 47/68 | Indizi usati: 2 (livello 1 e 2, entrambi sulla nota Django facoltativa; 0 sugli snippet 1-9)

| Correttezza | Casi limite | Design | Leggibilità | Idiomaticità | Processo |
|---|---|---|---|---|---|
| 2 | 2 | 2 | 2 | 2 | 2 |

L'esercizio non ha codice: la rubrica è applicata così.
- **Correttezza** = previsioni contro output reale: 5/9 snippet giusti, 4 sbagliati (3, 5, 7, 9).
- **Casi limite** = "casi che temo di sbagliare" in `design.md` contro gli snippet sbagliati davvero.
- **Design** = il modello con cui ragioni e gli esperimenti che costruisci per metterlo alla prova.
- **Leggibilità** = le spiegazioni scritte.
- **Idiomaticità** = uso degli strumenti del linguaggio (`is`, `id()`, REPL) e nomi.
- **Processo** = `design.md` e rispetto della consegna.

### Previsioni: i numeri
| Misura | Risultato |
|---|---|
| Snippet giusti, ignorando la forma (spazi, apici, maiuscole) | **5/9** (1, 2, 4, 6, 8) |
| Snippet giusti alla lettera ("output esatto", come chiede il README) | **0/9** |
| Righe di output giuste, ignorando la forma | 22/31 |
| Snippet 10 (facoltativo) | incompleto: 3 righe giuste, 2 lasciate con `?` |

Le differenze di sola forma sono state contate come giuste: è corretto per misurare il concetto, e lo confermo. Ma sappi che nessuna delle tue previsioni è l'output esatto (vedi osservazione 6).

### Calibrazione
- **Dichiarato 7/9, ottenuto 5/9.** Scarto di 2, nel verso dell'ottimismo.
- **Sicurezza per snippet contro esito** (scala 1-5; la conversione dai tuoi voti su 10 l'ha fatta l'orchestratore):

| Sicurezza | Snippet | Giusti |
|---|---|---|
| 5 | 1, 4, 6, 8 | 4 su 4 |
| 3 | 2, 3, 5, 7 | 1 su 4 |
| 1 | 9 | 0 su 1 |

I voti per snippet erano buoni: dove hai messo sicurezza alta hai avuto ragione, dove hai messo sicurezza media o bassa hai sbagliato quasi sempre. Il numero sbagliato è quello complessivo. Hai detto "i primi 7 penso di averli azzeccati tutti" dopo aver scritto "non so" nella spiegazione di 2, 3, 5 e 7: su quei quattro ne hai presi uno. Regola pratica che esce dai tuoi stessi dati: se nella spiegazione c'è scritto "non so", nel conteggio quello snippet vale come sbagliato.

Due cose da leggere con prudenza. Il 5/9 è sopra l'attesa per un primo esercizio (il test d'ingresso dava 0 snippet previsti), e il tempo tra fine previsioni e verifica (4 minuti), gli errori e la sicurezza bassa dove sbagli dicono che le previsioni sono autentiche. Però lo snippet 2 è arrivato dopo due solleciti e dopo la domanda "modifica l'oggetto esistente o ne crea uno nuovo? `+` e `+=` devono comportarsi uguale?": non è contata come indizio, ma l'alternativa giusta te l'ha messa sul tavolo quella domanda.

## Il punto più importante
**Ragioni con una regola sul tipo ("è mutabile o immutabile?") invece che con una domanda sulla riga ("questa riga sposta un'etichetta o modifica un oggetto?"). La regola sul tipo ti dà la risposta giusta solo quando l'oggetto è immutabile.**

La prova è nei tuoi risultati, non in una mia opinione:
- gli snippet dove il tipo decide da solo (stringhe nel 4, int nell'8) li hai presi tutti, con sicurezza 5;
- i quattro sbagliati (3, 5, 7, 9) riguardano tutti oggetti mutabili. Lì sapere che "la lista è mutabile" non dice niente: una lista *può* essere modificata, ma la riga che stai leggendo la modifica oppure no? `backup += [10]`, `{"first": morning}`, `items = items + [item]`, `menu.copy()`: quattro righe, quattro volte la stessa domanda senza risposta.

In `design.md` hai scritto in anticipo che temevi le "operazioni sugli immutabili": non ne hai sbagliata una. Hai sbagliato dove non guardavi.

Il README lo diceva nella teoria ("Per ogni riga chiediti: sposta un'etichetta oppure modifica un oggetto?") e l'orchestratore te lo aveva segnalato sulla nota di design prima che iniziassi. La nota è rimasta com'era. Finché il modello resta quello, ogni comportamento nuovo ti sembrerà "una cosa del linguaggio che non conoscevo" (lo scrivi nella sintesi) invece di una conseguenza che potevi ricavare.

## Casi limite
**Previsti in design.md:** "perdere il filo sulle assegnazioni, alias, e operazioni sugli immutabili". Tre categorie larghe, nessun caso concreto.

**Mancati:**
- `+=` su una lista si comporta diversamente da `+` (snippet 3);
- un contenitore tiene un riferimento, non una copia (snippet 5, e di nuovo nel 9);
- riassegnare un parametro dentro una funzione non tocca il chiamante (snippet 7);
- una copia superficiale condivide gli oggetti interni (snippet 9).

**Cosa avrebbe dovuto farteli vedere:** la teoria del README conteneva già le due domande che servivano. "`x = <espressione>` non copia niente" vale anche quando il lato sinistro è `history["first"]` o un parametro. Un "caso temuto" utile non è una categoria ("alias"), è una riga di codice di cui non sai rispondere: "non so se mettere una lista in un dict la copia", "non so se `+=` fa la stessa cosa di `= ... +`". Tre di questi quattro dubbi li avevi davvero, e li hai scritti nelle spiegazioni dopo: andavano in `design.md` prima, insieme all'esperimento per scioglierli.

## Osservazioni sul codice
Le righe si riferiscono a `risposte.md`.

**1. Snippet 7, analisi dello scarto (righe 189-197): la spiegazione non spiega, e il tuo esperimento la smentisce.**
Scrivi che `items` "è una variabile che vive esclusivamente nello scope della funzione". Ma `items` è locale anche in `add_item`, e lì il chiamante la modifica la vede: l'hai previsto giusto tu stesso (riga 180). Lo scope quindi non può essere la differenza tra le due funzioni. Subito dopo scrivi una terza versione con `items += [item]` e ottieni `True`: anche lì `items` è locale. Hai tre funzioni con lo stesso identico scope e due comportamenti diversi, e la tua spiegazione le tratta tutte allo stesso modo. Direzione: metti le tre funzioni una accanto all'altra e per la sola riga che cambia rispondi alla domanda del README. Poi verifica con un `print(id(items))` prima e dopo quella riga, in tutte e tre. Questo scarto va riscritto.

**2. Snippet 8, riga 210: output giusto, sicurezza 5, motivazione incompleta.**
"`visits` resta 5 perché l'int è immutabile". L'immutabilità spiega perché `counter += 1` non può modificare l'oggetto 5, ma non dice cosa succede al nome `counter`, né perché `visits` non lo segue. Confrontala con quello che avevi scritto per lo snippet 7 (riga 182): "il risultato non cambia perché nella funzione il puntatore in ingresso viene riassegnato". Se riassegnare il parametro si vedesse nel chiamante, `visits` diventerebbe 6. Hai usato due regole opposte per lo stesso gesto (riassegnare un parametro), scegliendole in base al tipo. Lo snippet 8 è giusto, ma non conta come prova che il passaggio di argomenti ti sia chiaro. La seconda metà della spiegazione (riga 211, "gli int dentro la lista sono altri oggetti ma la lista stessa è ancora puntata da `daily_visits`") è invece il modello giusto: quella frase è il livello a cui devono arrivare le altre.

**3. Snippet 5 e 9 (righe 131, 233, 240-243): lo stesso errore due volte, e nel 9 un'ipotesi che non produce conseguenze.**
Nel 5 dichiari che `backup = scores` condivide l'oggetto (snippet 1) ma che `{"first": morning}` lo copia: stesso meccanismo, due risposte. Nel 9 l'ipotesi è "`copy` copia solo la struttura, `deepcopy` anche i valori", ma poi prevedi lo stesso output per le due copie (`false` e `false`). Un'ipotesi che distingue due cose deve produrre due previsioni diverse: se non lo fa, non l'hai usata. Presa alla lettera, la tua ipotesi portava alla risposta giusta. Lo scarto del 9 inoltre: dice "usando il repl ho capito" senza incollare nulla (l'unico dei quattro senza prova); non spiega perché `desserts` non compare in `menu` mentre `salad` sì, che è il punto fine dello snippet; e scrive "si aggiorna *anche* la lista sul dizionario originale", come se le liste fossero due. Quante sono?

**4. Snippet 3, analisi dello scarto (righe 67-83), e la frase sullo snippet 10 (riga 268).**
Questo è lo scarto fatto meglio, e va ripetuto così: nella stessa sessione fai `+=`, controlli con `is`, poi fai `= ... +` sullo stesso oggetto e controlli di nuovo. È un esperimento di contrasto, non una conferma. Il limite: la regola che ne ricavi si ferma alle liste e non l'hai messa alla prova altrove. La riga 268 ("l'avrei fatta corretta, lo si deduce dalle risposte precedenti") l'ho verificata: con la regola che avevi prima della verifica (`+=` costruisce un oggetto nuovo) le ultime due righe verrebbero `TypeError again` e `([1, 9], 2)`; con quella di dopo (`+=` modifica sul posto) verrebbe solo `([1, 9, 5], 2)`. L'output reale è `TypeError again` e `([1, 9, 5], 2)`: nessuna delle due. Una previsione che non hai scritto prima di vedere l'output non esiste, e questa in particolare non si deduceva. Lo snippet è facoltativo e non pesa sul punteggio; la frase sì, perché è lo stesso riflesso del "7 su 9".

**5. Sintesi finale (riga 274): metà vera, e manca la risposta alla seconda domanda.**
"Non ho fatto errori di ragionamento, non conoscevo alcuni comportamenti". Vale per il 3 e per il 9: cosa fa `+=` su una lista e cosa fa `.copy()` non si ricavano, si sanno o si provano. Non vale per il 5 e per il 7. Nel 7 la riga è `items = items + [item]`: la stessa forma di `backup = backup + [10]`, che nello snippet 2 avevi previsto giusta (riga 42). Sapevi cosa fa quella riga e hai cambiato risposta solo perché era dentro una funzione. Quello è ragionamento, non conoscenza. La domanda "c'è una regola che adesso applicheresti a una riga mai vista?" è rimasta senza risposta: era la riga più importante dell'intera consegna.

**6. Forma dell'output, nomi, strumenti.**
- Output esatto 0/9: liste senza spazi (`[7,9,4,10]`), `false` minuscolo (righe 56, 228-229), `True, False` con la virgola (riga 151: cosa mette `print` tra due argomenti?), apici doppi dove Python stampa i singoli, `[milk, eggs, tea]` senza apici (righe 174-175). Singolarmente sono dettagli; insieme dicono che non hai ancora in testa come Python mostra un valore. Quando leggerai un traceback o un test fallito, quella forma è l'informazione.
- Nomi nei tuoi esperimenti (righe 140, 278-298): `dizionario`, `lista`, `Oggetto`, `costruisci`, `oggetto1`. In italiano e per tipo: due violazioni della stessa regola (metodo, punto 10), già segnalata nel test d'ingresso. Vale anche nel REPL: è lì che si formano le abitudini.
- `id()` mai usato, pur essendo previsto in `design.md`. Nello snippet 5 dimostri la condivisione modificando e ristampando (righe 140-145): funziona, ma `is` risponde alla domanda direttamente.

**Nota Django (facoltativa, fuori punteggio).** L'ipotesi scritta è nella direzione giusta ma vaga: "altre label" di chi? L'esperimento usa `def costruisci(lista=[])`, cioè uno strumento di cui non conoscevi il comportamento, per verificare un'ipotesi su quello stesso comportamento: ha funzionato, ma non potevi sapere in anticipo cosa stavi misurando. La chiusura invece è scritta bene ("credevo ne venisse costruito uno ogni volta", cioè cosa pensavi e cosa hai visto): è il formato che devono avere tutti gli scarti. Manca la seconda metà della domanda: la versione con il callable non l'hai provata, quindi non sai ancora perché `default=list` risolve.

### Processo
- `design.md`: modello descritto come regola sul tipo, casi temuti generici, uso del REPL ridotto a un elenco di strumenti. Dopo la segnalazione dell'orchestratore hai aggiunto due parole ("probabilmente id()"). Superficiale.
- Cinque previsioni lasciate a "non so" alla prima stesura, contro una regola scritta due volte nel README; lo snippet 10 è rimasto così.
- Previsioni scritte come commenti nei file `snippets/` invece che in `risposte.md`, poi fatte trascrivere. Il confronto tra output e previsione, cioè il passo 4 dell'esercizio, l'ha compilato l'orchestratore, come la sicurezza. Hai dichiarato due volte "credo di aver finito" con campi obbligatori vuoti.
- Tempo: 76 minuti per le sole previsioni contro una stima di 30-45, chiusura il giorno dopo.

Il confronto riga per riga tra quello che avevi scritto e quello che è uscito è il momento in cui l'esercizio insegna. Se lo fa un altro, ricevi un si/no e perdi il resto.

## Domande per te
1. Prima di prevedere una riga: so dire quale oggetto esisteva prima, se dopo la riga è lo stesso oggetto cambiato oppure un oggetto nuovo, e quali nomi lo guardano? Se a una di queste tre non so rispondere, quale esperimento di due righe me lo dice?
2. La mia regola su `+=` l'ho provata su una lista. Su una tupla o una stringa darebbe lo stesso risultato? Lo so o lo sto supponendo?
3. La mia ipotesi fa cambiare almeno una riga della previsione? Se due ipotesi diverse mi danno lo stesso output, quale delle due sto usando davvero?

## Esito modulo
**DA RIFARE (con variante breve)**

Non per il 5/9, che per un primo esercizio è sopra l'attesa. Per tre motivi:
1. l'analisi degli scarti doveva correggere il modello, e su due meccanismi su quattro non l'ha fatto: lo scarto del 7 è sbagliato, quello del 9 è senza prova e ignora metà dello snippet;
2. la sintesi non contiene nessuna regola riutilizzabile;
3. il confronto e parte della compilazione non li hai fatti tu.

Variante proposta: 6 snippet nuovi, 20-30 minuti, solo sui quattro meccanismi mancati (più `+=` su un tipo immutabile). Condizioni: `design.md` riscritto con il modello nome → oggetto e con i dubbi concreti; ogni riga spiegata con "sposta un'etichetta" o "modifica un oggetto"; `risposte.md` compilato da te, confronto compreso; nomi in inglese anche nel REPL. Prima della variante: riscrivi lo scarto dello snippet 7 e aggiungi la prova a quello del 9.

Il modulo M01 resta in corso: questo non era l'esercizio del criterio di uscita.
