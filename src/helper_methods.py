def merge_dictionaries(dict1, dict2):
    res = {**dict1, **dict2}
    return res


def flatten_list(input_list):
    return [item for sublist in input_list for item in sublist]

def filter_empty_vals(input_list):
    return [x for x in input_list if x is not None]