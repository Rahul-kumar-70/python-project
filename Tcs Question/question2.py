"""Joseph is learning digital logic subject which will be for his next semester. He usually tries to solve unit assignment
 problems before the lecture. Today he got one tricky question. The problem statement is “A positive integer has been given as an input.
  Convert decimal value to binary representation. Toggle all bits of it after the most significant bit including the most significant bit.
   Print the positive integer value after toggling all bits”.
Constrains-
1<=N<=100
Example 1:
Input :
10  -> Integer
Output :
5    -> result- Integer
Explanation:
Binary representation of 10 is 1010. After toggling the bits(1010), will get 0101 which represents “5”. Hence output will print “5”."""
n=input("enter the number:")
if int(n)<0:
    print("invalid number:")
else:
    if n.isdigit():
        a=bin(int(n))
        b=a[2:len(a)]
        c=[]
        for i in range(0,len(b)):
            if b[i]=='1':
                c.append(0)
            else:
                c.append(1)
        d=""
        for j in c:
            d+=str(j)
        print(d)
        e=int(d,2)
        print(e)
