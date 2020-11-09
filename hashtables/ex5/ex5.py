def finder(files, queries):
    file_map = {}
    for full in files:
        ind = full.rindex('/')
        filename = full if ind < 0 else full[ind + 1:]
        if filename in file_map:
            file_map[filename].append(full)
        else:
            file_map[filename] = [full]

    result = []
    for q in queries:
        if q in file_map:
            result.extend(file_map[q])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
