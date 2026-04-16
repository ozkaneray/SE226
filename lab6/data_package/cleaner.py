def remove_duplicates(data_list):
    if not isinstance(data_list, list):
        raise TypeError(f"Expected a list, got {type(data_list).__name__}")
    return list(dict.fromkeys(data_list))

def strip_whitespaces(string_list):
    if not isinstance(string_list, list):
        raise TypeError(f"Expected a list, got {type(string_list).__name__}")
    return [s.strip() for s in string_list]