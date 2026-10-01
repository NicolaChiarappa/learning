# Mappa competenze — Django + Django Ninja

Riferimento fisso per assessor e planner. Ogni area si valuta da 0 a 4.
Nota: Nick usa già Django in produzione. Il test deve distinguere tra "lo uso perché c'è nel progetto" e "so perché funziona così e quando non usarlo".

## A. Architettura di Django
- A1. Ciclo di una richiesta: URL resolver, middleware, view, risposta
- A2. Struttura di progetto e app; quando creare una nuova app
- A3. Settings per ambienti diversi, variabili d'ambiente, segreti

## B. ORM e modellazione dati
- B1. Modelli, tipi di campo, `Meta`, scelta delle chiavi primarie
- B2. Relazioni: FK, M2M (con `through`), OneToOne; `on_delete` e le sue conseguenze
- B3. Migrazioni: creazione, data migration, migrazioni reversibili, conflitti
- B4. QuerySet: lazy evaluation, caching, concatenazione di filtri
- B5. Problema N+1: `select_related`, `prefetch_related`, `Prefetch`
- B6. `annotate`, `aggregate`, `Q`, `F`, `Subquery`, `Exists`, espressioni condizionali
- B7. Vincoli e indici: `UniqueConstraint`, `CheckConstraint`, indici composti
- B8. Transazioni: `atomic`, `select_for_update`, race condition
- B9. Manager e QuerySet custom
- B10. Leggere l'SQL generato e capire il piano di esecuzione (`explain`)

## C. Logica di business e architettura applicativa
- C1. Dove mettere la logica: fat models, service layer, selectors; trade-off
- C2. Signals: come funzionano e perché spesso vanno evitati
- C3. Validazione: `clean`, validatori, validazione nel modello vs nell'API
- C4. Management command
- C5. Task asincroni e in background (Celery o alternative): quando servono

## D. View, form e template (Django classico)
- D1. Function-based vs class-based view
- D2. Form e ModelForm, validazione
- D3. Admin: personalizzazione, prestazioni con molti dati

## E. Sicurezza e autenticazione
- E1. Autenticazione, modello User custom, permessi e gruppi
- E2. CSRF, XSS, SQL injection: come Django protegge e dove puoi sbagliare tu
- E3. Autorizzazione a livello di oggetto (chi può vedere cosa)

## F. Django Ninja
- F1. Router, operazioni, path e query parameter
- F2. Schema (Pydantic): input vs output, `ModelSchema`, validazione, campi calcolati
- F3. Gestione degli errori: eccezioni, codici HTTP corretti, formato degli errori coerente
- F4. Autenticazione (API key, token, JWT) e permessi per endpoint
- F5. Paginazione, filtri, ordinamento
- F6. Documentazione OpenAPI e sua qualità
- F7. Async view con Ninja: quando hanno senso, interazione con l'ORM
- F8. Versioning delle API

## G. Design delle API (trasversale)
- G1. Risorse e URL REST, metodi HTTP, idempotenza
- G2. Contratti stabili, retrocompatibilità
- G3. Status code e gestione errori coerente
- G4. Prestazioni: query count per endpoint, payload, caching

## H. Testing
- H1. pytest-django o TestCase: database di test, transazioni
- H2. Factory (factory_boy) vs fixture
- H3. Test delle API: client, autenticazione, casi di errore
- H4. Test che verificano il numero di query (`assertNumQueries`/`django_assert_num_queries`)

## I. Operatività
- I1. Caching (per vista, per frammento, low-level)
- I2. File statici e media
- I3. Logging, gestione degli errori in produzione
- I4. Deploy di base: WSGI/ASGI, gunicorn/uvicorn, database, migrazioni in deploy
