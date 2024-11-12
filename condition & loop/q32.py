"""
 Write a Python program to check whether an alphabet is a vowel or consonant.
Expected Output:

Input a letter of the alphabet: k
k is a consonant.
"""
l=input("Input a letter of the alphabet:")
if len(l)==1:
    if l in ['a','e','i','o','u']:
        print("{} is a vowel".format(l))
    else:
        print("{} is consonant".format(l))
else:
    print("invalid latter")
