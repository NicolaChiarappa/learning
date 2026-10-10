# Esercizio 02 — Sessioni da uno stream di timestamp (generatori)

Tempo indicativo: 30 min. File da completare: `split_sessions.py`.

## Contesto
Un'app riceve uno **stream** di eventi di attività dell'utente, ognuno con un timestamp in secondi (float), già in ordine. Lo stream può essere molto lungo, anche potenzialmente infinito: arriva da una coda e non sta in memoria. Vuoi raggruppare gli eventi in "sessioni": due eventi consecutivi appartengono alla stessa sessione se sono abbastanza vicini nel tempo.

## Consegna
Implementa:

```python
def split_sessions(timestamps: Iterable[float], max_gap: float) -> Iterator[list[float]]:
```

### Regole
1. Due timestamp **consecutivi** appartengono alla stessa sessione se la loro differenza è `<= max_gap`. Se la differenza è `> max_gap`, inizia una nuova sessione.
2. Ogni sessione viene prodotta come `list[float]`, con i timestamp nell'ordine originale.
3. I timestamp devono essere **non decrescenti**. Valori uguali sono ammessi e restano tutti nella sessione. Se ne arriva uno minore del precedente, l'iteratore solleva `ValueError` **nel momento in cui lo incontra**. Le sessioni già prodotte restano valide.
4. `max_gap` deve essere `> 0`. Altrimenti `ValueError` va sollevato **subito, alla chiamata di `split_sessions(...)`**, non alla prima iterazione.
5. **Lazy**: la funzione deve funzionare con iterabili infiniti e non deve leggere dallo stream più elementi di quelli necessari per completare la sessione corrente. Per sapere che una sessione è finita serve leggere il primo elemento della successiva: quello è il massimo consentito.
6. Stream vuoto: nessuna sessione.

## Esempio
```python
>>> list(split_sessions([0, 10, 12, 100, 101, 400], max_gap=30))
[[0, 10, 12], [100, 101], [400]]
```

## Note
- Solo libreria standard.
- La regola 4 e la regola 5 sono in tensione con il modo più ovvio di scrivere la funzione. Pensaci prima di iniziare.
