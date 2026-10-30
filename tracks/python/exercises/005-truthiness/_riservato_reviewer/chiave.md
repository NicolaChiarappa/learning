# Chiave 005 (solo reviewer)

has_required_fields: `if "grams" not in row or "food" not in row:` (oppure `return "grams" in row and "food" in row`).
grams_label: `if grams is None:`
portion_or_default:
    if raw is None or (isinstance(raw, str) and not raw.strip()):
        return default
    return raw
needs_review: `if not entry["confirmed"] and (entry["grams"] > 1000 or entry["kcal_per_100g"] > 900):`
is_new_food: `entry.get("food") is not None and entry["food"] not in seen_foods` (comportamento invariato, solo leggibilita).
