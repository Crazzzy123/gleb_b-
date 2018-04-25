import rsa


def dec():
    file = input("Write the filename: ")
    file_key = input("Write the filename with key:")
    with open(file_key, "r") as k:
        pr_key = k.read().split()
        n, e, d, p, q = pr_key
    with open(file, "rb") as r:
        read = r.read()
        message = rsa.decrypt(read, rsa.PrivateKey(int(n), int(e), int(d), int(p), int(q)))
        print("\n[*] Decrypted text:\n\n[text] << " + str(message.decode("utf8")) + "\n")


def enc():
    try:
        with open('publicKey.txt', 'w+') as file_public_key, \
                open('privateKey.txt', 'w+') as file_private_key:
            public_key, private_key = rsa.newkeys(1024)
            public_key = str(public_key)
            public_key = public_key[public_key.find('(') + 1:public_key.find(',')]
            file_public_key.write(str(public_key))
            private_key = str(private_key)
            private_key = private_key.split()
            n, e, d, p, q = private_key[0], private_key[1], private_key[2], private_key[3], private_key[4]
            n, e, d, p, q = n[n.find('(') + 1:len(n) - 1], \
                            e[:len(e) - 1], \
                            d[:len(d) - 1], \
                            p[:len(p) - 1], \
                            q[:len(q) - 1]
            file_private_key.write(n + ' ' + e + ' ' + d + ' ' + p + ' ' + q)
    except FileNotFoundError:
        print('File not found!')

    text = input("\n[*] Write the text:\n\n[text] >> ")
    message = text.encode("utf8")
    crypt = rsa.encrypt(message, rsa.PublicKey(public_key))
    with open("text_crypt.txt", "wb") as w:
        w.write(crypt)
        print("\n[*] Crypt-text:\n\n" + str(crypt) + "\n\n[+] File: 'text_crypt.txt' successfully saved!\n")


def main():
    c = input('[1] Encrypt\n[2] Decrypt\n>>')
    if c == '1':
        enc()
    elif c == '2':
        dec()
    else:
        print('Wrong choice!')