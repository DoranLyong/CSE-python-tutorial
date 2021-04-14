#-*- coding: utf-8 -*-
"""
(ref) 알고리즘 이해: https://shoark7.github.io/programming/algorithm/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%84-%ED%95%B4%EA%B2%B0%ED%95%98%EB%8A%94-5%EA%B0%80%EC%A7%80-%EB%B0%A9%EB%B2%95
(ref) 코드 참고: https://github.com/davecom/ClassicComputerScienceProblemsInPython/blob/master/Chapter1/fib3.py
"""

"""
피보나치 수열 구하기 

- 특징: 0, 1, 1, 2, 3, 5, 8, 13, 21 ...  규칙으로 수가 나열 됨. 

- Memoization 구현 
"""

#%% Memoization technique 
from typing import Dict  

""" typing 왜 쓰지? 
    - 파이썬은 기본적으로 '동적할당' 이다 
    - 즉, 변수에 대입되는 값에 따라서 int, tuple, list 형태로 자료형이 바뀐다. 
    - 문제는 이러한 방식으로 값을 할당하면 사람에 의한 에러(human error)를 잡을 수 없다
    - 따라서, 변수에 대입되는 자료형을 명시해서 고정 시키는 과정이 필요하다. 

    (ref) https://michigusa-nlp.tistory.com/3
    (ref) https://scribblinganything.tistory.com/29
    (ref) https://www.daleseo.com/python-typing/
"""

memo: Dict[int, int] = {0: 0, 1: 1}   # typing 정의 
""" - memo 변수는 Dict 자료형이다 
    - key, value 는 모두 int 자료형이다. 
"""

# ================================================================= #
#                       1. Create a function                        #
# ================================================================= #
# %% 01. 피보나치 수열 공식 정의 
""" * n = 0, 1 일 때 => fibo(0) = 0, fibo(1) = 1 
    * n >=2 일 때 => fibo(n) = fibo(n-1) + fibo(n-2)
"""
def fibo(n: int) -> int: 
    
    if n not in memo:
        memo[n] = fibo(n-1) + fibo(n-2)  # memoization

    return memo[n]



# ================================================================= #
#                            2. Main                                #
# ================================================================= #
# %% 02. Main
if __name__ == '__main__':
    print(f"n=5 번째 피보나치 수열: {fibo(4)}")
    print(f"n=8 번째 피보나치 수열: {fibo(50)}") # time complexity is reduced
# %%
