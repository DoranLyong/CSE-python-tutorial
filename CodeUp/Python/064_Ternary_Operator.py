"""
[ref] https://codeup.kr/problem.php?id=1064

Question:
    1. take three integers; (a, b, c ) 
    2. print min out among them
    (!) Use Ternary Operatory -> https://m.blog.naver.com/wideeyed/221858874414
"""
import sys 

a, b ,c = map(int, sys.stdin.readline().rstrip().split())


output = (a if a < b else b) if (a if a < b else b) < c else c 

print("%d" %output)