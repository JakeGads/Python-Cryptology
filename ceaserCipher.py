from cryptTools import alpha, additiveInverse


def encrypt(message, index):
    message = message.lower()

    translated = ''

    for i in message:
        for h in range(len(alpha)):
            if i == alpha[h]:
                translated += alpha[(h + index) % len(alpha)]
                break

    return translated


def decrypt(message, index):
    message = message.lower()
    index = additiveInverse(index, len(alpha))
    translated = ''

    for i in message:
        for h in range(len(alpha)):
            if i == alpha[h]:
                if h - index < 0:
                    translated += alpha[(h + index + len(alpha)) % len(alpha)]
                else:
                    translated += alpha[(h + index) % len(alpha)]
                break

    return translated


def bruteForceDecrypt(message):
    message = message.lower()
    returnList = []
    for i in range(len(alpha)):
        returnList.append({i: decrypt(message, i)})

    return returnList


def test():
    print(encrypt('Jake is a cool guy', 3))
    print(decrypt('mdnhlvdfrrojxb', 3))
    print(bruteForceDecrypt('mdnhlvdfrrojxb'))


if __name__ == "__main__":
    test()
