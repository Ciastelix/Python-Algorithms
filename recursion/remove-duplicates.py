def remove_duplicates(txt: str, idx: int = 0) -> str:
    if not txt:
        return ""
    if idx == len(txt) - 1:
        return txt[idx]

    if txt[idx] == txt[idx + 1]:
        return remove_duplicates(txt, idx + 1)
    else:
        return txt[idx] + remove_duplicates(txt, idx + 1)
