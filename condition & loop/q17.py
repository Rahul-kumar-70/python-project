"""Write a Python program to print the alphabet pattern 'A'.
Expected Output:

  ***
 *   *
 *   *
 *****
 *   *
 *   *
 *   * """
for i in range(8):
    for j in range(5):
        if (i == 0 and j in {1, 2, 3}) or (i in {1,2,4, 5, 6} and (j == 0 or j == 4))  or (i == 3) :
            print("*", end="")
        else:
            print(" ", end="")
    print()