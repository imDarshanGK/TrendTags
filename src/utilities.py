from typing import List

def remove_duplicate_items(raw_list: List[str]) -> List[str]:
    """Remove duplicate items from a list while preserving order."""
    seen = set()
    deduped = []
    for item in raw_list:
        if item not in seen:
            seen.add(item)
            deduped.append(item)
    return deduped
