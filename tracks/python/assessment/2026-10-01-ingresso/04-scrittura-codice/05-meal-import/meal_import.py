class ImportFileError(Exception):
    """The file as a whole cannot be imported (empty, bad header)."""


def import_meals(text: str, tz: str) -> "ImportReport":
    raise NotImplementedError
