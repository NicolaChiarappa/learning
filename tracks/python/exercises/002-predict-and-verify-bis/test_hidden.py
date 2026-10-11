"""Reviewer checks for exercise 002 (run explicitly: pytest -q test_hidden.py).

Unlike test_delivery.py, these tests DO compare the predictions with the real
output. The expected output is produced by running each snippet, so the key is
never duplicated here.
"""
import re
import subprocess
import sys
from pathlib import Path

import pytest

from test_delivery import _blocks, _clean, _field, _parse_sections

HERE = Path(__file__).parent
SNIPPET_IDS = [1, 2, 3, 4, 5]
SECTIONS = _parse_sections(HERE / "risposte.md")
SNIPPETS = {n: SECTIONS[f"Snippet {n}"] for n in SNIPPET_IDS}
SYNTHESIS = SECTIONS["Sintesi e prova di trasferimento"]


def _run(name: str) -> list[str]:
    result = subprocess.run(
        [sys.executable, "-I", str(HERE / "snippets" / name)], capture_output=True, text=True, check=True
    )
    return result.stdout.splitlines()


REAL = {n: _run(f"s0{n}.py") for n in SNIPPET_IDS}
REAL_TRANSFER = _run("transfer.py")


def _lines(fields: dict[str, str], prefix: str) -> list[str]:
    blocks = _blocks(_field(fields, prefix, clean=False))
    return [line.rstrip() for line in blocks[0].splitlines()] if blocks else []


def _content(line: str) -> str:
    """Normalise away pure form: spaces, quote style, capitalisation, quotes around a bare string."""
    return line.replace('"', "'").replace(" ", "").lower().strip("'")


# Every printed line, labelled with the trap it is meant to catch (from _designer_notes.md).
TRAPS = {
    (1, 0): "E005: names_alias sees the in-place += on the list",
    (1, 1): "E005: ids_alias stays on the old tuple (no TypeError)",
    (1, 2): "E005: ids moves to a new tuple",
    (1, 3): "E005: label_alias stays on the old string",
    (2, 0): "E003: dict value is the same list, both appends visible",
    (2, 1): "E003: bundle holds the same list twice",
    (2, 2): "E003: bundle[0] is bundle[1]",
    (2, 3): "E001: menu['lunch'] = [99] does not touch base_prices",
    (2, 4): "E001: menu['lunch'] = [99] does not touch bundle",
    (3, 0): "E001: module-level log = [] leaves mirror alone",
    (3, 1): "E001: log now labels the new list",
    (3, 2): "E002: reassigning the parameter does not touch session",
    (3, 3): "E002: the function returns the new list",
    (3, 4): "E002: result is not session",
    (4, 0): "E002/E005: += on a list parameter mutates the caller's list (no TypeError)",
    (4, 1): "E002/E005: += on a tuple parameter leaves the caller's tuple alone",
    (4, 2): "E002: grown_list is as_list",
    (4, 3): "E005: grown_tuple differs from as_tuple",
    (5, 0): "E004: original sees the shared tags list, keeps its own name and scores",
    (5, 1): "E004: snapshot['scores'] = [9] rebinds a key, it is not an append",
    (5, 2): "E004: tags list is shared between the two dicts",
    (5, 3): "E004: scores is no longer shared after the key is rebound",
}


@pytest.mark.parametrize("snippet_id", SNIPPET_IDS)
def test_prediction_has_one_line_per_print(snippet_id):
    assert len(_lines(SNIPPETS[snippet_id], "previsione")) == len(REAL[snippet_id])


@pytest.mark.parametrize("key", sorted(TRAPS), ids=lambda key: f"s{key[0]}-line{key[1] + 1}")
def test_predicted_line_content(key):
    """One test per printed line, ignoring pure form. The trap covered is in TRAPS."""
    snippet_id, index = key
    predicted = _lines(SNIPPETS[snippet_id], "previsione")
    assert index < len(predicted), TRAPS[key]
    assert _content(predicted[index]) == _content(REAL[snippet_id][index]), TRAPS[key]


@pytest.mark.parametrize("snippet_id", SNIPPET_IDS)
def test_prediction_is_exact_output(snippet_id):
    """README, 'Output esatto': character by character, as Python prints it."""
    assert _lines(SNIPPETS[snippet_id], "previsione") == REAL[snippet_id]


@pytest.mark.parametrize("snippet_id", SNIPPET_IDS)
def test_pasted_output_is_the_real_output(snippet_id):
    """'Output ottenuto' must be a paste of the real run, not a rewrite."""
    assert _lines(SNIPPETS[snippet_id], "output ottenuto") == REAL[snippet_id]


@pytest.mark.parametrize("snippet_id", SNIPPET_IDS)
def test_self_assessment_matches_reality(snippet_id):
    """The si/no written after the verification agrees with the content comparison."""
    predicted = [_content(line) for line in _lines(SNIPPETS[snippet_id], "previsione")]
    right = predicted == [_content(line) for line in REAL[snippet_id]]
    assert _field(SNIPPETS[snippet_id], "dopo la verifica").lower() == ("si" if right else "no")


@pytest.mark.parametrize("snippet_id", SNIPPET_IDS)
def test_rows_say_who_sees_the_object_afterwards(snippet_id):
    """E001 exit criterion: every row ends with 'dopo:' and the names looking at the same object."""
    rows = [r for r in _field(SNIPPETS[snippet_id], "righe").splitlines() if r.strip().startswith("-")]
    missing = [r for r in rows if "dopo" not in r.lower()]
    assert not missing, f"{len(missing)}/{len(rows)} rows without 'dopo:'"


def test_rows_do_not_justify_by_type():
    """E001: 'essendo immutabile' as the reason, instead of what the line does to which label."""
    rows = " ".join(_field(SNIPPETS[n], "righe") for n in SNIPPET_IDS).lower()
    assert len(re.findall(r"essendo\s+(?:im)?mutabil", rows)) == 0


def test_same_line_shape_read_the_same_way():
    """`container[key] = [new]` appears in snippet 2 and in snippet 5: it must be read as a rebind both times."""
    row_2 = next(r for r in _field(SNIPPETS[2], "righe").splitlines() if 'menu["lunch"] = [99]' in r)
    row_5 = next(r for r in _field(SNIPPETS[5], "righe").splitlines() if 'snapshot["scores"] = [9]' in r)
    for row in (row_2, row_5):
        assert "aggiunge" not in row.lower() and "coda" not in row.lower(), row


def test_alternative_hypothesis_differs_from_prediction():
    assert _lines(SNIPPETS[5], "ipotesi alternativa") != _lines(SNIPPETS[5], "previsione")


def test_one_of_the_two_hypotheses_gives_the_real_output():
    """Snippet 5: two hypotheses on dict(); the right one must lead to the real output."""
    real = [_content(line) for line in REAL[5]]
    candidates = [_lines(SNIPPETS[5], "previsione"), _lines(SNIPPETS[5], "ipotesi alternativa")]
    assert any([_content(line) for line in candidate] == real for candidate in candidates)


def test_design_doubt_carried_into_prediction():
    """design.md, doubt 2 expects dict(original) to share the values ('is' -> True): the prediction must agree."""
    design = (HERE / "design.md").read_text(encoding="utf-8").lower()
    assert "torna true" in design  # the hypothesis written before predicting
    assert _content(_lines(SNIPPETS[5], "previsione")[2]) == "true"


def test_calibration_estimate_matches_result():
    closing = SECTIONS["Chiusura delle previsioni"]
    estimate = int(_field(closing, "stima dei giusti"))
    right = sum(
        [_content(a) for a in _lines(SNIPPETS[n], "previsione")] == [_content(b) for b in REAL[n]] for n in SNIPPET_IDS
    )
    assert estimate == right


def test_gap_expected_line_has_a_reason():
    """P02: 'Atteso: <output> perché <explanation under test>', written before running."""
    assert "perch" in _field(SNIPPETS[5], "scarto - atteso").lower()


def test_gap_experiment_can_fail():
    """The experiment must probe the two lines that were misread, not only what the output already showed."""
    experiment = " ".join(_blocks(_field(SNIPPETS[5], "scarto - esperimento", clean=False)))
    assert "+=" in experiment, "no probe of `snapshot[key] += ...`"
    assert re.search(r"\]\s*=\s*\[", experiment), "no probe of `snapshot[key] = [...]`"


def test_gap_explanation_covers_every_wrong_line():
    """The gap analysis must explain why 'y' shows up in original and why scores is [9]."""
    text = _field(SNIPPETS[5], "scarto - spiegazione").lower()
    assert "tags" in text and "scores" in text and "name" in text


def test_experiment_names_are_by_role():
    """Method rule 10: English, by role, also in throwaway REPL code."""
    code = " ".join(_blocks(_field(SNIPPETS[5], "scarto - esperimento", clean=False)))
    code += (HERE / "design.md").read_text(encoding="utf-8")
    assert not re.search(r"\b(new_dict|lista|dizionario|key1|oggetto\d*)\b", code)


def test_transfer_prediction_exact():
    assert _lines(SYNTHESIS, "riga nuova - previsione") == REAL_TRANSFER


def test_transfer_pasted_output_is_real():
    assert _lines(SYNTHESIS, "riga nuova - output ottenuto") == REAL_TRANSFER


def test_transfer_explanation_names_the_modified_object():
    """Why `row` sees it: the line modifies the dict that `record` and `row` both label."""
    text = _field(SYNTHESIS, "riga nuova - spiegazione").lower()
    assert re.search(r"\b(dict|dizionario|row)\b", text) and "record" in _clean(text.split("\n", 1)[-1])


def test_rule_distinguishes_bare_name_from_index():
    rule = _field(SYNTHESIS, "la mia regola").lower()
    assert re.search(r"indice|chiave|\[|sinistra", rule)


def test_rule_says_what_to_do_with_the_answer():
    rule = _field(SYNTHESIS, "la mia regola").lower()
    assert re.search(r"\bse\b|allora|quindi", rule)


def test_design_updated_mid_work():
    """A new doubt surfaced on snippet 5 (question about dict() docs): it belongs in 'Aggiornamenti a metà lavoro'."""
    text = (HERE / "design.md").read_text(encoding="utf-8")
    body = text.split("## Aggiornamenti a metà lavoro", 1)[1].split("## Tempo", 1)[0]
    assert len(_clean(body)) > 0
