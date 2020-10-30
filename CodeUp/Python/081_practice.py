# coding=<utf-8>

"""
[ref] https://codeup.kr/problem.php?id=1081

Question: 
    1. throw two different dices, which are numbered from 1 through n and 1 through m. 
    2. print out all the possible cases. 

"""
import sys 


n, m = map(int, sys.stdin.readline().rstrip().split()) 

for i in range(1, n+1): 
    for j in range(1, m+1): 
        print(i, j)
