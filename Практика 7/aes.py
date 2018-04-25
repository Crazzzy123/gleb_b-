import pyAesCrypt, os

def dec():
    print("---------------------------------------------------------------")
    file=input("File name: ")
    password=input("Password: ")
    bufferSize = 64*1024
    try:
        pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, bufferSize)
    except FileNotFoundError:
        print("[x] File not found!")
    except ValueError:
        print("[x] Password is Fasle!")
    else:
        print("[+] File '"+str(os.path.splitext(file)[0])+"' successfully saved!")
    finally:
        print("---------------------------------------------------------------")


def enc():
    print("---------------------------------------------------------------")
    file = input("File name: ")
    password = input("Password: ")
    bufferSize = 64 * 1024
    try:
        pyAesCrypt.encryptFile(str(file), str(file) + ".crp", password, bufferSize)
    except FileNotFoundError:
        print("[x] File not found!")
    else:
        print("[+] File '" + str(file) + ".crp' successfully saved!")
    finally:
        print("---------------------------------------------------------------")


def main():
    c = input('[1] Encrypt\n[2] Decrypt\n>>')
    if c == '1':
        enc()
    elif c == '2':
        dec()
    else:
        print('Wrong choice!')
