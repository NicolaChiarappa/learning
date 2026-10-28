# Verbale — 004 (2026-10-28)

## Cambio di processo, deciso con Nick a metà esercizio
Da "Durante" in poi Nick ha risposto in chat e l'orchestratore ha trascritto fedelmente in `appunti.md`. Motivo dichiarato: velocità ("non dobbiamo abbassare il livello di difficoltà ma aumentare l'agilità al massimo"). Restano di Nick: previsioni (date in chat prima di eseguire), codice, confronti, regola. Annotato in `progress.md`.

## Chiacchierata finale
Domande dell'orchestratore, risposte di Nick riportate parola per parola.

**D1.** `test_items_keep...` passava da solo e falliva nel gruppo sull'originale: quale test lo precedeva e cosa aveva lasciato dentro?
"il problema era legato al fatto che una funzione di test prima popolava già il default e veniva condiviso con la chiamata successiva, mentre da solo non era mai stato toccato da nessuno"
*(Il meccanismo è giusto. Non nomina il test né cosa conteneva il default; l'output del gruppo non è mai stato incollato.)*

**D2.** Con il codice corretto: `mine = []; cart = new_cart("x", items=mine); add_item(cart, "tea", 300); empty_cart(cart)`. Cosa contiene `mine` e quanto vale `cart["items"] is mine`?
"mine alla fine contine (tea,300) e vale false la valutazione con is"
*(Senza esitazioni. È la domanda su indice a sinistra + `=` che fa uscire un oggetto da uno stato condiviso: E001/E004.)*

**D3.** Il rosso di PyCharm mostrava `[] != []` con `Expected: []` e `Actual: []`: perché fallisce?
"perché il confronto era sull'oggetto quindi sul suo id e posizione in memoria non sul contenuto. è quello che controlla is se l'id è uguale, l'istanza è la stessa o meno"

**D4.** Se si corregge solo `items` e si lascia `created_at=time.time()`, quale test diventa rosso?
"test_created_at_is_the_moment_of_creation questo test fallirebbe"

**Domande di "Dopo"** (R1-R7 coperte dai test base, stima dei 12 nascosti): non risposte per scelta di Nick ("delle regole andiamo avanti non ci importa").

## Dove ha esitato o si è corretto
- Correzione: prima `items=list`, poi, dopo la domanda "cosa c'è in `cart["items"]`, che `type`?", `items=list()` ("forse meglio"). Dopo la domanda "quando viene eseguita `list()`? quante liste per tre carrelli?" passa a `None` + lista nuova nel corpo.
- Test di regressione: lo descrive come `carrelo1[1] is carrello2[1]`, ricalcando la tupla del suo esperimento. Dopo la domanda "cosa restituisce la `new_cart` di `cart.py`?" corregge in `cart["items"]`.
- Rosso di `total_cents` attribuito a "il test non legge gli apici". Dopo tre domande (tipo restituito, R6, cosa dicono gli apici): "restituisce una stringa, va corretto il codice". Dato su E006: legge l'apice come un difetto di visualizzazione, non come un'informazione sul tipo.
- Durante il lavoro `test_total_cents_sums_the_prices` in `test_cart.py` è risultato commentato in una lettura dell'orchestratore e ripristinato in quella successiva. Nessuna modifica è rimasta.

## Risposte arrivate dopo un aiuto dell'orchestratore
- B3 (quale riga dentro `add_item` fa trapelare il default) arriva dopo una riformulazione della domanda, poiché Nick non l'aveva capita. Il perché ("+= incrementa la lista sul posto") arriva dopo una seconda richiesta.
- R7: l'orchestratore ha spiegato concretamente quale pezza su `add_item` si intende (`cart["items"] = cart["items"] + [...]`) e ha chiesto come vedere il difetto senza `add_item`. L'idea di confrontare due carrelli appena creati con `is` è di Nick.
- Domanda superflua dell'orchestratore su `==` contro `is` per il test: Nick aveva già usato `is` nell'esperimento di "Prima di iniziare" e lo ha fatto notare.

## Indizi e teoria
- Teoria data due volte prima delle previsioni, su richiesta di Nick: i test pytest girano nello stesso processo e lo stato di un modulo importato (compresi i default) persiste da un test all'altro. Alla seconda richiesta l'orchestratore ha risposto in modo esplicito: "sì, in questo file i test dipendono l'uno dall'altro".
- Livello 1-2: rimando all'esempio `roll` del README per `list()` nel default.
- Livello 1: "cosa restituisce `new_cart` di `cart.py`?" (tupla contro dict nel test).
- Livello 1: tre domande socratiche sul rosso di `total_cents`.

## Processo
- Test base lanciati prima di scrivere la previsione test per test: previsione non disponibile, output del gruppo e del lancio singolo `-k items_keep` mai incollati. È la mancanza di 003 ripetuta.
- Esperimento A fatto solo in parte: "prima" e non "dopo `add_item`". B e C sull'originale hanno previsioni scritte prima, confronto di Nick "tutte giuste". C sul corretto è previsto ("true, false") ma non eseguito.
- Rosso del test di regressione sull'originale incollato, ottenuto chiamando temporaneamente `cart_original.new_cart`. È un `AssertionError` sulla riga dell'`is`: fallisce per la causa giusta. Verde sul corretto incollato. Suite completa: 7 passed (lanciata dall'orchestratore; Nick ha scritto "tutti verdi" senza incollare).
- Previsione della suite completa prima del lancio: giusta sul test (`total_cents`), sbagliata sulla causa.

## Tempi
Non rilevati. L'esercizio è stato creato il 2026-10-16, le prime note sono senza data, il lavoro in chat è del 2026-10-28 (circa un'ora, dalle ~12:30). Tempo di ambiente: poco. Script per gli esperimenti e comando per la cartella temporanea forniti dall'orchestratore.

## Cosa ha sistemato l'orchestratore nella forma
- Tolto da `cart.py` lo script degli esperimenti, che Nick aveva incollato nel file invece che nel terminale. `cart.py` riportato identico all'originale (verificato con `diff`) prima della correzione di Nick.
- Trascritte in `appunti.md` tutte le risposte date in chat, con la nota che sono trascrizioni.
- Non sistemato, segnalato a Nick: docstring di `new_cart` cancellata nella correzione e non ripristinata. File `raw_next_data.json` estraneo, non tracciato, nella cartella.
