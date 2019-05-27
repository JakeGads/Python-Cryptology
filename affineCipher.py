from cryptTools import alpha, multiplicitveInverse
import ceaserCipher as shift
import multiplictiveCipher as mult


def encrypt(message, additive, multiplictive):
    message = message.lower()
    message = shift.encrypt(message, additive)
    message = mult.encrypt(message, multiplictive)
    return message


def decrypt(message, additive, multiplicitve):
    message = message.lower()
    message = mult.decrypt(message, multiplicitve)
    message = shift.decrypt(message, additive)
    return message


def bruteForceDecrypt(message):
    message = message.lower()
    returnList = []
    for additive in range(len(alpha)):
        for multiplicitve in range(len(alpha)):
            returnList.append({'additive: ' + str(additive) + ' multiplicitve ' +
                               str(multiplicitve): decrypt(message, additive, multiplicitve)})

    return returnList


def test():
    print(encrypt('Jake is a cool guy', 5, 3))
    print(decrypt(encrypt('Jake is a cool guy', 5, 3), 5, 3))
    print(bruteForceDecrypt(encrypt('Jake is a cool guy', 5, 3)))


if __name__ == "__main__":
    test()
