"""
[ref] https://codeup.kr/problem.php?id=1041

Question:
    1. take one English letter 
    2. print the next letter 
"""

letter = input()
ascii_num = ord(letter)   # 'str' -> ASCII_num


print(chr(ascii_num + 1))




"""
Program to find the ASCII value of a character:

https://beginnersbook.com/2019/03/python-program-to-find-ascii-value-of-a-character/
"""