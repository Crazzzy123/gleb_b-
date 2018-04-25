import rsa, aes, ceasar

def main():
    c = input('[1] Ceasar\n[2] RSA\n[3] AES\nC:')
    if c == '1':
        ceasar.main()
    elif c == '2':
        rsa.main()
    elif c == '3':
        aes.main()
    else:
        print('Wrong input!')

if __name__ == '__main__':
    main()