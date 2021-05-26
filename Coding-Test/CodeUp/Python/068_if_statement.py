# coding=<utf-8>
"""
[ref] https://codeup.kr/problem.php?id=1068

Question:
    1. take one integer in range 0~100 
    2. print its estimation score 

        평가 기준
        점수 범위 : 평가
        90 ~ 100 : A
        70 ~   89 : B
        40 ~   69 : C
        0 ~   39 : D
"""
score = int(input())


estimation = str()


if score >= 90:  estimation = "A"

elif score<=89 and score>=70:   estimation = "B"

elif score<=69 and score>=40:   estimation = "C"

else:  estimation = "D"


print("%s" %estimation)