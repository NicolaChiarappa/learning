# Review — 004 — 2026-10-28

## Esito
Test base: 6/6 + regressione 1/1 | Test nascosti: 12/12 (sull'originale 3/12: discriminano) | Indizi: 3 (liv. 1-2) + 2 risposte di teoria
| Correttezza 4 | Casi limite 3 | Design 3 | Leggibilità 2 | Idiomaticità 2 | Processo 2 |

R7 verificato dal reviewer in una cartella temporanea: `test_regression.py` è rosso sull'originale (`assert not [] is []`) e **resta rosso** con la pezza `cart["items"] = cart["items"] + [...]` su `add_item` (mentre i test base 1-3 diventano verdi). Il test fa ciò che deve. Correzione minima: sentinella `None` con `is None` su entrambi i default; `created_at=0.0` viene rispettato, `__defaults__` è `(None, None)`. Calibrazione non disponibile: niente previsione test per test, niente stima dei nascosti, niente copertura R1-R7 (scelta di Nick).

## Il punto più importante
Due volte in questo esercizio hai avuto il modello giusto e non l'hai confrontato con ciò che avevi appena scritto.
1. In "Prima di iniziare" individui subito che `created_at=time.time()` viene valutato una volta (la trappola principale, vista prima di eseguire). Poi come correzione proponi `items=list()`: stessa riga, stesso meccanismo, e ti servono due domande per vederlo.
2. Sempre in "Prima di iniziare" scrivi che "le funzioni di modifica come rimozione di items" toccano tutti i carrelli. `empty_cart` fa `cart["items"] = []`: il test 5 è verde sull'originale. In D2 rispondi giusto, senza esitare, ma la frase di apertura non è mai stata ripresa. È lo stesso errore di `close_row` in 003, ed è rimasto nascosto per la stessa ragione: la previsione test per test (in cui il test 5 l'avrebbe fatto emergere) non è stata scritta, per la terza volta.
Non ti manca il meccanismo. Ti manca il passo "quello che ho scritto prima regge ancora?". Senza quello passi da un modello all'altro senza accorgertene.

## Osservazioni sul codice
- `cart.py` r.12: la docstring di `new_cart` è stata cancellata e non ripristinata. Era il contratto (cosa sono `items` e `created_at`). Ora che `None` ha un significato ("non passato"), è proprio lì che andava scritto.
- `test_regression.py` r.5: `test_new_cart` non dice quale comportamento protegge. Il nome di un test di regressione è la prima cosa che legge chi lo vedrà fallire.
- `test_regression.py` r.9: `assert not a is b` funziona solo perché `is` lega più forte di `not`. Python ha un operatore apposta (PEP 8). Sai dire perché il tuo funziona? Ti servirà nell'esercizio sulla precedenza.
- `total_cents`: rosso attribuito a "il test non legge gli apici"; ti servono tre domande per leggere `'750'` come un `str`. E006 ancora aperto.

## Domande per te
- Prima di correggere: la riga che sto per scrivere ha lo stesso difetto di quella che ho appena criticato?
- Cosa avevo scritto in "Prima di iniziare" su questa funzione, e l'output lo conferma?

## Esito modulo
PASSATO CON RISERVA. Questo esercizio copre la parte "corregge un default mutabile in codice non suo spiegando il meccanismo" del criterio di uscita di M01, ma è arrivata con un aiuto su `list()`. La riserva riguarda il processo: la previsione dei test base è stata saltata per la terza volta.
