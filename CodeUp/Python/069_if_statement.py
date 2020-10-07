# coding=<utf-8>
"""
[ref] https://codeup.kr/problem.php?id=1069

Question:
    1. receive evaluation as letters (A, B, C, D ...)
    2. print it as comment 

        평가 내용 
        평가 : 내용
        A : best!!!
        B : good!!
        C : run!
        D : slowly~ 
        others : what? 
"""

eval = input() 


comment = {"A":"best!!!", "B":"good!!", "C":"run!", "D":"slowly~"}



if eval in comment.keys():
    print("%s" %comment[eval])

else: 
    print("%s" %"what?")