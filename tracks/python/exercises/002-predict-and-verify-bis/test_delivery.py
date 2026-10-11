"""Completeness checks for exercise 002.

These tests do NOT check whether the predictions are correct, and they never
run the snippets. They check that the delivery is complete and internally
consistent: the design note is filled in the required form, every snippet has
per-line explanations, a prediction, a confidence level, a verification, a
structured gap analysis with an "Atteso" line, and the derived counts match
what is written in the file.
"""
import re
from pathlib import Path

import pytest

HERE = Path(__file__).parent
SNIPPET_IDS = [1, 2, 3, 4, 5]
MIN_ROWS = {1: 6, 2: 5, 3: 6, 4: 4, 5: 4}
MIN_ROW_CHARS = 20
MIN_TEXT_CHARS = 40

COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
FIELD_RE = re.compile(
    r"^\*\*(?P<label>[^*\n]+?):\*\*[ \t]*(?P<body>.*?)(?=^\*\*|\Z)", re.DOTALL | re.MULTILINE
)
FENCE_RE = re.compile(r"```[^\n]*\n(.*?)```", re.DOTALL)


def _clean(text: str) -> str:
    return COMMENT_RE.sub("", text).replace("---", "").strip()


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _blocks(text: str) -> list[str]:
    return [block.strip() for block in FENCE_RE.findall(text)]


def _parse_sections(path: Path) -> dict[str, dict[str, str]]:
    """Return {section title: {field label (lowercase): raw body}}. Comments kept."""
    text = path.read_text(encoding="utf-8")
    parts = re.split(r"^## (.+)$", text, flags=re.MULTILINE)
    sections: dict[str, dict[str, str]] = {}
    for title, body in zip(parts[1::2], parts[2::2]):
        fields = {}
        for match in FIELD_RE.finditer(body):
            fields[match.group("label").strip().lower()] = match.group("body")
        sections[title.strip()] = fields
    return sections


def _field(fields: dict[str, str], prefix: str, clean: bool = True) -> str:
    for label, body in fields.items():
        if label.startswith(prefix):
            return _clean(body) if clean else body
    return ""


@pytest.fixture(scope="module")
def sections() -> dict[str, dict[str, str]]:
    return _parse_sections(HERE / "risposte.md")


@pytest.fixture(scope="module")
def snippets(sections) -> dict[int, dict[str, str]]:
    found = {}
    for title, fields in sections.items():
        match = re.match(r"Snippet (\d+)", title)
        if match:
            found[int(match.group(1))] = fields
    return found


def _confidence(fields) -> int | None:
    value = _field(fields, "sicurezza")
    return int(value) if re.fullmatch(r"[1-5]", value) else None


def _doubtful(fields) -> bool:
    confidence = _confidence(fields)
    text = (_field(fields, "righe") + " " + _field(fields, "previsione")).lower()
    return confidence is None or confidence <= 3 or "non so" in text


# ---------------------------------------------------------------- design.md


def _design_sections() -> dict[str, str]:
    text = (HERE / "design.md").read_text(encoding="utf-8")
    result = {}
    for section in re.split(r"^## ", text, flags=re.MULTILINE)[1:]:
        title, _, body = section.partition("\n")
        result[title.strip()] = body
    return result


def _design_body(prefix: str) -> str:
    for title, body in _design_sections().items():
        if title.lower().startswith(prefix):
            return _clean(body)
    return ""


def _all_snippet_code() -> str:
    return _norm(" ".join(p.read_text(encoding="utf-8") for p in sorted((HERE / "snippets").glob("*.py"))))


def test_design_operations_seen():
    body = _design_body("cosa vedo")
    spans = {_norm(s) for s in re.findall(r"`([^`\n]+)`", body)}
    real = [s for s in spans if s and s in _all_snippet_code()]
    assert len(real) >= 4, (
        "design.md, 'Cosa vedo negli snippet': write at least 4 different operations or lines, "
        "each in `backticks`, copied from the snippets"
    )


def test_design_model_is_a_question_about_the_line():
    body = _design_body("il modello").lower()
    assert "?" in body, "design.md, 'Il modello': write it as a question to ask about each line (with a question mark)"
    assert "etichett" in body and "oggett" in body, (
        "design.md, 'Il modello': use the words 'etichetta' and 'oggetto' (is this line moving a label or changing an object?)"
    )


def test_design_has_two_concrete_doubts_with_experiments():
    body = _design_body("dubbi concreti")
    items = re.split(r"^\s*\d+[.)]\s+", body, flags=re.MULTILINE)[1:]
    valid = 0
    code = _all_snippet_code()
    for item in items:
        spans = [_norm(s) for s in re.findall(r"`([^`\n]+)`", item)]
        has_line = any(s and s in code for s in spans)
        match = re.search(r"esperimento[^:\n]*:\s*(.+)", item, flags=re.IGNORECASE | re.DOTALL)
        has_experiment = bool(match and len(match.group(1).strip()) >= 20)
        valid += has_line and has_experiment
    assert valid >= 2, (
        "design.md, 'Dubbi concreti': at least 2 numbered doubts, each quoting a line from the snippets in "
        "`backticks` and an 'Esperimento ...: <what you will try and expect>' of at least 20 characters"
    )


@pytest.mark.parametrize("prefix", ["come userò", "tempo"])
def test_design_other_sections(prefix):
    if prefix == "tempo":
        title = next(t for t in _design_sections() if t.lower().startswith("tempo"))
        assert "__" not in title, "design.md: fill in the 'Tempo' line (inizio / fine / indizi)"
    else:
        assert len(_design_body(prefix)) >= 15, f"design.md: section '{prefix}' is empty"


# --------------------------------------------------------------- risposte.md


def test_timing_header_is_filled():
    text = (HERE / "risposte.md").read_text(encoding="utf-8")
    for label in (
        "Previsioni terminate alle",
        "Verifica iniziata alle",
        "Minuti di lavoro effettivo",
        "Minuti persi su ambiente",
    ):
        match = re.search(rf"^{label}[^:\n]*:[ \t]*(.*)$", text, flags=re.MULTILINE)
        assert match and match.group(1).strip(), f"missing: {label}"


@pytest.mark.parametrize("snippet_id", SNIPPET_IDS)
def test_code_in_risposte_matches_snippet_file(snippets, snippet_id):
    fields = snippets.get(snippet_id, {})
    blocks = _blocks(_field(fields, "codice", clean=False))
    expected = (HERE / "snippets" / f"s0{snippet_id}.py").read_text(encoding="utf-8")
    assert blocks and _norm(blocks[0]) == _norm(expected), (
        f"snippet {snippet_id}: the code block in risposte.md was modified or removed; restore it"
    )


@pytest.mark.parametrize("snippet_id", SNIPPET_IDS)
def test_line_explanations(snippets, snippet_id):
    fields = snippets.get(snippet_id, {})
    body = _field(fields, "righe", clean=False)
    rows = re.findall(r"^\s*[-*]\s+`.+?`.*?→(.*)$", body, flags=re.MULTILINE)
    rows = [_clean(row) for row in rows]
    assert len(rows) >= MIN_ROWS[snippet_id], (
        f"snippet {snippet_id}: at least {MIN_ROWS[snippet_id]} lines must be explained (keep the '→' format)"
    )
    bad = [
        row
        for row in rows
        if len(row) < MIN_ROW_CHARS
        or not ("etichett" in row.lower() or "oggett" in row.lower())
        or "dopo" not in row.lower()
    ]
    assert not bad, (
        f"snippet {snippet_id}: {len(bad)} line(s) not in the form "
        f"'sposta un'etichetta / modifica un oggetto (quale); dopo: <nomi sullo stesso oggetto>'"
    )


@pytest.mark.parametrize("snippet_id", SNIPPET_IDS)
def test_prediction_is_exact_output_block(snippets, snippet_id):
    fields = snippets.get(snippet_id, {})
    blocks = _blocks(_field(fields, "previsione", clean=False))
    assert blocks and len(blocks[0]) >= 3, f"snippet {snippet_id}: prediction missing (exact output in a code block)"


@pytest.mark.parametrize("snippet_id", SNIPPET_IDS)
def test_confidence_declared(snippets, snippet_id):
    assert _confidence(snippets.get(snippet_id, {})) is not None, (
        f"snippet {snippet_id}: confidence must be a single digit 1-5"
    )


@pytest.mark.parametrize("snippet_id", SNIPPET_IDS)
def test_alternative_hypothesis_when_confidence_low(snippets, snippet_id):
    fields = snippets.get(snippet_id, {})
    confidence = _confidence(fields)
    alternative = _field(fields, "ipotesi alternativa", clean=False)
    assert _clean(alternative), f"snippet {snippet_id}: 'Ipotesi alternativa' is empty (write 'no' if confidence is 4 or 5)"
    if confidence is not None and confidence <= 3:
        alt_blocks = _blocks(alternative)
        assert len(_clean(alternative)) >= 30 and alt_blocks, (
            f"snippet {snippet_id}: confidence {confidence} requires a second explanation and, in a code "
            f"block, the exact output it would produce"
        )
        prediction = _blocks(_field(fields, "previsione", clean=False))
        assert not prediction or _norm(alt_blocks[0]) != _norm(prediction[0]), (
            f"snippet {snippet_id}: the alternative hypothesis gives the same output as the prediction, "
            f"so it is not an alternative"
        )


@pytest.mark.parametrize("snippet_id", SNIPPET_IDS)
def test_verification_fields(snippets, snippet_id):
    fields = snippets.get(snippet_id, {})
    blocks = _blocks(_field(fields, "output ottenuto", clean=False))
    assert blocks and blocks[0], f"snippet {snippet_id}: paste the real output in 'Output ottenuto' (code block)"
    assert len(_field(fields, "righe in cui")) >= 3, (
        f"snippet {snippet_id}: write which lines differ between prediction and output (or 'nessuna')"
    )
    assert _field(fields, "dopo la verifica").lower() in {"si", "sì", "no"}, (
        f"snippet {snippet_id}: write si or no after verifying"
    )


@pytest.mark.parametrize("snippet_id", SNIPPET_IDS)
def test_structured_gap_analysis(snippets, snippet_id):
    fields = snippets.get(snippet_id, {})
    if _field(fields, "dopo la verifica").lower() != "no":
        return
    assert len(_field(fields, "scarto - spiegazione")) >= MIN_TEXT_CHARS, (
        f"snippet {snippet_id}: 'Scarto - spiegazione' missing (what you thought, what happens, why)"
    )
    experiment = _field(fields, "scarto - esperimento", clean=False)
    experiment_blocks = _blocks(experiment)
    assert experiment_blocks, f"snippet {snippet_id}: 'Scarto - esperimento' needs a code block with the REPL code"
    expected = _field(fields, "scarto - atteso")
    lines = re.findall(r"^\s*(?:[-*]\s*)?Atteso\b.*$", expected, flags=re.MULTILINE | re.IGNORECASE)
    assert len(lines) >= len(experiment_blocks), (
        f"snippet {snippet_id}: one 'Atteso: <output> perché <spiegazione>' line is required for each "
        f"experiment block ({len(experiment_blocks)}), written before running"
    )
    assert all("perch" in line.lower() for line in lines), (
        f"snippet {snippet_id}: every 'Atteso' line needs a 'perché' with the explanation under test"
    )
    obtained = _blocks(_field(fields, "scarto - ottenuto", clean=False))
    assert obtained and obtained[0], f"snippet {snippet_id}: paste what the experiment printed in 'Scarto - ottenuto'"
    holds = _field(fields, "scarto - la spiegazione regge").lower()
    assert holds in {"si", "sì", "no"}, f"snippet {snippet_id}: 'la spiegazione regge' must be si or no"
    if holds == "no":
        assert len(_field(fields, "scarto - nuova spiegazione")) >= MIN_TEXT_CHARS, (
            f"snippet {snippet_id}: the explanation did not hold, so write the new one "
            f"(with its experiment and its 'Atteso' line)"
        )


def test_every_repl_block_has_an_atteso_line():
    text = (HERE / "risposte.md").read_text(encoding="utf-8")
    text = COMMENT_RE.sub("", text)
    repl_blocks = [b for b in _blocks(text) if b.lstrip().startswith(">>>")]
    atteso_lines = re.findall(r"^\s*(?:[-*]\s*)?Atteso:", text, flags=re.MULTILINE)
    assert len(repl_blocks) <= len(atteso_lines), (
        f"{len(repl_blocks)} REPL blocks pasted but only {len(atteso_lines)} 'Atteso:' lines: "
        f"each run needs its line written before"
    )


def test_derived_estimate(sections, snippets):
    fields = sections.get("Chiusura delle previsioni", {})
    declared = _field(fields, "snippet con almeno un")
    estimate = _field(fields, "stima dei giusti")
    assert re.fullmatch(r"\d+", declared), "Chiusura: write the number of snippets with doubts"
    assert re.fullmatch(r"\d+", estimate), "Chiusura: write your estimate of correct snippets (a number)"
    actual = sum(_doubtful(snippets.get(i, {})) for i in SNIPPET_IDS)
    assert int(declared) == actual, (
        f"Chiusura: you wrote {declared} snippets with doubts, but your own fields (confidence <= 3 or 'non so') "
        f"give a different number: count again from the file"
    )
    assert int(estimate) <= len(SNIPPET_IDS) - int(declared), (
        "Chiusura: snippets with doubts count as wrong, so the estimate cannot exceed 5 minus that number"
    )


def test_synthesis_and_transfer(sections):
    fields = sections.get("Sintesi e prova di trasferimento", {})
    for prefix in ("il mio errore", "un caso di questo esercizio"):
        assert len(_field(fields, prefix)) >= MIN_TEXT_CHARS, f"Sintesi: '{prefix}...' missing or too short"
    rule = _field(fields, "la mia regola")
    assert len(rule) >= MIN_TEXT_CHARS and "?" in rule, (
        "Sintesi: 'La mia regola' must be written as a question to ask about a line, with what you do depending on the answer"
    )
    code = _blocks(_field(fields, "riga nuova - codice", clean=False))
    expected = (HERE / "snippets" / "transfer.py").read_text(encoding="utf-8")
    assert code and _norm(code[0]) == _norm(expected), "Sintesi: the 'Riga nuova' code block was modified"
    explanation = _field(fields, "riga nuova - spiegazione").lower()
    assert len(explanation) >= 60 and "etichett" in explanation and "oggett" in explanation, (
        "Sintesi: explain the new line in the 'etichetta / oggetto' form before predicting"
    )
    prediction = _blocks(_field(fields, "riga nuova - previsione", clean=False))
    assert prediction and prediction[0], "Sintesi: prediction of the new line missing (code block)"
    assert re.fullmatch(r"[1-5]", _field(fields, "riga nuova - sicurezza")), "Sintesi: confidence 1-5 for the new line"
    obtained = _blocks(_field(fields, "riga nuova - output ottenuto", clean=False))
    assert obtained and obtained[0], "Sintesi: paste the real output of the new line"
    holds = _field(fields, "la regola ha retto").lower()
    assert holds in {"si", "sì", "no"}, "Sintesi: 'La regola ha retto' must be si or no"
    if holds == "no":
        assert len(_field(fields, "se no")) >= MIN_TEXT_CHARS, "Sintesi: the rule did not hold, write how you change it"
