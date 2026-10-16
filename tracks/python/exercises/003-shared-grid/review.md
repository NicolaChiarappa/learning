# Review — 003 — 2026-10-16

**Esito: PASSATO CON RISERVA.** Test base 8/8 | tuoi 5/5 sul corretto | nascosti 11/12 (rosso solo R8, facoltativa) | indizi 2 (livello 1)
Correttezza 4 | Casi limite 2 | Design 3 | Leggibilità 3 | Idiomaticità 2 | Processo 2

**Il punto che conta: hai previsto rosso il test di `close_row`, era verde, e non te ne sei accorto.** In "Durante" (righe 81-100) lo metti tra quelli che falliscono "perché la lista è una sola". Sul codice originale passa: `hall[row] = ...` sposta la posizione `row` su una lista nuova, e solo quella fila esce dal gruppo condiviso. Era il dato che distingue "modifico l'oggetto" da "sposto una posizione". Non l'hai visto perché il rosso iniziale non l'hai mai incollato, e poi hai riscritto `close_row`, che nessuna regola R1-R9 dava per rotta. Così hai cancellato la prova. Prima di toccare una funzione, chiediti: quale regola viola?

**Esperimenti che non possono smentirti.** Dubbio 2 (righe 42-79): con `for seat in ...: seat = "close"` credevi di modificare la fila, che è lo stesso errore di E001 su un nome di ciclo. Il confronto `!=` misura i valori, non l'identità. L'esito "True / False" è uscito come previsto, ma per la ragione opposta. Nella chiacchierata l'hai riconosciuto da solo (D1): è il riflesso da rendere automatico prima di eseguire.

**I tuoi test sull'originale (verifica mia, non tua):** 3 rossi, 2 verdi. `test_zero_rows` e `test_n_empty_rows` passano sul codice con il bug, quindi non sono test di regressione. Il secondo controlla le lunghezze ma non che le file vuote siano indipendenti (R7: "indipendenti"). Avevi detto "sono tutti rossi" senza incollare l'output. Bene invece: `free_per_row` l'hai separato come causa diversa, e il test sull'unione degli `id` delle due sale l'hai rafforzato da solo, dopo averlo bucato con un controesempio tuo.

**Codice.** `seating.py:16` `list[list[str]]()` istanzia un alias generico: funziona, ma non è il modo idiomatico di scrivere una lista vuota. `seating.py:35` usa un indice manuale per riscrivere il contenuto di una fila: esiste un costrutto diretto (M04). `seating.py:38-39` ha una riga vuota di troppo.

**Calibrazione.** Nessuna stima numerica. "Fallirò i casi limite" contraddice "R7 coperta", e i casi limite sono passati tutti tranne R8. Manca la regola finale.

**`+=` con indice a sinistra (E005):** ancora nessun esperimento. In D2 dici cosa fa all'oggetto, non cosa fa alla posizione.

Errori: E001 occ. 3 e E004 occ. 3 (ripasso 2026-10-23); E003 riaperto (`[list(free_row)] * 2`, ripasso 2026-10-23); nuovo E007 (`==` usato per provare l'identità, ripasso 2026-10-26); E005 ed E006 non verificati, date invariate.
