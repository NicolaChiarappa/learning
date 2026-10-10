# Esercizio 03 — Decoratore con cache a scadenza (decoratori, testabilità)

Tempo indicativo: 40 min. File da completare: `ttl_cache.py`.

## Contesto
Una funzione interroga un servizio esterno lento, per esempio i valori nutrizionali di un alimento. I risultati cambiano raramente: vuoi tenerli in cache per un tempo limitato. `functools.lru_cache` non ha una scadenza, quindi scrivi un decoratore tuo. **Non usare `lru_cache` né `cache` per implementarlo.**

## Consegna
Implementa:

```python
def ttl_cache(seconds: float, *, clock: Callable[[], float] = time.monotonic):
```

Uso:

```python
@ttl_cache(seconds=60)
def nutrition_for(food_id: int, *, locale: str = "it") -> dict: ...
```

### Regole
1. Il risultato di una chiamata viene memorizzato e riusato per le chiamate successive **con gli stessi argomenti** (posizionali e keyword). L'ordine in cui passi gli argomenti keyword non conta: `f(a=1, b=2)` e `f(b=2, a=1)` sono la stessa chiamata. Non serve trattare `f(1)` e `f(a=1)` come uguali.
2. Una voce è valida finché `clock() - momento_in_cui_è_stata_salvata < seconds`. Quando la differenza è `>= seconds` la voce è scaduta: la funzione viene richiamata e il nuovo risultato sostituisce quello vecchio.
3. Se la funzione solleva un'eccezione, **niente** viene messo in cache e l'eccezione si propaga invariata.
4. Qualsiasi valore di ritorno va messo in cache, compresi `None`, `0` e `""`.
5. Se un argomento non è hashable (per esempio una lista), la funzione viene chiamata normalmente, **senza** cache e **senza** errori.
6. `seconds <= 0` solleva `ValueError` subito, quando viene chiamato `ttl_cache(...)`.
7. La funzione decorata deve mantenere `__name__`, `__doc__` e `__wrapped__` dell'originale, ed esporre due metodi:
   - `cache_clear()`: svuota la cache;
   - `cache_size() -> int`: numero di voci attualmente memorizzate.
8. Ogni funzione decorata ha una cache **propria**.
9. Le voci scadute non devono accumularsi per sempre. Quando una chiamata trova la propria voce scaduta, la voce vecchia viene sostituita, non duplicata. Non è richiesta una pulizia periodica delle altre voci scadute.

### Perché `clock`?
Il parametro `clock` serve a rendere il decoratore **testabile senza aspettare davvero**. Guarda come lo usano i test base.

## Note
- Solo libreria standard. Non serve che sia thread-safe.
