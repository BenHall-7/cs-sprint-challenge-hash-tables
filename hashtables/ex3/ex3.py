def intersection(arrays):
    inter = {}
    for arr in arrays:
        for n in arr:
            inter[n] = inter[n] + 1 if n in inter else 1
    
    return list(map(lambda n: n[0], filter(lambda n: n[1] == len(arrays), inter.items())))

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
