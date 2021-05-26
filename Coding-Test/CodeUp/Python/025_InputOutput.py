"""
[ref] https://codeup.kr/problem.php?id=1025

Question:
    1. get one number in five-digit
    2. Print it into each digit
"""

data = input() 

for idx, value in enumerate(data): 

    print("[%d]" %(int(value)*10**(4-idx)))