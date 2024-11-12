"""
Write a Python program to convert a month name to a number of days.
Expected Output:

List of months: January, February, March, April, May, June, July, August
, September, October, November, December
Input the name of Month: February
No. of days: 28/29 days
"""
lst=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print(lst)
s=input("enter the name of given month:").capitalize()
if s=='January':
    print("No. of days:",31," days" )
elif s=='February':
    print("No. of days:",28/29," days" )
elif s=='March':
    print("No. of days:",31," days" )
elif s=='April':
    print("No. of days:",30," days" )
elif s=='May':
    print("No. of days:",31," days" )
elif s=='June':
    print("No. of days:",30," days" )
elif s=='July':
    print("No. of days:",31," days" )
elif s=='August':
    print("No. of days:",31," days" )
elif s=='September':
    print("No. of days:",30," days" )
elif s=='October':
    print("No. of days:",31," days" )
elif s=='November':
    print("No. of days:",30," days" )
elif s=='December':
    print("No. of days:",31," days" )

