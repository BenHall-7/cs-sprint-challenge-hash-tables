def get_indices_of_item_weights(weights, length, limit):
    prev = {} # maps weight to index
    for i in range(length):
        cur = weights[i]
        diff = limit - cur
        if diff in prev:
            return sorted((i, prev[diff]), reverse=True)
        else:
            prev[cur] = i

    return None
