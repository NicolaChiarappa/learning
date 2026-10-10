# Parte 2 — Concetti

20 domande a risposta breve: da 3 a 8 righe ciascuna, salvo dove è indicato diversamente. Contano il **perché** e la precisione, non la lunghezza. Niente documentazione e niente esecuzione di codice. Se non sai, scrivi "non lo so" o scrivi solo quello che sai con certezza.

La difficoltà cresce più o meno con il numero della domanda.

---

### 1. Identità e uguaglianza
Perché si scrive `if x is None:` e non `if x == None:`? In generale, quando è corretto usare `is` e quando è un bug? Fai un esempio di un uso di `is` che **sembra** funzionare ma è sbagliato.

**Risposta:**
non lo so

---

### 2. Liste annidate
```python
grid = [[0] * 3] * 3
grid[0][0] = 1
```
Cosa contiene `grid` dopo queste righe e perché? Come costruiresti correttamente una griglia 3x3?

**Risposta:**
il primo sembra un vettore con 3 vettori annidati, non so se l'operazione *3 su un vettore funziona così.
non so cosa contiene grid.
quello che so è che una matrice 3x3 la possiamo vedere come un vettore con 3 vettori di dimensione 3 annidati:
una cosa del genere grid = [[3]*3]

---

### 3. Costo delle operazioni
Qual è la complessità di `x in some_list`, `x in some_set`, `some_list.pop(0)` e `some_list.pop()`? Perché un elemento di un `set` deve essere hashable? Cosa può andare storto se un oggetto cambia il proprio hash dopo essere stato inserito in un set?

**Risposta:**
non lo so


---

### 4. Scope
```python
def make_counter():
    count = 0
    def increment():
        count += 1
        return count
    return increment

c = make_counter()
c()
```
Cosa succede all'ultima riga e **perché** (spiega la regola, non solo l'errore)? Dai due modi per correggerlo e dì quale preferisci e perché.

**Risposta:**
l'ultima riga produce un errore perché non sa cosa sia count, perché la funzione vede solo le variabili dichiarate dentro il corpo o passate per argomento
possiamo o modificare lo scope della varibile dentro la funzione interna, oppure passare count come parametro
non saprei dirti cosa preferisco

---

### 5. Firme delle funzioni
Hai una funzione di libreria `def transfer(source, target, amount, *, dry_run=False)`. Perché `dry_run` è keyword-only? In quali casi useresti invece un parametro positional-only (`/`)? Dai un motivo concreto per ciascuno.

**Risposta:**
so cosa sono positional-only e keyword-only ma non so quando conviene cosa, vado per logica e dico che dry_run è kw-only perché potremmo avere diversi booleani come parametro e distinguerli è fondamentale, positional only non saprei perché preferirli

---

### 6. Iterabile e iteratore
Qual è la differenza tra un iterabile e un iteratore? Perché puoi fare due volte `for x in my_list` ma un generatore si "svuota" dopo il primo ciclo? Che problema concreto risolve una pipeline di generatori quando devi processare un file di log da 10 GB?

**Risposta:**
un iterabile è il contenuto, un iteratore lo consuma dall'inizio alla fine.
non sono molto ferrato ma ad intuito, puoi fare for x in my_list perché python genera ogni volta un iteratore è quello è un modo sintetico di scriverlo nella sintassi. 
il problema che risolve è non caricare tutto in memoria, ma non so di cosa stiamo parlando davvero.

---

### 7. Decoratori
Cosa fa `functools.wraps` e cosa si rompe concretamente se lo ometti (almeno due cose)? Perché un decoratore con argomenti, come `@retry(times=3)`, richiede un livello di funzione annidata in più rispetto a `@retry`?

**Risposta:**
non lo so

---

### 8. groupby
`itertools.groupby` ha un comportamento che sorprende chi lo usa per la prima volta come un "GROUP BY" SQL. Qual è, e perché secondo te è stato progettato così?

**Risposta:**
non lo so

---

### 9. `__eq__` e `__hash__`
Che relazione deve esserci tra `__eq__` e `__hash__`? Cosa fa Python se in una classe definisci `__eq__` ma non `__hash__`, e perché questa scelta ha senso?

**Risposta:**
non lo so


---

### 10. Scegliere una struttura per i dati
Per rappresentare "un alimento con nome, kcal per 100 g e macronutrienti", quando sceglieresti `@dataclass(frozen=True)`, quando `NamedTuple`, quando una classe normale e quando un `dict` o `TypedDict`? Dai criteri, non solo preferenze.

**Risposta:**
non li ho mai sentiti questi nomi


---

### 11. Attributi di classe e `@property`
Qual è la differenza tra un attributo di classe e un attributo di istanza quando li **leggi** e quando li **assegni** tramite `self`? Quando ha senso una `@property` e quando è un segnale di design sbagliato, cioè nasconde un costo o un effetto collaterale?

**Risposta:**
non lo so

---

### 12. Eccezioni: catturare o propagare
Come decidi se catturare un'eccezione o lasciarla propagare? Che differenza c'è, sia nel traceback sia nel significato, tra queste tre forme dentro un blocco `except KeyError as e:`?
- `raise ConfigError("missing key")`
- `raise ConfigError("missing key") from e`
- `raise ConfigError("missing key") from None`

**Risposta:**
lo decido in base a chi ha la responsabilità di gestire quella specifica eccezione. questa è teoria poi la pratica porta ad una serie di decisioni da fare sul singolo caso d'uso
le differenze che mi proponi non le conosco

---

### 13. Context manager
Cosa garantisce un blocco `with`, e cosa no? Cosa succede se `__exit__` ritorna `True`? Se scrivi un context manager con `@contextlib.contextmanager`, dove va il `try/finally` e cosa succede se lo dimentichi?

**Risposta:**
non so cosa sia un context manager

---

### 14. Numeri e importi
Perché `0.1 + 0.2 == 0.3` è `False`? Che differenza c'è tra `Decimal(0.1)` e `Decimal("0.1")`? Quali conseguenze ha tutto questo per chi salva e somma importi in euro?

**Risposta:**
non ne ho idea

---

### 15. Date e fusi orari
Che differenza c'è tra un `datetime` naive e uno aware? Perché in un backend conviene salvare i timestamp in UTC? Fai un esempio concreto di bug che compare solo due volte all'anno.

**Risposta:**
non lo so

---

### 16. MRO e `super()`
In una gerarchia con ereditarietà multipla (`class C(A, B)`, con `A` e `B` che ereditano da `Base`), `super().__init__()` dentro `A` chiama "il genitore di A"? Cosa chiama davvero, e perché questo rende possibili i mixin cooperativi?

**Risposta:**
io a questa domanda sono confuso, non vedo come il fatto che C eredita da A e B dovrebbe influenzare il meccanismo di A.
In ogni caso se A eredita da Base, allora super().__init__ chiama l'inizializzatore di Base

---

### 17. ABC e Protocol
Che differenza c'è tra definire un'interfaccia con `abc.ABC` e con `typing.Protocol`? In quale situazione sceglieresti l'una e in quale l'altra?

**Risposta:**
Non lo so

---

### 18. Type hints e varianza
I type hints vengono controllati quando il programma gira? Per il parametro di una funzione che **legge soltanto** una collezione di elementi, perché è spesso meglio annotare `Sequence[Animal]` invece di `list[Animal]`? Cosa direbbe il type checker passando una `list[Dog]` a un parametro `list[Animal]`, e perché?

**Risposta:**
no, vengono controllati prima che gira. 
non so perché è meglio sequence di list
non so cosa direbbe il type checker

---

### 19. Logging e test
a) In un modulo di libreria, perché si usa `logger = logging.getLogger(__name__)` e non si chiama `logging.basicConfig()`? Perché `logger.info("user %s", user_id)` è preferibile a `logger.info(f"user {user_id}")`?

b) Il modulo `orders.py` fa `from payments import charge` e poi chiama `charge(...)`. In un test vuoi sostituire `charge`. Perché patchare `payments.charge` non funziona, e cosa patcheresti? In generale, cosa **non** va mockato?

**Risposta:**
non so rispondere a nessuno


---

### 20. Concorrenza
Hai due job: (A) scaricare 200 URL, (B) ridimensionare 200 immagini con codice Python puro. Per ciascuno, useresti thread, processi o asyncio, e perché? Spiega il ruolo del GIL. Cosa succede se dentro una coroutine chiami `time.sleep(2)` invece di `await asyncio.sleep(2)`?

**Risposta:**
non lo so


---

Tempo impiegato: 30 min | Sicurezza (1-5): 2
