"""
[ref] https://codeup.kr/problem.php?id=1063

Question:
    1. take two integers; (a, b) 
    2. print max out among them
    (!) Use Ternary Operatory -> https://m.blog.naver.com/wideeyed/221858874414
"""
import sys 

a, b = map(int, sys.stdin.readline().rstrip().split())


output = a if a > b else b 


print("%d" %output)








