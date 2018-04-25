class Stego():
    def zip(self):
        try:
            namefile = input("File-Cover: ")
            with open(namefile, 'rb') as file1:
                read1 = file1.read()
        except FileNotFoundError:
            print("[x] File: '"+namefile+"' is not defined!")
            raise SystemExit
        try:
            zipfile = input("Zip-File: ")
            with open(zipfile, 'rb') as file2:
                read2 = file2.read()
        except FileNotFoundError:
            print("[x] File: '"+zipfile+"' is not defined!")
            raise SystemExit
        with open(namefile, 'wb') as file3:
            file3.write(read1)
            file3.write(read2)
            print("[+] File: "+namefile+" successfully overwritten!")

    def read(self):
        try:
            namefile = input("File name: ")
            with open(namefile, "rb") as r:
                byte = r.read(1)
                k = 0
                while byte:
                    try:
                        byte = r.read(1).decode("utf-8")
                    except:
                        continue
                    print(byte, end="")
                    k += 1
        except FileNotFoundError:
            print("\n[x] File: '"+namefile+"' is not defined!")
            raise SystemExit
        else:
            print("\n[+] Number of bytes in the '"+namefile+"': "+str(k))

    def write(self):
        try:
            namefile = input("File name: ")
            with open(namefile, 'ab') as file:
                text = input("Write the text: ")
                file.write(text.encode("utf-8"))
        except FileNotFoundError:
            print("[x] File: '"+namefile+"' is not defined!")
            raise SystemExit
        else:
            print("[+] File: "+namefile+" successfully overwritten!")


def main():
    st = Stego
    st.write()
    st.read()
    st.zip()
    st.read()


if __name__ == '__main__':
    main()