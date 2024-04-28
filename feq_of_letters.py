# figuring out how frequent which letters are in the alphabet
# we have sample1.txt and sample2.txt

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def get_frequency():
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    n = 0
    o = 0
    p = 0
    q = 0
    r = 0
    s = 0
    t = 0
    u = 0
    v = 0
    w = 0
    x = 0
    y = 0
    z = 0
    total = 0

    with open('sample1.txt', 'r', errors='ignore') as file:
        for line in file:
            for char in line:
                if char in ALPHABET:
                    if char == 'a':
                        a += 1
                    elif char == 'b':
                        b += 1
                    elif char == 'c':
                        c += 1
                    elif char == 'd':
                        d += 1
                    elif char == 'e':
                        e += 1
                    elif char == 'f':
                        f += 1
                    elif char == 'g':
                        g += 1
                    elif char == 'h':
                        h += 1
                    elif char == 'i':
                        i += 1
                    elif char == 'j':
                        j += 1
                    elif char == 'k':
                        k += 1
                    elif char == 'l':
                        l += 1
                    elif char == 'm':
                        m += 1
                    elif char == 'n':
                        n += 1
                    elif char == 'o':
                        o += 1
                    elif char == 'p':
                        p += 1
                    elif char == 'q':
                        q += 1
                    elif char == 'r':
                        r += 1
                    elif char == 's':
                        s += 1
                    elif char == 't':
                        t += 1
                    elif char == 'u':
                        u += 1
                    elif char == 'v':
                        v += 1
                    elif char == 'w':
                        w += 1
                    elif char == 'x':
                        x += 1
                    elif char == 'y':
                        y += 1
                    elif char == 'z':
                        z += 1
                    total += 1

    with open('sample2.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            for char in line:
                if char in ALPHABET:
                    if char == 'a':
                        a += 1
                    elif char == 'b':
                        b += 1
                    elif char == 'c':
                        c += 1
                    elif char == 'd':
                        d += 1
                    elif char == 'e':
                        e += 1
                    elif char == 'f':
                        f += 1
                    elif char == 'g':
                        g += 1
                    elif char == 'h':
                        h += 1
                    elif char == 'i':
                        i += 1
                    elif char == 'j':
                        j += 1
                    elif char == 'k':
                        k += 1
                    elif char == 'l':
                        l += 1
                    elif char == 'm':
                        m += 1
                    elif char == 'n':
                        n += 1
                    elif char == 'o':
                        o += 1
                    elif char == 'p':
                        p += 1
                    elif char == 'q':
                        q += 1
                    elif char == 'r':
                        r += 1
                    elif char == 's':
                        s += 1
                    elif char == 't':
                        t += 1
                    elif char == 'u':
                        u += 1
                    elif char == 'v':
                        v += 1
                    elif char == 'w':
                        w += 1
                    elif char == 'x':
                        x += 1
                    elif char == 'y':
                        y += 1
                    elif char == 'z':
                        z += 1
                    total += 1

    monogram = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h, 'i': i, 'j': j, 'k': k, 'l': l,
                'm': m, 'n': n, 'o': o, 'p': p, 'q': q, 'r': r, 's': s, 't': t, 'u': u, 'v': v, 'w': w, 'x': x, 'y': y, 'z': z}

    for key, value in monogram.items():
        monogram[key] = round(value / total * 100, 4)

    # for key, value in monogram.items():
    #     print(f'{key}: {value}%')
    return monogram
