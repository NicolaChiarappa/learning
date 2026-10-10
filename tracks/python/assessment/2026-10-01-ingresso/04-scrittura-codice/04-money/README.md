# Esercizio 04 — Value object `Money` (OOP, dunder, Decimal, design)

Tempo indicativo: 50-60 min. File da completare: `money.py`.

## Contesto
Gli importi in euro non si gestiscono con i `float`. Ti serve un **value object** `Money`: immutabile, confrontabile, sicuro rispetto alle valute. Come implementarlo (classe normale, dataclass, `__slots__`...) è una tua scelta di design, purché rispetti l'interfaccia qui sotto.

## Interfaccia richiesta

```python
class CurrencyMismatchError(ValueError): ...

class Money:
    def __init__(self, amount: Decimal | int | str, currency: str) -> None: ...
    amount: Decimal      # read-only
    currency: str        # read-only
    def allocate(self, ratios: Sequence[int]) -> list["Money"]: ...
```

### Costruzione
1. `amount` accetta `Decimal`, `int` o `str` (per esempio `"12.5"`). Viene arrotondato a **2 decimali con `ROUND_HALF_UP`**: `"1.005"` diventa `1.01`.
2. Un `float` solleva `TypeError`, perché gli importi non devono mai passare da un float. Anche `bool` e qualunque altro tipo sollevano `TypeError`.
3. Una stringa non numerica, `NaN` o un valore infinito sollevano `ValueError`.
4. `currency` deve essere una stringa di **esattamente 3 lettere ASCII**. Viene normalizzata in maiuscolo (`"eur"` diventa `"EUR"`). Se la stringa non è valida solleva `ValueError`; se non è una stringa, `TypeError`.
5. Gli attributi sono **in sola lettura**: assegnare `m.amount = ...` solleva `AttributeError`.

### Rappresentazione
6. `repr(Money("12.5", "eur"))` restituisce `Money('12.50', 'EUR')`.
7. `str(Money("12.5", "eur"))` restituisce `12.50 EUR`.

### Uguaglianza e hashing
8. Due `Money` sono uguali se hanno stesso importo e stessa valuta: `Money("1", "EUR") == Money("1.00", "EUR")`. Con la stessa valuta e lo stesso importo devono avere lo stesso hash, così da poter stare in set e dict.
9. Il confronto con un oggetto che non è `Money` restituisce `False` per `==` e non solleva eccezioni.

### Aritmetica e ordinamento
10. `+` e `-` tra `Money` della stessa valuta restituiscono un nuovo `Money`. Con valute diverse sollevano `CurrencyMismatchError`. Con un operando che non è `Money` sollevano `TypeError`.
11. `-m` (meno unario) restituisce l'opposto.
12. `m * n` e `n * m`, con `n` di tipo `int` o `Decimal`, restituiscono un nuovo `Money` arrotondato come al punto 1. Con `float`, `bool` o `Money` sollevano `TypeError`.
13. `sum(lista_di_money)` funziona per liste **non vuote** della stessa valuta, senza passare il parametro `start`.
14. `<`, `<=`, `>`, `>=` funzionano tra `Money` della stessa valuta. Con valute diverse sollevano `CurrencyMismatchError`.

### `allocate`
15. `allocate(ratios)` divide l'importo in parti proporzionali ai `ratios` **senza perdere né creare centesimi**: la somma delle parti è sempre esattamente uguale all'originale.
    - Ogni parte riceve prima la quota proporzionale **arrotondata per difetto al centesimo**.
    - I centesimi avanzati vengono assegnati uno alla volta, nell'ordine delle posizioni, alle sole parti con ratio `> 0`.
    - Con un importo negativo il risultato è l'opposto di quello che si ottiene allocando il valore assoluto.
    - `ratios` deve contenere solo `int` (`bool` escluso) `>= 0`, avere almeno un elemento e somma `> 0`. Altrimenti `ValueError`.
    - Il risultato ha la stessa lunghezza di `ratios`.

```python
>>> Money("100", "EUR").allocate([1, 1, 1])
[Money('33.34', 'EUR'), Money('33.33', 'EUR'), Money('33.33', 'EUR')]
>>> Money("0.05", "EUR").allocate([3, 7])
[Money('0.02', 'EUR'), Money('0.03', 'EUR')]
```

## Note
- Solo libreria standard.
- Al termine scrivi in fondo a `money.py`, in un commento di 3-6 righe, **perché** hai scelto quella forma di classe e quali alternative hai scartato.
