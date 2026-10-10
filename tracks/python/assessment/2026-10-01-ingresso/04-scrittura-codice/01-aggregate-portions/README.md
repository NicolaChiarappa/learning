# Esercizio 01 — Aggregare le porzioni (semplice)

Tempo indicativo: 20-25 min. File da completare: `aggregate_portions.py`.

## Contesto
Un'app registra cosa ha mangiato l'utente. Ogni voce è un dizionario `{"food": <nome>, "grams": <quantità>}`. I nomi arrivano da input utente, quindi sono "sporchi": maiuscole, spazi in eccesso.

## Consegna
Implementa:

```python
def aggregate_portions(entries: Iterable[Mapping[str, object]]) -> list[tuple[str, float]]:
```

La funzione restituisce, per ogni alimento, il totale dei grammi, come lista di tuple `(nome_normalizzato, totale)`.

### Regole
1. **Normalizzazione del nome**: togli gli spazi iniziali e finali, porta tutto in minuscolo e riduci le sequenze di spazi interni a uno solo. `"  Pasta   Integrale "` diventa `"pasta integrale"`. Due voci con lo stesso nome normalizzato sono lo stesso alimento.
2. **Ordinamento**: per totale decrescente; a parità di totale, per nome crescente (alfabetico).
3. **Input vuoto**: restituisce `[]`.
4. `entries` può essere **qualsiasi iterabile**, anche un generatore. La funzione non deve modificare l'input.
5. **Validazione**: se una voce non è valida solleva `ValueError`. Il messaggio deve contenere `index <i>`, dove `<i>` è la posizione della voce (a partire da 0). Una voce non è valida se:
   - manca la chiave `"food"` o la chiave `"grams"`;
   - `food` non è una stringa, oppure è vuota dopo la normalizzazione;
   - `grams` non è un numero `int` o `float` (le stringhe come `"100"` non sono valide e un booleano non è un numero valido), non è finito, oppure non è strettamente positivo.

## Note
- Solo libreria standard.
- Pensa ai casi limite **prima** di scrivere il codice. I test base ne coprono pochi.
