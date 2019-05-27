alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def multiplicitveInverse(key, max):
    for i in range(max):
        if key * i % max is 1:
            return i

    return -1


def additiveInverse(key, max):
    return max - key
