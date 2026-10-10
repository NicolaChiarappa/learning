# Esercizio 05 — Import CSV dei pasti (design, validazione, date, errori)

Tempo indicativo: 70-90 min, nota di design compresa. File da completare: `meal_import.py` e `NOTE.md`.

**Prima di scrivere codice compila `NOTE.md`** (10-15 minuti). È parte della valutazione.

## Contesto
Gli utenti caricano un export CSV dei pasti, generato da un'altra app o compilato a mano in Excel. Il file è sporco. L'import **non deve fermarsi al primo errore**: deve importare le righe valide e restituire un elenco preciso delle righe scartate e del motivo, da mostrare all'utente.

## Interfaccia richiesta
```python
def import_meals(text: str, tz: str) -> ImportReport: ...

class ImportFileError(Exception): ...
```

Il **design dei tipi è tuo**: `ImportReport`, il tipo dei pasti, il tipo degli errori di riga, eventuali funzioni di supporto. I test accedono **solo** a questi attributi:

- `report.meals`: lista dei pasti validi, nell'ordine del file;
- `report.errors`: lista degli errori di riga, nell'ordine del file;
- per ogni pasto: `.eaten_at` (`datetime` aware in UTC), `.food` (`str`), `.grams` (`Decimal`), `.kcal` (`Decimal`);
- per ogni errore di riga: `.line` (`int`), `.field` (`str | None`), `.message` (`str`, leggibile da un utente).

## Formato del file
- CSV standard: separatore `,`, campi tra virgolette ammessi, per esempio `"pasta, al pomodoro"`. Le righe possono terminare con `\n` o `\r\n`. Il testo può iniziare con un BOM UTF-8 (`﻿`, tipico di Excel), che va ignorato.
- La **prima riga** è l'intestazione e deve contenere le colonne `timestamp`, `food`, `grams`, `kcal_per_100g`. L'ordine può variare. I nomi si confrontano ignorando maiuscole e spazi attorno. Colonne extra sono ammesse e vengono ignorate.
- Numerazione: l'intestazione è la riga 1. `.line` indica la riga fisica nel file.
- Le righe vuote o composte solo da spazi vengono ignorate, ma contano nella numerazione.

## Errori a livello di file: eccezione
- `ImportFileError` se il testo è vuoto (o contiene solo spazi), oppure se nell'intestazione manca una delle colonne richieste.
- `ValueError` se `tz` non è un fuso orario IANA valido (per esempio `"Europe/Rome"`). Va controllato prima di leggere il file.

## Errori a livello di riga: vanno nel report, la riga viene scartata
- Una riga con un numero di campi diverso dall'intestazione produce **un solo** errore con `field=None`.
- Altrimenti ogni campo non valido produce **un** errore con `field` uguale al nome canonico della colonna (`"timestamp"`, `"food"`, `"grams"`, `"kcal_per_100g"`). Una riga con due campi non validi produce due errori, in questo ordine: timestamp, food, grams, kcal_per_100g.

Regole dei campi (a tutti i valori vengono tolti gli spazi attorno):
- `timestamp`: formato ISO 8601, per esempio `2026-09-30 12:30`, `2026-09-30T12:30:00` o `2026-09-30T12:30:00+02:00`.
  - Se **non ha offset**, è un orario locale nel fuso `tz`.
  - Se **ha offset**, si usa quello.
  - Un orario locale **che non esiste** nel fuso `tz` (il salto dell'ora legale, per esempio `2026-03-29 02:30` a Roma) è un errore.
  - Un orario locale **ambiguo** (il ritorno all'ora solare) si interpreta come la **prima** occorrenza.
  - `.eaten_at` è sempre convertito in UTC.
- `food`: non vuoto.
- `grams`: numero decimale con il punto (`"150.5"`; `"150,5"` è un errore), finito e `> 0`.
- `kcal_per_100g`: numero decimale con il punto, finito e `>= 0`.
- `.kcal` = `grams * kcal_per_100g / 100`, arrotondato a **1 decimale con `ROUND_HALF_UP`**.

## Esempio
Con `tz="Europe/Rome"`:

```
timestamp,food,grams,kcal_per_100g
2026-09-30 12:30,pasta,80,350
2026-09-30 13:00,,abc,50
```
→ 1 pasto (`eaten_at` = 2026-09-30 10:30 UTC, kcal 280.0) e 2 errori sulla riga 3: `food` e `grams`.

## Note
- Solo libreria standard.
- I test base coprono il caso normale. I casi descritti sopra verranno verificati tutti.
