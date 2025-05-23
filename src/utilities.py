def remove_duplicate_items(raw_list: list[str]) -> list[str]:
    """
    Ensures list only contains unique items by removing duplicates from
    the provided list.

    Args:
        raw_list (list[str]): A 1-dimensional list of strings.

    Returns:
        list[str]: A list of strings with duplicates removed.
    """
    
    deduplicated_list = list(dict.fromkeys(raw_list))
        
    return deduplicated_list
