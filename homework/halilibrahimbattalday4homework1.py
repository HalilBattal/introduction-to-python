def halil(start, end):
    out = list()
    if start <= 1:
        start = 2

    battal = [True] * (end + 1)
    for p in range(start, end + 1):
        if (battal[p]):
            out.append(p)
            for i in range(p, end + 1, p):
                battal[i] = False
    return out

print(halil(1, 100))