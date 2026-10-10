from collections.abc import Iterable, Iterator


def split_sessions(timestamps: Iterable[float], max_gap: float) -> Iterator[list[float]]:
    if timestamps is None or max_gap is None or max_gap <= 0.0:
        raise ValueError()


    sessioni = []

    for timestamp in timestamps:
        if len(sessioni) == 0:
            sessioni.append([timestamp])
        else:
            if sessioni[-1][-1] + max_gap >= timestamp:
                sessioni[-1].append(timestamp)
            else:
                sessioni.append([timestamp])

    print(sessioni)
    return sessioni
