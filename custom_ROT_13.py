

def decrypt_ro13(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890./='
    result_str = ''
    for character in string:
        index = alphabet.find(character)
        result_str += alphabet[(index + 0xD) % len(alphabet)]
    print(result_str)

def main():
    while True:
        filename = input("String: ")
        data = decrypt_ro13(filename)
if __name__ == '__main__':
    main()