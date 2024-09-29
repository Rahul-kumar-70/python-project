class DepositError(Exception):pass
class WithdrawError(BaseException):pass
class InSuffFundError(Exception):pass
def menu():
    print("="*50)
    print("\tATM / Funds Transfer Applications")
    print("=" * 50)
    print("\t1.Deposit")
    print("\t2.Withdraw")
    print("\t3.Bal Enq")
    print("\t4.Exit")
    print("=" * 50)
bal=500.00 # Global Variable
def deposit():
    damt=float(input("Enter Ur Deposit Amount:")) # implcitly raising ValueError in the case non-num vals
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("Ur Account xxxxxxxxx123 Credited with INR:{}".format(damt))
        print("Now Ur Account xxxxxxxxx123 Bal after Deposit INR:{}".format(bal))
def withdraw():
    global bal
    wamt = float(input("Enter Ur Withdraw Amount:")) # implcitly raising ValueError in the case non-num vals
    if(wamt<=0):
        raise WithdrawError
    elif((wamt+500)>bal):
        raise InSuffFundError
    else:
        bal=bal-wamt
        print("Ur Account xxxxxxxxx123 Debited with INR:{}".format(wamt))
        print("Now Ur Account xxxxxxxxx123 Bal after withdraw INR:{}".format(bal))

def balenq():
    print("Now Ur Account xxxxxxxxx123 Bal INR:{}".format(bal))
while(True):
    try:
        menu()
        ch=int(input("Enter Ur Choice:"))
        match(ch):
            case 1:
                try:
                    deposit() # Function Call
                except DepositError:
                    print("\tDon't try to Deposit -VE and Zero Amount")
                except ValueError:
                    print("\tDon't try to Deposit alnums,strs and symbols")
            case 2:
                try:
                    withdraw()
                except WithdrawError:
                    print("\tDon't try to Withdraw -VE and Zero Amount")
                except InSuffFundError:
                    print("\tUr Account does not have funds--Read Python Notes")
                except ValueError:
                    print("\tDon't try to Withdraw alnums,strs and symbols")
            case 3:
                balenq()
            case 4:
                print("Thx for Using Program")
                break
            case _:
                print("Ur Selection of Operations is wrong-try again")
    except ValueError:
        print("\tDon't enter strs,alnums,symbols for Choice of Ints")
