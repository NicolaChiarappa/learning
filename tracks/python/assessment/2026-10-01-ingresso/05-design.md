# Parte 5 — Design

Due domande aperte. Rispondi in prosa (puoi aggiungere un elenco puntato o una firma di funzione o classe), **al massimo una pagina per domanda**. Non esiste una risposta unica giusta: conta come ragioni, quali alternative consideri, quali trade-off dichiari e cosa decidi di **non** fare.

---

## Domanda 1 — Calcolo dei totali nutrizionali giornalieri

Devi scrivere il modulo Python (puro, senza Django) che calcola i totali nutrizionali giornalieri di un utente: kcal, proteine, carboidrati e grassi.

Vincoli:
- I valori degli alimenti arrivano da un'**API esterna** lenta (300-800 ms), che a volte va in timeout e a volte restituisce campi mancanti.
- I pasti dell'utente sono registrati in **unità diverse**: grammi, millilitri, "pezzi" (1 uovo, 1 mela). Per i pezzi l'API fornisce, a volte, un peso medio.
- L'utente vive in un fuso orario; "giornata" significa la sua giornata locale.
- Il modulo deve essere **testabile senza rete**.

Rispondi:
1. Quali tipi o classi definiresti e quali responsabilità avrebbe ciascuno? Indica le firme principali.
2. Dove passa il confine tra dati "non fidati" e dati validati? Cosa succede quando un alimento ha dati incompleti o l'API non risponde: errore, valore parziale, altro? Motiva.
3. Come rappresenteresti le quantità e le unità per evitare errori come sommare grammi e pezzi?
4. Come lo testeresti? Cosa sostituiresti con un fake o un mock e cosa no?
5. Quale parte del design ti convince di meno, e perché?

**Risposta:**
le firme precise non riesco ad immaginarle in ogni caso mi immagino un modulo che fa da confine tra l'api e il mio sistema, questo modulo di confine fa le chiamate e pulisce i dati quando arrivano dall'esterno e li normalizza nel formato che la mia app si aspetta. il modulo di boundary dipende da uno o più providers, almeno due: uno di fallback con dati mockati quando l'api non risponde e uno che chiama l'api vera e propria. come scelgo cosa può essere mockato e cosa no
non lo so. la parte del design che mi convince di meno è la chiamata all'api ad ogni richiesta che si riceve, si può pensare ad un meccanismo che aggiorna i dati solo quando c'è n'è bisogno, magari andando a controllare il last_update_time una volta ogni tot, o simili


---

## Domanda 2 — Smontare un `utils.py`

In un progetto Django in produzione c'è `core/utils.py`: 2.000 righe con funzioni di date, formattazione di prezzi, invio email, chiamate HTTP a un fornitore, helper per i queryset. Viene importato da 60 file. Ci sono già due import circolari aggirati con `import` dentro le funzioni. La copertura dei test è intorno al 30%.

Rispondi:
1. Perché un import circolare a volte "funziona" e a volte esplode con `ImportError: cannot import name ... (most likely due to a circular import)`? Cosa ti dice sul design?
2. Come lo divideresti? Con quale criterio scegli i nuovi moduli e cosa eviti?
3. Come procedi **senza rompere la produzione**? Indica l'ordine dei passi, la rete di sicurezza (test, compatibilità degli import esistenti) e come capisci di aver finito.
4. Cosa **non** faresti, anche se è allettante?

**Risposta:**

può esplodere perché magari il modulo che importiamo nella funzione usa proprio quella funzione, e questo può succedere se in futuro qualcuno chiama quella funzione proprio in quel modulo e non sa che c'è causerebbe una dipendenza circolare. in generale è sintomo di una gerarchia dei moduli disordinata e che ha progettato il software non si è occupato troppo di capire chi dipende da chi.
quello che bisogna fare è capire qual'è il flusso di dipendenza e dividere il codice in sotto moduli che rispettano questa dipendenza.
alla fine esporre all'esterno solo il modulo più esterno, in questo modo chi utilizzava quel file non dovrebbe rompersi se ha scritto gli import nella maniera corretta
il modulo si chiama comunque utils

Cosa non farei anche se è allettante? non lo so

---

Tempo impiegato: 10 min | Sicurezza (1-5): 2
