"""Completeness checks for exercise 001.

These tests do NOT check whether the predictions are correct. They check that
the delivery is complete: design note filled, and for snippets 1-9 a prediction,
an explanation, a confidence level, a verification result and, when the
prediction was wrong, a motivated explanation of the gap.
"""
import re
from pathlib import Path

import pytest

HERE = Path(__file__).parent
SNIPPET_IDS = list(range(1, 10))
MIN_EXPLANATION_CHARS = 40
MIN_GAP_CHARS = 40

COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
FIELD_RE = re.compile(r"^\*\*(?P<label>[^*\n]+?):\*\*[ \t]*(?P<body>.*?)(?=^\*\*|\Z)", re.DOTALL | re.MULTILINE)


def _clean(text: str) -> str:
    return COMMENT_RE.sub("", text).replace("---", "").strip()


def _parse_snippets(path: Path) -> dict[int, dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    sections = re.split(r"^## Snippet (\d+)[^\n]*\n", text, flags=re.MULTILINE)
    snippets: dict[int, dict[str, str]] = {}
    # re.split with a capture group: [preamble, id1, body1, id2, body2, ...]
    for snippet_id, body in zip(sections[1::2], sections[2::2]):
        fields = {}
        for match in FIELD_RE.finditer(body):
            fields[match.group("label").strip().lower()] = _clean(match.group("body"))
        snippets[int(snippet_id)] = fields
    return snippets


def _field(fields: dict[str, str], prefix: str) -> str:
    for label, body in fields.items():
        if label.startswith(prefix):
            return body
    return ""


@pytest.fixture(scope="module")
def snippets() -> dict[int, dict[str, str]]:
    return _parse_snippets(HERE / "risposte.md")


def test_design_note_is_filled():
    text = (HERE / "design.md").read_text(encoding="utf-8")
    sections = re.split(r"^## ", text, flags=re.MULTILINE)[1:]
    assert len(sections) >= 5
    empty = []
    for section in sections:
        title, _, body = section.partition("\n")
        if len(_clean(body)) < 15:
            empty.append(title.strip())
    assert not empty, f"design.md sections still empty: {empty}"


def test_timing_header_is_filled():
    text = (HERE / "risposte.md").read_text(encoding="utf-8")
    for label in ("Previsioni terminate alle", "Verifica iniziata alle", "Quanti snippet su 9"):
        match = re.search(rf"^{label}[^:\n]*:[ \t]*(.*)$", text, flags=re.MULTILINE)
        assert match and match.group(1).strip(), f"missing: {label}"


@pytest.mark.parametrize("snippet_id", SNIPPET_IDS)
def test_prediction_present(snippets, snippet_id):
    fields = snippets.get(snippet_id, {})
    assert len(_field(fields, "previsione")) >= 3, f"snippet {snippet_id}: prediction is empty"


@pytest.mark.parametrize("snippet_id", SNIPPET_IDS)
def test_explanation_present(snippets, snippet_id):
    fields = snippets.get(snippet_id, {})
    explanation = _field(fields, "spiegazione")
    assert len(explanation) >= MIN_EXPLANATION_CHARS, (
        f"snippet {snippet_id}: explanation missing or too short "
        f"(at least {MIN_EXPLANATION_CHARS} characters, with the real names from the code)"
    )


@pytest.mark.parametrize("snippet_id", SNIPPET_IDS)
def test_confidence_declared(snippets, snippet_id):
    fields = snippets.get(snippet_id, {})
    assert re.fullmatch(r"[1-5]", _field(fields, "sicurezza")), (
        f"snippet {snippet_id}: confidence must be a single digit 1-5"
    )


@pytest.mark.parametrize("snippet_id", SNIPPET_IDS)
def test_verification_done_and_gap_explained(snippets, snippet_id):
    fields = snippets.get(snippet_id, {})
    verdict = _field(fields, "dopo la verifica").lower()
    assert verdict in {"si", "sì", "no"}, f"snippet {snippet_id}: write si or no after verifying"
    if verdict == "no":
        gap = _field(fields, "se no")
        assert len(gap) >= MIN_GAP_CHARS, (
            f"snippet {snippet_id}: prediction was wrong but the gap is not explained "
            f"(what you thought, what happens, why, which REPL test)"
        )
