# coding=<utf-8> 

"""
[ref] https://codeup.kr/problem.php?id=1082

Question: 
    1. get one hexadecimal 
    2. print multiplication table of it. 
"""


num = int( input(), 16)    # get a char as hexadecimal



multi_table = "{:X}*{:X}={:X}"


for i in range(1,16):
    print(multi_table.format(num, i, num*i)) 





"""
https://infinitt.tistory.com/104
"""

#print('%X' %num)
#print("{:X}".format(num))
#print(f"{num:X}   ")


