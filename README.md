# Learning System — Setup

Sistema di apprendimento con un orchestratore e 5 agenti specializzati per Claude Code.

## Installazione
1. Copia la cartella `learning/` dove preferisci (es. `~/learning`).
2. Inizializza git (consigliato: è la cronologia dei tuoi progressi):
   ```bash
   cd ~/learning
   git init && git add . && git commit -m "Setup learning system"
   ```
3. Avvia Claude Code nella cartella:
   ```bash
   claude
   ```
4. Controlla che gli agenti siano caricati con il comando `/agents`. Devi vedere: assessor, planner, exercise-designer, reviewer, mentor.

## Comandi
| Comando | Cosa fa |
|---|---|
| `/test-ingresso python` | Prepara il test d'ingresso; rilanciato dopo averlo svolto, lo valuta e genera la roadmap |
| `/sessione python` | Apre una sessione: stato, ripassi in scadenza, proposta del prossimo esercizio |
| `/consegna python 003` | Consegna un esercizio: review, analisi del mentor, aggiornamento dei progressi |
| `/verifica python` | Mini-verifica ogni 2 settimane e aggiornamento della roadmap |
| `/settimana` | Revisione settimanale del mentor |

Per tutto il resto parla normalmente con l'orchestratore: domande di teoria, richieste di indizi, cambi di programma.

## Primo giorno
1. `/test-ingresso python` → svolgi il test **senza IA** (circa 3-4 ore).
2. `/test-ingresso python` di nuovo → valutazione e roadmap.
3. Nei giorni successivi fai lo stesso con `django` e `typescript-react`, poi inizia con `/sessione python`.

## Prerequisiti
- Python 3.12+ e `pip install pytest` (meglio in un venv nella cartella)
- Per Django: `pip install django django-ninja pytest-django factory-boy`
- Per TypeScript/React/Expo: Node.js LTS. Le dipendenze le indicherà ogni esercizio.

## Struttura
```
CLAUDE.md                 # istruzioni dell'orchestratore
.claude/agents/           # i 5 agenti
.claude/commands/         # i comandi /sessione, /consegna, ...
profile/                  # errori ricorrenti e pattern di ragionamento
tracks/<track>/           # competenze, test, roadmap, progressi, esercizi
tracks/capstone/          # app di tracking nutrizionale
sessions/                 # log brevi di ogni sessione
weekly/                   # revisioni settimanali
```

## Personalizzare
Gli agenti sono file Markdown: puoi modificarli quando qualcosa non funziona. Esempi: un reviewer troppo morbido, esercizi troppo facili, test troppo lunghi. Dopo 1-2 settimane d'uso conviene rivederli insieme all'orchestratore.
