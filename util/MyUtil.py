def read_file(filepath):
    # read file:
    with open(filepath) as f:
        lines = f.readlines()
    # trim
    lines = list(map(lambda x: x.strip(), lines))
    # filter empty
    return list(filter(lambda x: len(x) > 0, lines))