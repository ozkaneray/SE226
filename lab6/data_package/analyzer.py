def calculate_mean(num_list):
    if not isinstance(num_list, list):
        raise TypeError(f"Expected a list, got {type(num_list).__name__}")
    if len(num_list) == 0:
        raise ValueError("Cannot calculate mean of an empty list.")
    return sum(num_list) / len(num_list)

def find_maximum(num_list):
    if not isinstance(num_list, list):
        raise TypeError(f"Expected a list, got {type(num_list).__name__}")
    if len(num_list) == 0:
        raise ValueError("Cannot find maximum of an empty list.")
    return max(num_list)

def find_minimum(num_list):
    if not isinstance(num_list, list):
        raise TypeError(f"Expected a list, got {type(num_list).__name__}")
    if len(num_list) == 0:
        raise ValueError("Cannot find minimum of an empty list.")
    return min(num_list)