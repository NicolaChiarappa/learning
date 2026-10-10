from collections.abc import Iterable, Mapping
from operator import itemgetter, attrgetter


def clean_string(valore):
    if isinstance(valore, str):
        substrings = valore.split()
        for sub in substrings:
            sub.strip()
        result = " ".join(substrings)
        result = result.lower()
        if result == "":
            raise ValueError("la stringa è vuota")
        return result
    else:
        raise ValueError('valore must be str')

def clean_grams(valore):
    if isinstance(valore, int) or isinstance(valore, float):
        if valore > 0:
            return valore
        else: raise ValueError('valore must be positive')
    else:
        raise ValueError('valore must be int or float')

def food_exist(mappa, valore):
    if valore in mappa.keys():
        return mappa[valore]
    raise IndexError('valore non trovato')

def clean_dict(dizionario):
    if "grams" not in dizionario.keys() or "food" not in dizionario.keys():
        raise ValueError("grams non trovato")


def aggregate_portions(entries: Iterable[Mapping[str, object]]) -> list[tuple[str, float]]:
    lista = []
    mappa_posizione_food={}
    list_index = 0

    for entry in entries:
        try:
            clean_dict(entry)
            food = clean_string(entry['food'])
            grams = clean_grams(entry['grams'])
        except ValueError:
            raise ValueError(list_index, entry)
        try:
            index = food_exist(mappa_posizione_food, food)
            existing_grams = lista[index][1]
            lista[index] = (food, grams + existing_grams)
        except IndexError:
            lista.append((food, grams))
            mappa_posizione_food[food] = len(lista) - 1
        list_index += 1

    secondary_k_sorting = sorted(lista, key=itemgetter(0), reverse=False)
    primary = sorted(secondary_k_sorting, key=itemgetter(1), reverse=True)
    return primary
