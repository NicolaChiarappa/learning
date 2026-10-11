"""Hidden checks for exercise 001 (written by the reviewer).

The base tests only check completeness. These check what the base tests
cannot: whether each written prediction matches the real output, whether the
declared score matches the real one, and whether every gap is backed by
evidence. Expected outputs are never hardcoded: each snippet is executed.

Run only this file:
    python -m pytest -q test_hidden.py
"""
import re
import subprocess
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).parent
ANSWERS = HERE / "risposte.md"
REQUIRED_IDS = list(range(1, 10))
WRONG_AFTER_VERIFICATION = [3, 5, 7, 9]
# Names used in Nick's own REPL experiments: Italian and by type (method rule 10).
ITALIAN_TYPE_NAMES = ["lista", "dizionario", "oggetto", "costruisci"]

SECTION_RE = re.compile(r"^## Snippet (\d+)[^\n]*\n", re.MULTILINE)
FENCE_RE = re.compile(r"\*\*Previsione:\*\*\s*```\n(.*?)```", re.DOTALL)
FIELD_RE = re.compile(
    r"^\*\*(?P<label>[^*\n]+?):\*\*[ \t]*(?P<body>.*?)(?=^\*\*|^## |\Z)",
    re.DOTALL | re.MULTILINE,
)
TOKEN_RE = re.compile(r"\w+|[^\w\s,'\"]")


def _sections() -> dict[int, str]:
    parts = SECTION_RE.split(ANSWERS.read_text(encoding="utf-8"))
    return {int(number): body for number, body in zip(parts[1::2], parts[2::2])}


def _field(snippet_id: int, prefix: str) -> str:
    for match in FIELD_RE.finditer(_sections()[snippet_id]):
        if match.group("label").strip().lower().startswith(prefix):
            return match.group("body").replace("---", "").strip()
    return ""


def _predicted_lines(snippet_id: int) -> list[str]:
    match = FENCE_RE.search(_sections()[snippet_id])
    assert match, f"snippet {snippet_id}: no fenced prediction found"
    return [line.strip() for line in match.group(1).splitlines() if line.strip()]


def _snippet_path(snippet_id: int) -> Path:
    name = "s10_challenge.py" if snippet_id == 10 else f"s{snippet_id:02d}.py"
    return HERE / "snippets" / name


def _real_lines(snippet_id: int) -> list[str]:
    completed = subprocess.run(
        [sys.executable, str(_snippet_path(snippet_id))],
        capture_output=True, text=True, check=True,
    )
    return completed.stdout.splitlines()


def _normalize(line: str) -> list[str]:
    """Ignore spacing, quote style, comma separators and letter case."""
    return TOKEN_RE.findall(line.lower())


def _matches_ignoring_form(snippet_id: int) -> bool:
    predicted = [_normalize(line) for line in _predicted_lines(snippet_id)]
    real = [_normalize(line) for line in _real_lines(snippet_id)]
    return predicted == real


# --- Correctness of the predictions -----------------------------------------

@pytest.mark.parametrize("snippet_id", REQUIRED_IDS)
def test_prediction_matches_real_output_ignoring_form(snippet_id):
    # Case: the concept is right even if quotes/spaces/case differ.
    assert [_normalize(line) for line in _predicted_lines(snippet_id)] == [
        _normalize(line) for line in _real_lines(snippet_id)
    ]


@pytest.mark.parametrize("snippet_id", REQUIRED_IDS)
def test_prediction_matches_real_output_exactly(snippet_id):
    # Case: the README asks for the EXACT output (repr quotes, list spacing,
    # print separator, True/False capitalisation).
    assert _predicted_lines(snippet_id) == _real_lines(snippet_id)


def test_optional_challenge_prediction_is_complete_and_right():
    # Case: snippet 10, last block left as "?" (a missing prediction is wrong).
    assert _matches_ignoring_form(10)


# --- Calibration -------------------------------------------------------------

def test_declared_score_matches_real_score():
    # Case: "how many out of 9 I think I got right" against the real count.
    header = ANSWERS.read_text(encoding="utf-8")
    declared = int(re.search(r"^Quanti snippet su 9[^:\n]*:\s*(\d+)", header, re.MULTILINE).group(1))
    real = sum(_matches_ignoring_form(snippet_id) for snippet_id in REQUIRED_IDS)
    assert declared == real, f"declared {declared}, real {real}"


@pytest.mark.parametrize("snippet_id", REQUIRED_IDS)
def test_self_verdict_matches_real_comparison(snippet_id):
    # Case: the si/no written after verifying must agree with the real diff.
    verdict = _field(snippet_id, "dopo la verifica").lower()
    assert (verdict in {"si", "sì"}) == _matches_ignoring_form(snippet_id)


@pytest.mark.parametrize("snippet_id", REQUIRED_IDS)
def test_high_confidence_is_never_wrong(snippet_id):
    # Case: confidence 4-5 on a wrong prediction = model wrong AND unnoticed.
    confidence = int(_field(snippet_id, "sicurezza"))
    if confidence >= 4:
        assert _matches_ignoring_form(snippet_id)


# --- Quality of explanations and gaps ---------------------------------------

@pytest.mark.parametrize("snippet_id", REQUIRED_IDS)
def test_explanation_uses_real_names_from_the_snippet(snippet_id):
    # Case (designer note): an explanation citing no real name is generic.
    code = _snippet_path(snippet_id).read_text(encoding="utf-8")
    code_only = "\n".join(line.split("#")[0] for line in code.splitlines())
    assigned = set(re.findall(r"^\s*([a-z_]+)(?:\s*,\s*[a-z_]+)*\s*(?:=|\+=)", code_only, re.MULTILINE))
    cited = {name for name in assigned if name in _field(snippet_id, "spiegazione")}
    assert len(cited) >= 2, f"real names cited: {sorted(cited)} out of {sorted(assigned)}"


@pytest.mark.parametrize("snippet_id", REQUIRED_IDS)
def test_explanation_says_label_moved_or_object_modified(snippet_id):
    # Case: the README asks, for each relevant line, "moves a label or
    # modifies an object?" The explanation must speak in those terms.
    explanation = _field(snippet_id, "spiegazione").lower()
    vocabulary = ["label", "etichett", "stesso oggetto", "nuovo oggetto", "oggetto divers", "punta", "riferiment"]
    assert any(word in explanation for word in vocabulary)


@pytest.mark.parametrize("snippet_id", WRONG_AFTER_VERIFICATION)
def test_gap_contains_a_repl_transcript(snippet_id):
    # Case (method rule 7): every gap needs evidence, not "I understood that".
    assert ">>>" in _field(snippet_id, "se no"), "no REPL evidence pasted"


@pytest.mark.parametrize("snippet_id", WRONG_AFTER_VERIFICATION)
def test_gap_states_previous_belief(snippet_id):
    # Case: "what I thought" must be explicit (credevo / avevo ipotizzato / pensavo).
    gap = _field(snippet_id, "se no").lower()
    assert any(word in gap for word in ("credevo", "ipotizzato", "pensavo"))


def test_gap_of_snippet_9_explains_the_new_key():
    # Case (designer note): the fine point of snippet 9 is that the same
    # shallow copy shares the inner lists but NOT a key added afterwards.
    assert "desserts" in _field(9, "se no")


def test_own_experiments_use_english_role_names():
    # Case (method rule 10): names in English and by role, also in REPL tests.
    text = ANSWERS.read_text(encoding="utf-8").lower()
    experiment_lines = [line for line in text.splitlines() if line.lstrip().startswith((">>>", "..."))]
    offenders = sorted({name for name in ITALIAN_TYPE_NAMES for line in experiment_lines if re.search(rf"\b{name}\d*\b", line)})
    assert not offenders, f"Italian / by-type names: {offenders}"


def test_identity_is_checked_with_id_or_is_in_every_experiment():
    # Case: design.md promised `is`, `==` and `id()` as REPL tools.
    for snippet_id in WRONG_AFTER_VERIFICATION:
        gap = _field(snippet_id, "se no")
        assert " is " in gap or "id(" in gap, f"snippet {snippet_id}: sharing shown without is/id()"


# --- Claims written after the verification ----------------------------------

def test_snippet_10_claim_would_have_been_right():
    # Case: "I would have got it right, it follows from my previous answers".
    # The two rules Nick actually wrote down for `+=` on a list are:
    #   before verifying (snippet 3): it builds a new object;
    #   after verifying  (snippet 3 gap): it modifies the object in place.
    # Applied to the last block, each rule gives one precise output.
    real_tail = _real_lines(10)[3:]
    first_three = _real_lines(10)[:3]
    unchanged_record = first_three[2]
    from_rule_before = ["TypeError again", unchanged_record]
    from_rule_after = [unchanged_record.replace("9]", "9, 5]")]  # no error printed
    assert real_tail in (from_rule_before, from_rule_after), (
        f"real: {real_tail}; rule before: {from_rule_before}; rule after: {from_rule_after}"
    )
