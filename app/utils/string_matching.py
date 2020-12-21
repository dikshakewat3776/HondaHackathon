from difflib import SequenceMatcher


def similar_string(a, b):
    ratio = SequenceMatcher(None, a, b).ratio()
    if ratio > 0.7:
        return True
    else:
        return False
