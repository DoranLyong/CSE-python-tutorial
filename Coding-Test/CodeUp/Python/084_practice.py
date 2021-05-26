# coding=<utf-8>

"""
[ref] https://codeup.kr/problem.php?id=1084

Question: 
    1. make various light color; RGB 
    2. compute the total combinations of all cases 
    3. compute the total number of the cases 

"""

r, g, b = map(int, input().split())


count = 0 

for i in range(0, r):
    for j in range(0, g): 
        for k in range(0, b): 


            print(i, j, k) 

            count += 1 


print(count)
