from meals import (
    grams_label,
    has_required_fields,
    is_new_food,
    needs_review,
    portion_or_default,
)

# --- has_required_fields ---


def test_required_fields_complete_row():
    assert has_required_fields({"food": "oats", "grams": "40"}) is True


def test_required_fields_missing_grams():
    assert has_required_fields({"food": "oats"}) is False


# --- grams_label ---

def test_label_positive_grams():
    assert grams_label(120) == "120 g"


def test_label_missing_grams():
    assert grams_label(None) == "unknown"


def test_label_zero_grams():
    assert grams_label(0) == "0 g"


# --- portion_or_default ---

def test_default_when_none():
    assert portion_or_default(None, 100) == 100


def test_default_when_blank_text():
    assert portion_or_default("   ", 100) == 100


def test_default_keeps_zero():
    assert portion_or_default(0, 100) == 0


def test_default_keeps_text_zero():
    assert portion_or_default("0", 100) == "0"


# --- needs_review ---

def _entry(grams, kcal, confirmed):
    return {"food": "x", "grams": grams, "kcal_per_100g": kcal, "confirmed": confirmed}


def test_review_unconfirmed_huge_portion():
    assert needs_review(_entry(1500, 100, False)) is True


def test_review_confirmed_huge_portion():
    assert needs_review(_entry(1500, 100, True)) is False


def test_review_confirmed_high_kcal():
    assert needs_review(_entry(100, 950, True)) is False


# --- is_new_food ---

def test_new_food():
    assert is_new_food({"food": "tea"}, ["oats"]) is True


def test_known_food():
    assert is_new_food({"food": "oats"}, ["oats"]) is False


def test_food_none():
    assert is_new_food({"food": None}, ["oats"]) is False
