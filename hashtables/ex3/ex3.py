def intersection(arrays):
    inter = set(arrays[0])
    for arr in arrays[1:]:
        next_set = set(arr)
        for x in list(inter):
            if x not in next_set:
                inter.remove(x)

    return list(inter)


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
