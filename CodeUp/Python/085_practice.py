# coding=<utf-8>

"""
[ref] https://codeup.kr/problem.php?id=1085

Question: 
    1. given recording time 's'. 
    2. compute the required storage capacity. 
"""

hz, bit, channel, sec = map(int, input().split()) 


# print(hz, bit, channel, sec)


required_storage = hz * bit * channel * sec  # bit unit

bit_to_MB = required_storage / (8 *( 1024*1024))  # 1024*1024 := 2**20 


print("{:.1f} MB".format(bit_to_MB))






"""
https://infinitt.tistory.com/104
"""
