year = int(input("Enter Year: "))
month = int(input("Enter Month (1-12): "))
day = int(input("Enter Date (1-31): "))

if year < 1582 or (year == 1582 and month == 10 and 1 <= day < 15 ) or (year <= 1582 and 1<= month <10 and 1<= day <= 31) or (year < 1582 and 1<= month <=12 and 1<= day <= 31):
    print(True)
else:
    print(False)





    




