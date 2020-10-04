"""
[ref] https://codeup.kr/problem.php?id=1023

Question:
    1. get a real number 
    2. print it into integer and fraction parts
"""
integer, fraction = input().split(".")

print("%d \n%d" %(int(integer), int(fraction)))