def build_params(page: int):
    params = [
        ("floors[]", 1),
        ("floors[]", 2),
        ("square[]", "100"),
        ("square[]", "100-150"),
        ("price_from", 761970),
        ("price_max", 3989300),
        ("action", "filter"),
    ]

    if page > 1:
        params.append(("page", page))

    return params