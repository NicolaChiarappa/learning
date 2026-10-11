# Mentor — 002

Data: 2026-10-11. Il contenuto tecnico è in `review.md`: qui c'è solo come hai lavorato.

## Cosa ho visto nel tuo ragionamento

- **Quello che scrivi prima non arriva a quello che scrivi dopo.** Tre casi, stessa forma. (1) `design.md`, dubbio 2: "comportamento uguale al copy (NON DEEPCOPY)", `is` → true. Mezz'ora dopo, snippet 5, scegli come previsione l'ipotesi opposta e metti `false`. (2) Snippet 5, "Righe": `snapshot["name"] += "!"` "costruisce un nuovo oggetto stringa". Poche righe sotto, nell'ipotesi 2, `original` ha `"ada!"`. (3) Scarto: nomini le due righe lette male e l'esperimento ne prova una terza, di cui avevi già l'output davanti. In tutti e tre i casi l'informazione giusta l'avevi scritta tu. Non l'hai riletta.
- **La fretta è arrivata dopo che il tempo era già andato, e ha tagliato il pezzo sbagliato.** 84 minuti per le previsioni (stima totale: 60; il README diceva di consegnare a 80 con la nota di blocco). Poi 35 minuti per verifica, scarto, sintesi e trasferimento, con tre "ho finito" a campi vuoti. Hai tagliato il confronto, che costa cinque minuti. E dove l'hai fatto da solo è venuto sbagliato: allo snippet 5 scrivi "tutte sbagliate tranne il primo true", ma la riga giusta è l'ultima e nella tua previsione non c'è nessun `true`; allo snippet 1 l'"output ottenuto" era la tua previsione riscritta a mano. Questo dice che il confronto non è una formalità che sai già fare: è un passaggio in cui sbagli.
- **Chiami "forma" tre cose diverse.** L'impaginazione del file (forma vera: può sistemarla chiunque). L'output esatto (regola dell'esercizio; da 003 la giudica pytest, non una discussione). Il "dopo: chi guarda l'oggetto" e il confronto (contenuto: è lì che hai perso lo snippet 5). Sul "dopo:" avevi un argomento a disposizione e non l'hai usato: sugli snippet 1-4, nomi nudi a un livello, hai fatto 4/4 senza scriverlo, quindi 26 voci erano più del necessario. Detto così, il requisito si restringeva alle righe con un indice a sinistra o un contenitore dentro un contenitore. Hai detto "cazzate di forma" ed è rimasto tutto com'era, errore compreso.
- **Dove hai lavorato meglio: lo scarto del 9 di 001, rifatto tra le due sessioni.** Atteso scritto prima, nomi in inglese, un `KeyError` previsto: un esperimento che poteva smentirti. Nessuno te lo stava chiedendo in quel momento e non avevi fretta. Lo sai fare. In 002, sotto pressione, lo stesso campo è diventato "atteso : True" su una cosa che sapevi già.
- **Due ipotesi con due output diversi, al primo passaggio.** Snippet 5: ti è stato detto "niente documentazione, ipotesi più alternativa" e le hai scritte tutte e due. È la risposta alla tua domanda "come faccio a prevedere come funziona il `+` sulle liste?": non lo prevedi perché lo sai, ti impegni su un'ipotesi così l'output può darti torto. In 001 su quei casi c'era "non so".

## Il pattern

Confronto con 001 e con il test d'ingresso. Tre misure: le tendenze cominciano a valere qualcosa.

**Confermati**
- *Ipotesi e spiegazioni non portate alle conseguenze* (seconda volta, forma diversa). In 001 l'ipotesi giusta sul `copy` non cambiava la previsione; qui l'ipotesi giusta stava in `design.md` e la previsione ha preso l'altra. In 001 l'esperimento smentiva la spiegazione senza che te ne accorgessi; qui l'esperimento è scelto in modo da non poter smentire niente. La riga "Atteso" l'hai adottata nella lettera (c'è) e non nella funzione (manca il "perché", e l'esito era noto).
- *"Finito" senza controllo, verifica fatta da altri* (terza volta: test d'ingresso, 001, 002). Tre "ho finito" con campi vuoti, test di completezza mai incollati, risposte dentro il blocco di codice per la terza volta. Non migliora. Novità di questa misura: ora si vede cosa costa. L'unico errore dell'esercizio e l'unico confronto sbagliato sono nei punti che avevi classificato come forma.

**In miglioramento, con evidenza**
- *Dubbi concreti nel design.* Da "alias, immutabili" a due righe di codice vere, una delle quali è lo snippet che hai sbagliato. Nota: è migliorato dopo che la tua obiezione ha cambiato l'ordine di lavoro (prima scorri gli snippet, poi il design). Avevi ragione: in 001 il formato ti chiedeva una cosa che non potevi fare.
- *Stima complessiva.* 1 snippet con dubbi, stima 4, ottenuto 4. Prima volta a scarto zero. È una misura sola, e la stima era derivata dai campi invece che dichiarata a sentimento: è la prova che il metodo funziona, non ancora che l'abitudine è tua.
- *Tentare al primo passaggio.* Nessun "non so", nessun sollecito sulle ipotesi.
- *Nome dell'errore.* In 001: "non ho fatto errori di ragionamento". Qui: "considero solo la mutabilità di un tipo". La regola sul tipo è ancora la tua prima mossa (`design.md`, riga 7, nella sezione dove non dovevano esserci previsioni), ma adesso la riconosci come tale.
- *Nomi.* In inglese negli esperimenti. Restano per tipo `new_dict`, `base`, `second`, `key1`.

**Da coltivare**
- *Contestare un requisito con un argomento.* Dopo 001 hai fatto due obiezioni ("la trascrizione mi ha solo evitato un copia-incolla"; "se non conoscevo gli esercizi come facevo a prevedere quei dubbi?"). Erano in parte fondate e hanno cambiato il formato di 002. Sul "dopo:" non hai portato un argomento, hai portato fretta, e non è cambiato niente. La differenza tra le due cose è misurabile nei tuoi stessi risultati: l'obiezione argomentata ti ha tolto lavoro inutile, il rifiuto no.

**Da riguardare**
- *Il feedback diventa revisione?* Dipende da quando arriva. A freddo sì: scarti del 7 e del 9 riscritti tra le sessioni, il 9 bene. A metà sessione no: "dopo:" chiesto tre volte, mai scritto. In `design.md` c'è una terza domanda sull'alias che all'orchestratore non risulta: se l'hai aggiunta tu dopo il suo commento, è esattamente la mossa giusta, ma va detta.

## Da cambiare nel processo

**Una sola abitudine: ogni esperimento ha due esiti scritti prima di eseguire.**

Sostituisce la riga "Atteso ... perché ...". Prima di premere invio:

```
Se ho ragione: <output esatto>
Se ho torto:   <output esatto, diverso dal primo>
```

Poi esegui, incolli dal terminale quello che è uscito e scrivi quale dei due è.

Se non riesci a scrivere la seconda riga, o se le due righe sono uguali, l'esperimento non verifica niente: cambialo. Lo scarto dello snippet 5 non avrebbe superato questo controllo ("se ho torto" su `second["key1"] is base["key1"]` non aveva un output plausibile: sapevi già che era `True`). Quello del 9 di 001 sì: `KeyError` contro una lista.

Perché questa: in 003 non ci sono più snippet da prevedere, c'è un bug da trovare in una matrice. Lì ogni prova che lanci o distingue due spiegazioni o è tempo perso, ed è il tempo che dici di non avere.

Come si verifica: in 003 si contano gli esperimenti. Ognuno ha le due righe, con due output diversi, sopra l'output incollato. Prima applicazione: il completamento dello scarto dello snippet 5 che il reviewer chiede prima di 003 (due esperimenti, uno su `snapshot["name"] += "!"`, uno su `snapshot["scores"] = [9]`).

**Condizione, non abitudine.** "Consegno" vale con l'output di pytest incollato da te. Se vuoi lasciare un test rosso, puoi: una riga per test, "lo lascio rosso perché ...". È un'obiezione argomentata e il reviewer la valuta come tale. Senza la riga è un campo saltato.

**Sul tempo.** Se sfori, si taglia il numero di cose da fare, non la verifica di quelle fatte. Quattro snippet verificati da te valgono più di cinque con il confronto fatto da un altro.
