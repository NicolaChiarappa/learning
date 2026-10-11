"""Completeness checks for exercise 003.

They never judge whether an answer is correct and never run the exercise code
(only an import for the interface check). They check that the delivery is
complete and internally consistent: every field is filled, every experiment has
two different outcomes written before the output, the pasted output matches the
outcome declared, the rules are ticked, the numbers agree with each other.

Tests with "gate" in the name check design.md only: they must be green before
any change to seating.py. Run them with:  pytest -q test_delivery.py -k gate
"""
import ast
import inspect
import re
from pathlib import Path

import pytest

HERE = Path(__file__).parent
MODULE_FUNCTIONS = ("build_hall", "book_seat", "add_seat", "close_row", "free_per_row")
RULE_IDS = list(range(1, 10))

COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
FIELD_RE = re.compile(
    r"^\*\*(?P<label>[^*\n]+?):\*\*[ \t]*(?P<body>.*?)(?=^\*\*|\Z)", re.DOTALL | re.MULTILINE
)
FENCE_RE = re.compile(r"```[^\n]*\n(.*?)```", re.DOTALL)


# ------------------------------------------------------------------ helpers


def _clean(text: str) -> str:
    return COMMENT_RE.sub("", text).replace("---", "").strip()


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _flat(text: str) -> str:
    """Normalise for comparing outputs: no fences, no backticks, single spaces."""
    text = re.sub(r"```\w*", "", text).replace("`", "")
    return _norm(text)


def _blocks(text: str) -> list[str]:
    return [block.strip() for block in FENCE_RE.findall(text)]


def _split_sections(text: str) -> dict[str, str]:
    parts = re.split(r"^## (.+)$", text, flags=re.MULTILINE)
    return {title.strip(): body for title, body in zip(parts[1::2], parts[2::2])}


def _fields(body: str) -> dict[str, str]:
    return {m.group("label").strip().lower(): m.group("body") for m in FIELD_RE.finditer(body)}


def _field(fields: dict[str, str], prefix: str, clean: bool = True) -> str:
    for label, body in fields.items():
        if label.startswith(prefix):
            return _clean(body) if clean else body
    return ""


def _section(sections: dict[str, str], prefix: str) -> str:
    for title, body in sections.items():
        if title.lower().startswith(prefix.lower()):
            return body
    return ""


def _test_names() -> set[str]:
    names: set[str] = set()
    for filename in ("test_seating.py", "test_regression.py"):
        path = HERE / filename
        if path.exists():
            tree = ast.parse(path.read_text(encoding="utf-8"))
            names |= {n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name.startswith("test_")}
    return names


@pytest.fixture(scope="module")
def design() -> dict[str, str]:
    return _split_sections((HERE / "design.md").read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def answers_text() -> str:
    return (HERE / "risposte.md").read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def answers(answers_text) -> dict[str, str]:
    return _split_sections(answers_text)


def _check_experiment(fields: dict[str, str], where: str, need_output: bool, need_is: bool = False) -> None:
    """Shared checks for an experiment with two outcomes written before running."""
    code = _blocks(_field(fields, "codice", clean=False))
    assert code and code[0], f"{where}: campo 'Codice' vuoto (blocco di codice con le righe dell'esperimento)"
    if need_is:
        assert re.search(r"\bis\b", code[0]) and "build_hall(" in code[0], (
            f"{where}: il codice dell'esperimento deve usare build_hall e almeno un confronto con `is`"
        )
    right = _flat(_field(fields, "se ho ragione"))
    wrong = _flat(_field(fields, "se ho torto"))
    assert right, f"{where}: campo 'Se ho ragione' vuoto (output esatto atteso)"
    assert wrong, f"{where}: campo 'Se ho torto' vuoto (output esatto, diverso da 'Se ho ragione')"
    assert right != wrong, f"{where}: 'Se ho ragione' e 'Se ho torto' sono uguali, quindi l'esperimento non decide niente"
    if not need_output:
        return
    obtained_blocks = _blocks(_field(fields, "output ottenuto", clean=False))
    assert obtained_blocks and obtained_blocks[0], f"{where}: campo 'Output ottenuto' vuoto (incolla dal terminale)"
    obtained = _flat(obtained_blocks[0])
    outcome = _field(fields, "è uscito").lower()
    assert outcome in {"ragione", "torto", "nessuno dei due"}, (
        f"{where}: campo 'È uscito' deve essere una sola parola tra ragione / torto / nessuno dei due"
    )
    expected = {"ragione": right, "torto": wrong}.get(outcome)
    if expected is not None:
        assert obtained == expected, (
            f"{where}: hai scritto che e' uscito '{outcome}' ma l'output incollato non coincide con quella riga"
        )
    else:
        assert obtained not in {right, wrong}, (
            f"{where}: hai scritto 'nessuno dei due' ma l'output incollato coincide con una delle due righe"
        )


# ---------------------------------------------------- design.md: the gate


def test_gate_positions_and_lists(design):
    fields = _fields(_section(design, "1."))
    text = _field(fields, "posizioni e liste")
    missing = [p for p in ("hall[0]", "hall[1]", "hall[2]") if p not in text]
    assert not missing and len(text) >= 60, (
        "design.md, sezione 1, campo 'Posizioni e liste': scrivi hall[0], hall[1] e hall[2] con la lista che ciascuna guarda"
    )


def test_gate_edge_cases_from_the_rules(design):
    body = _clean(_section(design, "2."))
    lines = [ln for ln in body.splitlines() if ln.strip().startswith("-")]
    good = 0
    for line in lines:
        spans = re.findall(r"`([^`\n]+)`", line)
        has_call = any("(" in s and any(f in s for f in MODULE_FUNCTIONS) for s in spans)
        has_rule = re.search(r"\bR[1-9]\b", line) or "non lo dice" in line.lower()
        good += bool(has_call and "→" in line and has_rule)
    assert good >= 3, (
        "design.md, sezione 2: servono almeno 3 righe `- `chiamata(...)` → cosa deve succedere (Rn)` oppure 'la consegna non lo dice'"
    )


def test_gate_predicted_red_tests(design):
    text = _field(_fields(_section(design, "3.")), "test che prevedo rossi")
    assert text, "design.md, sezione 3, campo 'Test che prevedo rossi': vuoto (nomi dei test, oppure 'nessuno')"
    named = set(re.findall(r"test_\w+", text))
    unknown = named - _test_names()
    assert named or text.lower().strip(". ") == "nessuno", (
        "design.md, sezione 3: scrivi i nomi esatti dei test di test_seating.py, oppure 'nessuno'"
    )
    assert not unknown, f"design.md, sezione 3: questi nomi non esistono in test_seating.py: {sorted(unknown)}"


def test_gate_hypotheses_are_two_and_different(design):
    fields = _fields(_section(design, "4."))
    mine = _field(fields, "ipotesi sulla causa")
    rival = _field(fields, "ipotesi rivale")
    assert len(mine) >= 20, "design.md, sezione 4, campo 'Ipotesi sulla causa': una frase con funzione e riga (almeno 20 caratteri)"
    assert len(rival) >= 20, "design.md, sezione 4, campo 'Ipotesi rivale': una frase con un'altra causa plausibile (almeno 20 caratteri)"
    assert _norm(mine).lower() != _norm(rival).lower(), "design.md, sezione 4: le due ipotesi sono uguali"


def test_gate_experiment_has_two_different_outcomes(design):
    _check_experiment(_fields(_section(design, "4.")), "design.md, sezione 4", need_output=False, need_is=True)


# ----------------------------------------------- design.md: after running


def test_design_experiment_result(design):
    _check_experiment(_fields(_section(design, "4.")), "design.md, sezione 4", need_output=True, need_is=True)


# ------------------------------------------------------------- risposte.md


def test_time_header_is_filled(answers_text):
    for label in (
        "Ora di inizio",
        "Punto di controllo",
        "Ora di fine",
        "Minuti persi su ambiente",
    ):
        match = re.search(rf"^{label}[^:\n]*:[ \t]*(.*)$", answers_text, flags=re.MULTILINE)
        assert match and len(match.group(1).strip()) >= 2, f"risposte.md, intestazione: '{label}' vuoto"


def _red_names(block: str) -> set[str]:
    return set(re.findall(r"FAILED\s+\S+::(\w+)", block))


def test_a_base_output_shows_red_tests(answers):
    fields = _fields(_section(answers, "A."))
    blocks = _blocks(_field(fields, "output di", clean=False))
    assert blocks and blocks[0], "risposte.md, sezione A, campo 'Output di pytest': vuoto (incolla dal terminale)"
    assert "failed" in blocks[0].lower(), (
        "risposte.md, sezione A: l'output incollato non mostra test rossi (va lanciato sul codice originale)"
    )


def test_a_prediction_gap_declared(answers):
    text = _field(_fields(_section(answers, "A.")), "previsioni di design.md sbagliate")
    assert len(text) >= 6, "risposte.md, sezione A, campo 'Previsioni di design.md sbagliate': vuoto (nomi dei test, oppure 'nessuna')"


def test_a_every_red_test_has_a_cause(answers):
    fields = _fields(_section(answers, "A."))
    blocks = _blocks(_field(fields, "output di", clean=False))
    red = _red_names(blocks[0]) if blocks else set()
    causes = _field(fields, "cause dei test rossi")
    assert len(causes) >= 30, "risposte.md, sezione A, campo 'Cause dei test rossi, raggruppate': vuoto o troppo corto"
    missing = sorted(name for name in red if name not in causes)
    assert not missing, f"risposte.md, sezione A, campo 'Cause dei test rossi': mancano questi test rossi: {missing}"


def test_b_who_looks_at_what(answers):
    fields = _fields(_section(answers, "B."))
    original = _flat((HERE / "original" / "seating_original.py").read_text(encoding="utf-8"))
    body = _field(fields, "righe", clean=False)
    rows = [ln for ln in _clean(body).splitlines() if ln.strip().startswith("-")]
    good = 0
    for row in rows:
        spans = [_flat(s) for s in re.findall(r"`([^`\n]+)`", row)]
        low = row.lower()
        in_code = any(s and s in original for s in spans)
        good += bool(in_code and "→" in row and "dopo" in low and ("etichett" in low or "oggett" in low) and "hall[" in row)
    assert good >= 3, (
        "risposte.md, sezione B, campo 'Righe': servono 3 voci `riga` → sposta un'etichetta / modifica un oggetto; dopo: posizioni di hall[...]"
    )
    assert len(_field(fields, "confronto")) >= 80, (
        "risposte.md, sezione B, campo 'Confronto tra close_row e add_seat': vuoto o troppo corto (almeno 2-3 frasi)"
    )


def test_c_regression_test_exists_and_was_red(answers):
    path = HERE / "test_regression.py"
    assert path.exists(), "manca il file test_regression.py (sezione C)"
    text = path.read_text(encoding="utf-8")
    assert re.search(r"^def test_\w+", text, flags=re.MULTILINE) and "assert" in text, (
        "test_regression.py: serve almeno una funzione test_ con un assert"
    )
    blocks = _blocks(_field(_fields(_section(answers, "C.")), "output prima della correzione", clean=False))
    assert blocks and blocks[0], "risposte.md, sezione C, campo 'Output prima della correzione': vuoto"
    low = blocks[0].lower()
    assert "test_regression.py" in blocks[0] and "failed" in low, (
        "risposte.md, sezione C: l'output incollato deve mostrare un test di test_regression.py rosso"
    )


def test_d_experiment(answers):
    fields = _fields(_section(answers, "D."))
    assert len(_field(fields, "ipotesi")) >= 20, "risposte.md, sezione D, campo 'Ipotesi': una frase con risposta e motivo (almeno 20 caratteri)"
    _check_experiment(fields, "risposte.md, sezione D", need_output=True)
    assert len(_field(fields, "cosa ne concludo")) >= 60, (
        "risposte.md, sezione D, campo 'Cosa ne concludo per la correzione': vuoto o troppo corto (2-3 frasi)"
    )


def test_e_choice_has_an_alternative(answers):
    text = _field(_fields(_section(answers, "E.")), "scelta").lower()
    assert len(text) >= 60 and "invece di" in text and "perch" in text, (
        "risposte.md, sezione E, campo 'Scelta': scrivi 'ho fatto X invece di Y perché ...' (almeno 60 caratteri)"
    )


def test_f_design_retrospective(answers, design):
    fields = _fields(_section(answers, "F."))
    original = _flat((HERE / "original" / "seating_original.py").read_text(encoding="utf-8"))
    spans = [_flat(s) for s in re.findall(r"`([^`\n]+)`", _field(fields, "riga del codice originale"))]
    assert any(s and s in original for s in spans), (
        "risposte.md, sezione F, campo 'Riga del codice originale': copia tra apici inversi una riga di original/seating_original.py"
    )

    def squash(text: str) -> str:
        return _norm(re.sub(r"[`\"'«»“”]", "", _clean(text))).lower()

    quote = squash(_field(fields, "cosa avevo scritto"))
    design_text = squash(" ".join(design.values()))
    assert len(quote) >= 20 and quote in design_text, (
        "risposte.md, sezione F, campo 'Cosa avevo scritto in design.md': la citazione deve essere copiata parola per parola da design.md"
    )
    holds = _field(fields, "reggeva").lower()
    assert holds in {"si", "sì", "no"}, "risposte.md, sezione F, campo 'Reggeva': una sola parola, si oppure no"
    assert len(_field(fields, "se no")) >= (40 if holds == "no" else 10), (
        "risposte.md, sezione F, campo 'Se no, cosa cambia nel mio modello': "
        + ("spiega cosa è cambiato (almeno 40 caratteri)" if holds == "no" else "scrivi 'nessun cambiamento'")
    )


def test_g_reading_a_failed_test(answers):
    fields = _fields(_section(answers, "G."))
    assert "assert" in _field(fields, "riga assert"), (
        "risposte.md, sezione G, campo 'Riga assert copiata da pytest': copia la riga 'E ... assert ...' dall'output"
    )
    assert len(_field(fields, "cosa confronta")) >= 80, (
        "risposte.md, sezione G, campo 'Cosa confronta pytest ...': vuoto o troppo corto (almeno 2 frasi)"
    )
    original = _flat((HERE / "original" / "seating_original.py").read_text(encoding="utf-8"))
    spans = [_flat(s) for s in re.findall(r"`([^`\n]+)`", _field(fields, "riga di seating.py"))]
    assert any(s and s in original for s in spans), (
        "risposte.md, sezione G, campo 'Riga di seating.py che causa la differenza': copia tra apici inversi una riga del codice originale"
    )


def _lines_left_red(answers) -> dict[str, str]:
    body = _clean(_section(answers, "Test lasciati rossi"))
    result = {}
    for line in body.splitlines():
        match = re.match(r"\s*[-*]\s*`?(test_\w+)`?\s*→\s*(.+)", line)
        if match:
            result[match.group(1)] = match.group(2).strip()
    return result


def test_h_final_run_is_green_or_justified(answers):
    blocks = _blocks(_field(_fields(_section(answers, "H.")), "output di", clean=False))
    assert blocks and blocks[0], "risposte.md, sezione H, campo 'Output di pytest': vuoto (incolla dal terminale)"
    output = blocks[0]
    assert re.search(r"\d+ passed", output), "risposte.md, sezione H: nell'output incollato non compare '... passed'"
    red = _red_names(output)
    if red:
        left = _lines_left_red(answers)
        unjustified = sorted(n for n in red if len(left.get(n, "")) < 20 or "perch" not in left.get(n, "").lower())
        assert not unjustified, (
            f"test rossi senza riga '- nome_test → lo lascio rosso perché ...' in fondo a risposte.md: {unjustified}"
        )


def test_left_red_section_is_filled(answers):
    body = _clean(_section(answers, "Test lasciati rossi"))
    assert body.lower().strip(". ") == "nessuno" or _lines_left_red(answers), (
        "risposte.md, sezione 'Test lasciati rossi e perché': scrivi 'nessuno' oppure una riga per test"
    )


RULE_RE = re.compile(
    r"R(?P<n>\d)\s*→\s*copertura:\s*(?P<cov>[^|]+?)\s*\|\s*rispetto:\s*(?P<ok>si|sì|no|non so)\b", re.IGNORECASE
)


def _rules(answers) -> dict[int, tuple[str, str]]:
    body = _field(_fields(_section(answers, "I.")), "regole")
    return {int(m.group("n")): (m.group("cov").strip(), m.group("ok").lower()) for m in RULE_RE.finditer(body)}


def test_i_rules_are_ticked(answers):
    rules = _rules(answers)
    missing = [n for n in RULE_IDS if n not in rules]
    assert not missing, f"risposte.md, sezione I, campo 'Regole': righe mancanti o non compilate per R{missing}"
    known = _test_names()
    for n, (coverage, _) in rules.items():
        if coverage.lower().strip(". ") == "nessuna":
            continue
        names = [c.strip().strip("`") for c in coverage.split(",")]
        bad = [c for c in names if c not in known]
        assert not bad, f"risposte.md, sezione I, R{n}: test inesistenti {bad}; scrivi nomi di test_seating.py / test_regression.py o 'nessuna'"


def test_i_hidden_estimate_is_coherent(answers):
    text = _field(_fields(_section(answers, "I.")), "test nascosti")
    assert re.fullmatch(r"\d+", text) and 0 <= int(text) <= 10, (
        "risposte.md, sezione I, campo 'Test nascosti che prevedo di passare': un numero da 0 a 10"
    )
    doubtful = sum(1 for _, ok in _rules(answers).values() if ok in {"no", "non so"})
    assert int(text) <= max(0, 10 - doubtful), (
        f"risposte.md, sezione I: hai {doubtful} regole con 'no' o 'non so', quindi non puoi prevedere più di {10 - doubtful} test nascosti su 10"
    )


def test_j_synthesis_rule_is_a_question_with_consequence(answers):
    text = _field(_fields(_section(answers, "J.")), "regola")
    low = text.lower()
    assert len(text) >= 60 and "?" in text and re.search(r"\bse\b", low), (
        "risposte.md, sezione J, campo 'Regola': una domanda (con '?') e cosa concludi a seconda della risposta ('se ...')"
    )


def test_k_optional_extension_is_done_or_cut(answers):
    fields = _fields(_section(answers, "K."))
    state = _field(fields, "stato").lower()
    assert state in {"fatta", "tagliata"}, "risposte.md, sezione K, campo 'Stato': scrivi fatta oppure tagliata"
    if state == "fatta":
        _check_experiment(fields, "risposte.md, sezione K", need_output=True)


def test_interface_unchanged():
    import seating

    expected = {
        "build_hall": ["rows", "seats_per_row"],
        "book_seat": ["hall", "row", "seat"],
        "add_seat": ["hall", "row"],
        "close_row": ["hall", "row"],
        "free_per_row": ["hall"],
    }
    for name, params in expected.items():
        assert hasattr(seating, name), f"seating.py: manca la funzione {name}"
        assert list(inspect.signature(getattr(seating, name)).parameters) == params, (
            f"seating.py: la firma di {name} è cambiata (deve restare {params}); le firme non fanno parte dell'esercizio"
        )
