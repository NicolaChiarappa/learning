#!/usr/bin/env bash
# Copy one Exercism Python exercise into tracks/python/exercism/NNN-<slug>/,
# without the reference solution (.meta/) and without the hints (.docs/hints.md).
# Usage: tools/exercism_new.sh <slug>
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SOURCE="$ROOT/vendor/exercism-python/exercises"
TARGET_ROOT="$ROOT/tracks/python/exercism"
slug="${1:?usage: exercism_new.sh <slug>}"

if [[ -d "$SOURCE/concept/$slug" ]]; then
    source_dir="$SOURCE/concept/$slug"
elif [[ -d "$SOURCE/practice/$slug" ]]; then
    source_dir="$SOURCE/practice/$slug"
else
    echo "exercise not found: $slug" >&2
    exit 1
fi

last=$(ls "$TARGET_ROOT" | grep -E '^[0-9]{3}-' | sort | tail -1 | cut -c1-3 || true)
number=$(printf "%03d" $((10#${last:-0} + 1)))
target="$TARGET_ROOT/$number-$slug"
mkdir -p "$target"

cp "$source_dir"/*.py "$target"/

{
    echo "# $number — $slug (Exercism, MIT)"
    echo
    [[ -f "$source_dir/.docs/introduction.md" ]] && cat "$source_dir/.docs/introduction.md" && echo
    cat "$source_dir/.docs/instructions.md"
    echo
    echo "---"
    echo "Test: \`cd $target && $ROOT/.venv/bin/python -m pytest -q\`"
} > "$target/README.md"

printf '[pytest]\nmarkers =\n    task: A concept exercise task.\n' > "$target/pytest.ini"

cat > "$target/appunti.md" <<'NOTES'
# Appunti

## Prima (2 righe, prima del codice)
Approccio e un caso limite che prevedi.

## Seconda passata (dopo i test verdi, prima della soluzione di riferimento)
Cosa hai cambiato o cambieresti: uniformità, una riga un compito, nomi.

## Dopo (1 riga, dopo il confronto con la soluzione di riferimento)
Cosa faceva meglio, o "niente di nuovo".
NOTES

echo "$target"
