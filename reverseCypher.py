def encrypt(message):
    translated = ''
    
    i = len(message) - 1

    while i >= 0:
        translated += message[i]
        i-=1

    return translated

def decrypt(message):
    translated = ''
    
    i = len(message) - 1

    while i >= 0:
        translated += message[i]
        i-=1

    return translated

if __name__ == "__main__":
    print(encrypt('Jake is a cool guy'))
    print(decrypt(encrypt('Jake is a cool guy')))