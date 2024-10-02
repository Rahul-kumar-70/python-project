print("""            \t\t===================================
                     base conversion calculator
                    ====================================
                      1.Decimal---binary
                      2.decimal---octal
                      3.decimal---hexa
                    ==========================
                      4.binary---decimal
                      5.binary---octal
                      6.binary---hexa
                    ==========================
                      7.octal----decimal
                      8.octal----binary
                      9.octal----hexa
                    ===========================
                      10.hexa---decimal
                      11.hexa---binary
                      12.hexa---octal
                    ===========================
                      13.Exit                   """)
while True:
    ch=input("enter your choice:")
    if ch.isdigit():
        match (ch):
            case '1':
                while True:
                    if ch.isdigit():
                        d=int(input("enter the decimal value for to convert into binary number:"))
                        print("="*70)
                        print("\tdecimal -- binary number")
                        print("=" * 70)
                        print("\t{}---> {}".format(d,bin(d)))
                        print("=" * 70)
                        break
                    else:
                        print("please enter valid digit only digit(0-9)")
            case '2':
                while True:
                    if ch.isdigit():
                        d = int(input("enter the decimal value for to convert into octal number:"))
                        print("=" * 70)
                        print("\tdecimal -- octal number")
                        print("=" * 70)
                        print("\t{}---> {}".format(d, oct(d)))
                        print("="*70)
                        break
                    else:
                        print("please enter valid digit only digit(0-9)")
            case '3':
                while True:
                    if ch.isdigit():
                        d = int(input("enter the decimal value for to convert into hexadecimal number:"))
                        print("=" * 70)
                        print("\tdecimal --hexadecimal number")
                        print("=" * 70)
                        print("\t{}---> {}".format(d, hex(d)))
                        print("="*70)
                        break
                    else:
                        print("please enter valid digit only digit(0-9)")
            case '4':
                while True:
                    b = input("enter the binary value for to convert into decimal number:")
                    if all(char in '01' for char in b):
                        print("=" * 70)
                        print("\tbinary--decimal")
                        print("=" * 70)
                        print("\t0b{}---> {}".format(b, int(b,2)))
                        print("="*70)
                        break
                    else:
                        print("please enter valid binary no(0-1 only)..")
            case '5':
                while True:
                    b = input("enter the binary value for to convert into octal number:")
                    if all(char in '01' for char in b):
                        c=int(b)
                        print("=" * 70)
                        print("\tbinary--octal")
                        print("=" * 70)
                        print("\t0b{}---> {}".format(b, oct(c)))
                        print("="*70)
                        break
                    else:
                        print("please enter valid binary no(0-1 only)..")
            case '6':
                while True:
                    b = input("enter the binary value for to convert into hexadecimal number:")
                    if all(char in '01' for char in b):
                        c = int(b)
                        print("=" * 70)
                        print("\tbinary--hexadecimal")
                        print("=" * 70)
                        print("\t0b{}---> {}".format(b, hex(c)))
                        print("="*70)
                        break
                    else:
                        print("please enter valid binary no(0-1 only)..")
            case '7':
                while True:
                    o = input("enter the octal value for to convert into decimal number:")
                    if all(char in '01234567' for char in o):
                        print("=" * 70)
                        print("\toctal--decimal")
                        print("=" * 70)
                        print("\t0o{}---> {}".format(o, int(o,8)))
                        print("="*70)
                        break
                    else:
                        print("please enter valid octal no(0-7 only)..")
            case '8':
                while True:
                    o = input("enter the octal value for to convert into binary number:")
                    if all(char in '01234567' for char in o):
                        c=int(o,8)
                        print("=" * 70)
                        print("\toctal--binary")
                        print("=" * 70)
                        print("\t0o{}---> {}".format(o, bin(c)))
                        print("="*70)
                        break
                    else:
                        print("please enter valid octal no(0-7 only)..")
            case '9':
                while True:
                    o = input("enter the octal value for to convert into hexadecimal number:")
                    if all(char in '01234567' for char in o):
                        c=int(o,8)
                        print("=" * 70)
                        print("\toctal--hexdecimal")
                        print("=" * 70)
                        print("\t0o{}---> {}".format(o, hex(c)))
                        print("="*70)
                        break
                    else:
                        print("please enter valid octal no(0-7 only)..")
            case '10':
                while True:
                    h = input("enter the hexadecimal value for to convert into decimal number:")
                    if all(char in '0123456789abcdef' for char in h):
                        print("=" * 70)
                        print("\thexadecimal--decimal")
                        print("=" * 70)
                        print("\t\t0x{}---> {}".format(h, int(h, 16)))
                        print("="*70)
                        break
                    else:
                        print("please enter valid hexadecimal no(0-9 or a-f)..")
            case '11':
                while True:
                    h = input("enter the hexadecimal value for to convert into binary number:")
                    if all(char in '0123456789abcdef' for char in h):
                        c=int(h,16)
                        print("=" * 70)
                        print("\thexadecimal--binary")
                        print("=" * 70)
                        print("\t\t0x{}---> {}".format(h, bin(c)))
                        print("="*70)
                        break
                    else:
                        print("please enter valid hexadecimal no(0-9 or a-f)..")
            case '12':
                while True:
                    h = input("enter the hexadecimal value for to convert into octal number:")
                    if all(char in '0123456789abcdef' for char in h):
                        c=int(h,16)
                        print("=" * 70)
                        print("\thexadecimal--octal")
                        print("=" * 70)
                        print("\t\t0x{}---> {}".format(h, oct(c)))
                        print("="*70)
                        break
                    else:
                        print("please enter valid hexadecimal no(0-9 or a-f)..")

            case '13':
                import sys
                sys.exit()
            case _:
                print("your choice invalid ! so please enter the valid choice..")
    else:
        print("your choice invalid ! so please enter the valid choice..")

