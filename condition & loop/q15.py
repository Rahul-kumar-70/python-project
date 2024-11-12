"""Write a Python program to check the validity of passwords input by users.
Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters."""
"""lc=0
uc=0
val=list(input('enter the value:'))
for v in val:
    if v.isupper():
        uc=uc+1
    else:
        lc=lc+1
if (lc>0 and uc>0 and set(val).intersection(['@','$','#']) and set(val).intersection(dl) and (len(val)>=6 or len(val)<=16)):
    print('valid password')
else:
    print('invalid password')

"""
up=0
lo=0
d=0
c=0
s=input("enter the password:")
for ch in s:
    if ch.isupper() :
        up=up+1
    if ch.islower():
        lo=lo+1
    if ch.isdigit():
        d=d+1
    if ch in ['$','#','@']:
        c=c+1
if up>=1 and lo>=1 and d>=1 and c>=1:
    if 6<=(up+lo+d+c)<=16:
        print(s)
    else:
        print("password not greater than 16 chacters or less than 6 charters")
else:
    print("invalid pasaword must be 1 upperCase,1 LowerCase,1 digit,1 special symbol")
