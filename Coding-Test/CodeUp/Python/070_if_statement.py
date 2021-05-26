# coding=<utf-8>
"""
[ref] https://codeup.kr/problem.php?id=1070

Question:
    1. receive the month
    2. print the season names corresponding to the month 

월 : 계절 이름
12, 1, 2 : winter
3, 4, 5 : spring
6, 7, 8 : summer
9, 10, 11 : fall
"""

month = int(input())



calendar = {"winter":[12, 1, 2], "spring":[3, 4, 5], "summer":[6, 7, 8], "fall":[9, 10, 11]}

for season, months in calendar.items(): 

    if month in months:
        print("%s" %season)

    else: 
        continue





"""
Get key by value in dict() 

    * https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary

"""