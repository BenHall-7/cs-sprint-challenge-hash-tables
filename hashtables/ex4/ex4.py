def has_negatives(a):
    data = {}
    for num in a:
        if -num in data:
            data[-num] = True
        elif num not in data:
            data[num] = False

    return list(map(lambda i: abs(i[0]), filter(lambda i: i[1], data.items())))

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
