# Capstone — App di tracking nutrizionale

Progetto finale che unisce le tre track. Parte indicativamente dalla settimana 8, quando Python e Django sono avviati e TypeScript/React è in corso.

## L'idea (di Nick)
App di tracking nutrizionale in stile MyFitnessPal:
- tracking di kcal, macronutrienti e micronutrienti
- ricette
- generazione di un menu settimanale

Nick sa che il problema è già in gran parte risolto sul mercato. L'obiettivo del capstone è **costruirla bene**, non fare un prodotto commerciale. Resta aperta l'ipotesi di andare verticale su un mercato specifico: la decisione può arrivare più avanti e non blocca il lavoro tecnico.

## Perché è un buon capstone
| Track | Cosa allena |
|---|---|
| Python | Calcolo dei nutrienti, scalatura delle ricette, conversione unità, generazione di menu con vincoli: algoritmi veri, pieni di casi limite |
| Django + Ninja | Modellazione relazionale non banale (alimenti, nutrienti, ricette, porzioni, diario, piani), API ben progettate, prestazioni delle query |
| TypeScript + Expo | App mobile con form complesse, liste lunghe, funzionamento offline, stati di caricamento ed errore |

## Regole del capstone
1. **Nessun codice senza documento di design.** Ogni milestone parte da un `design/<milestone>.md` scritto da Nick: requisiti, modello dati, API, casi limite, alternative scartate.
2. **Il reviewer valuta le milestone** come gli esercizi, con la stessa rubrica e con test nascosti dove possibile.
3. **Il mentor valuta le decisioni di architettura**: sono le più importanti del progetto.
4. **Scope piccolo e completo** prima di scope grande e incompleto.

## Milestone indicative
(Il planner le dettaglierà in `roadmap.md` quando il capstone partirà.)

1. **Dominio in Python puro**: modello degli alimenti e dei nutrienti, calcolo dei valori per porzione, scalatura delle ricette, conversione delle unità. Niente framework, solo Python e test.
2. **Backend Django + Ninja**: modelli, migrazioni, API CRUD per alimenti e ricette, autenticazione.
3. **Diario alimentare**: registrazione dei pasti, totali giornalieri, obiettivi.
4. **App Expo**: autenticazione, ricerca alimenti, registrazione pasti, riepilogo giornaliero.
5. **Generatore di menu settimanale**: algoritmo con vincoli (kcal, macro, varietà, preferenze). È la parte algoritmicamente più interessante.
6. **Qualità**: offline, prestazioni, test end-to-end, deploy.

## Dati
Per gli alimenti valutare un database pubblico (es. Open Food Facts, o tabelle nutrizionali ufficiali). Prima di scegliere, va scritta una nota su licenza, qualità e copertura dei dati.

## Struttura
```
tracks/capstone/
├── brief.md          # questo file
├── roadmap.md        # generata dal planner all'avvio
├── progress.md
├── design/           # documenti di design di Nick, uno per milestone
└── code/             # repository del progetto (backend/ e app/)
```
