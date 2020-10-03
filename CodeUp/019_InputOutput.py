"""
[ref] https://codeup.kr/problem.php?id=1019

Question:
    1. get the time; year.month.day
    2. print it in a certain format 
"""
year, month, day = input().split('.')

print("%04d.%02d.%02d" %(int(year), int(month), int(day)))