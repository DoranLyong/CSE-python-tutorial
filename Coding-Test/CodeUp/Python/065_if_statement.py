"""
[ref] https://codeup.kr/problem.php?id=1065

Question:
    1. take three integers; (a, b, c) 
    2. print only even numbers 
"""
import sys 

a, b, c = map(int, sys.stdin.readline().rstrip().split())


even_num = [ even for even in (a, b, c) if even%2==0 ]


for i in even_num:
    print("%d" %i)