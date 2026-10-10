# Progress — python

Unica fonte di verità sullo stato della track. Aggiornato da planner (moduli) e reviewer (esercizi).

## Stato attuale
- **Modulo corrente**: M01 — Nomi, oggetti, riferimenti (non ancora iniziato)
- **Prossimo esercizio previsto**: M01, esercizio 1 "Prevedi e verifica" (snippet su aliasing, copie, mutazione; previsione scritta, poi REPL)
- **Ultimo test o verifica**: ingresso, valutato il 2026-10-10 (`tracks/python/assessment/2026-10-01-ingresso/risultati.md`)
- **Prossima verifica prevista**: V1 il 2026-10-23 (2 settimane dall'inizio previsto del 2026-10-12; da spostare se l'inizio effettivo cambia). Copre M01-M03 e quanto chiuso di M04.

## Moduli
| Modulo | Stato | Inizio | Fine | Esito |
|---|---|---|---|---|
| M01 — Nomi, oggetti, riferimenti | da fare | — | — | — |
| M02 — Dalla specifica ai test: casi limite, pytest, traceback | da fare | — | — | — |
| M03 — Tipi built-in, costi, `collections` | da fare | — | — | — |
| M04 — Controllo di flusso idiomatico | da fare | — | — | — |
| M05 — Funzioni: firme, scope, closures | da fare | — | — | — |
| M06 — Eccezioni | da fare | — | — | — |
| M07 — Classi: attributi di classe e istanza, property, classmethod | da fare | — | — | — |
| M08 — Metodi speciali | da fare | — | — | — |
| M09 — Iteratori e generatori | da fare | — | — | — |
| M10 — `itertools` e pipeline lazy | da fare | — | — | — |
| M11 — Decoratori e `functools` | da fare | — | — | — |
| M12 — Context manager e gestione delle risorse | da fare | — | — | — |
| M13 — `dataclasses`, `enum`, immutabilità | da fare | — | — | — |
| M14 — Type hints e type checker | da fare | — | — | — |
| M15 — Importi e serializzazione: `decimal`, `json`, `csv` | da fare | — | — | — |
| M16 — `datetime` e `zoneinfo` | da fare | — | — | — |
| M17 — Ereditarietà, MRO, `super()`, mixin | da fare | — | — | — |
| M18 — Composizione, `abc` e `Protocol`, quando astrarre | da fare | — | — | — |
| M19 — Testing: fixture, parametrize, mock, codice testabile | da fare | — | — | — |
| M20 — Moduli, package, strumenti, logging | da fare | — | — | — |
| M21 — Refactoring sicuro e separazione delle responsabilità | da fare | — | — | — |
| M22 — Concorrenza: thread, processi, `asyncio` | da fare | — | — | — |
| M23 — Progetto di sintesi: import di pasti | da fare | — | — | — |

## Esercizi
| NNN | Data | Modulo | Corr. | Casi lim. | Design | Legg. | Idiom. | Proc. | Indizi | Esito |
|---|---|---|---|---|---|---|---|---|---|---|

## Note
(Solo informazioni utili agli altri agenti: blocchi, cambi di direzione, richieste di Nick.)

- 2026-10-10 (planner): roadmap creata dal test d'ingresso. Nessuna area SOLIDA; 23 moduli, 74 giorni di lavoro stimati. La sequenza di `CLAUDE.md` (Python settimane 1-5) non regge: stima 16-17 settimane in sequenza. Dettagli e proposta in `tracks/python/roadmap.md`, sezione "Valutazione onesta della durata".
- Per exercise-designer: applicare in ogni esercizio la sezione "Metodo: vale in ogni modulo" della roadmap. In Fase 1 (M01-M05) esercizi da 20-45 minuti con un solo concetto nuovo; formati: prevedi e verifica, trova il bug, funzione piccola da specifica. `design.md` corto (5-10 righe) ma obbligatorio, con regole numerate e griglia dei casi limite da M02.
- Per reviewer: registrare per ogni esercizio lo scarto tra previsione dichiarata da Nick e risultato (calibrazione), e valutare sempre nomi in inglese e per ruolo.
- Regola del tentativo minimo: nessun esercizio si salta; 20 minuti di lavoro più nota sul punto di blocco valgono come consegna. Motivo: tre esercizi su cinque saltati nel test d'ingresso.
- Decisioni in attesa di Nick (sezione "Decisioni aperte" della roadmap): sequenza delle track, giorni a settimana, collocazione di M22, riuso dei problemi S03/S04/S05 come esercizi.
- 2026-10-10 (orchestratore, decisioni di Nick): lavora 7 giorni su 7, minimo 1 ora al giorno, spesso di più (le stime della roadmap assumono 5 giorni da 3-4 ore: ricalibrare alla verifica V1 sul ritmo reale). Avvio della track Django rimandato: si decide più avanti, non prima della fine della Fase 2. Restano aperte: collocazione di M22, riuso di S03/S04/S05.
