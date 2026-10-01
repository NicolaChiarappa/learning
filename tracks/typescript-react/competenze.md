# Mappa competenze — TypeScript + React + Expo

Riferimento fisso per assessor e planner. Ogni area si valuta da 0 a 4.

## A. JavaScript (fondamenta)
- A1. Tipi, coercizione, `==` vs `===`, truthy/falsy, `null` vs `undefined`
- A2. Scope, closures, `let`/`const`, hoisting
- A3. `this`, arrow function vs function
- A4. Oggetti e array: spread, destructuring, immutabilità, `map`/`filter`/`reduce`
- A5. Event loop, microtask e macrotask
- A6. Promise, `async`/`await`, gestione degli errori asincroni, `Promise.all`/`allSettled`/`race`
- A7. Moduli ES (import/export)

## B. TypeScript
- B1. Tipi di base, inferenza, `type` vs `interface`
- B2. Union, intersection, narrowing (type guard, `in`, `instanceof`, discriminated union)
- B3. Generics: funzioni, tipi, vincoli (`extends`)
- B4. Utility type: `Partial`, `Pick`, `Omit`, `Record`, `ReturnType`, ecc.
- B5. `unknown` vs `any`, `never`, controlli esaustivi
- B6. Strict mode e configurazione di `tsconfig`
- B7. Tipizzare dati esterni: validazione a runtime (zod) vs tipi statici
- B8. Tipi avanzati: mapped type, conditional type, template literal type (saperli leggere)

## C. React
- C1. Componenti, JSX, props, composizione (children, render prop)
- C2. Stato: `useState`, aggiornamenti funzionali, stato derivato (e perché non duplicarlo)
- C3. `useEffect`: quando serve davvero, dipendenze, cleanup, errori tipici
- C4. Rendering: quando un componente si ri-renderizza, `key`, riconciliazione
- C5. `useMemo`, `useCallback`, `React.memo`: quando servono e quando no
- C6. `useRef`, `useReducer`, `useContext`
- C7. Custom hook: estrarre logica riusabile
- C8. Form: componenti controllati, validazione (react-hook-form)
- C9. Stato del server vs stato del client; TanStack Query (cache, invalidazione, mutation)
- C10. Gestione dello stato globale (Context, Zustand): quando serve

## D. React Native ed Expo
- D1. Differenze tra React web e React Native: componenti core, layout con Flexbox, stili
- D2. Expo: progetto, Expo Go vs development build, configurazione (`app.json`/`app.config`)
- D3. Navigazione con Expo Router: stack, tab, route dinamiche, layout
- D4. Liste performanti (`FlatList`, `FlashList`), immagini
- D5. Storage locale (AsyncStorage, SecureStore, SQLite); funzionamento offline
- D6. Permessi e API native (fotocamera, notifiche, posizione)
- D7. Differenze tra iOS, Android e web; codice specifico per piattaforma
- D8. Build e distribuzione con EAS; aggiornamenti OTA
- D9. Accessibilità di base su mobile

## E. Comunicazione con il backend
- E1. Chiamate HTTP (fetch), gestione degli errori, timeout, retry
- E2. Autenticazione da app mobile: token, refresh, archiviazione sicura
- E3. Tipi condivisi con il backend (generazione da OpenAPI)

## F. Testing
- F1. Vitest/Jest: test di funzioni pure e hook
- F2. React Native Testing Library: testare il comportamento, non l'implementazione
- F3. Mock delle chiamate di rete (MSW o simili)

## G. Design e qualità (trasversale)
- G1. Struttura del progetto per feature; separazione UI / logica / accesso ai dati
- G2. Componenti piccoli e componibili; dove vive lo stato
- G3. Gestione degli stati di caricamento, errore e vuoto (sempre tutti e tre)
- G4. Leggibilità e naming in TS; tipi come documentazione
- G5. Casi limite nelle UI: rete lenta o assente, doppio tap, liste vuote, testi lunghi, rotazione
- G6. Strumenti: ESLint, Prettier, TypeScript strict nel flusso di lavoro
