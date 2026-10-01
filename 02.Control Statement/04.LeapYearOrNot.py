# WAP to check the given year is a Leap Year or NOT. 

year = int(input("Enter your year : "))

if (year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year} is leap year")

else:
    print(f"{year} is not leap year")