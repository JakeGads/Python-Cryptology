from cryptTools import alpha, multiplicitveInverse


def encrypt(message, key):
    translated = ''
    message = message.lower()

    for i in message:
        for h in range(len(alpha)):
            if i == alpha[h]:
                translated += alpha[(h * key) % len(alpha)]

    return translated


def decrypt(message, key):
    key = multiplicitveInverse(key, len(alpha))
    if key is -1:
        return 'No multiplicitve inverse found'

    return encrypt(message, key)


def bruteForceDecrypt(message):
    returnList = []
    for i in range(len(alpha)):
        returnList.append({i: decrypt(message, i)})

    return returnList


def test():
    print(encrypt('Jake is a cool guy', 3))
    print(decrypt(encrypt('Jake is a cool guy', 3),
                  multiplicitveInverse(3, len(alpha))))
    print(bruteForceDecrypt(encrypt('Jake is a cool guy', 3)))


if __name__ == "__main__":
    test()
