def union_with(combine, dict1, dict2):
    common_keys = set(dict1.keys()) & set(dict2.keys())
    combined_dict = {key: combine(dict1[key], dict2[key]) for key in common_keys}
    combined_dict.update({key: dict1[key] for key in dict1.keys() - common_keys})
    combined_dict.update({key: dict2[key] for key in dict2.keys() - common_keys})
    return combined_dict