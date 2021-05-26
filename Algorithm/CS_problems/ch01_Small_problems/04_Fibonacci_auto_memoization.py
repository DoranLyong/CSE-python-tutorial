#-*- coding: utf-8 -*-
"""
(ref) 알고리즘 이해: https://shoark7.github.io/programming/algorithm/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%84-%ED%95%B4%EA%B2%B0%ED%95%98%EB%8A%94-5%EA%B0%80%EC%A7%80-%EB%B0%A9%EB%B2%95
(ref) 코드 참고: https://github.com/davecom/ClassicComputerScienceProblemsInPython/blob/master/Chapter1/fib4.py
"""

"""
피보나치 수열 구하기 

- 특징: 0, 1, 1, 2, 3, 5, 8, 13, 21 ...  규칙으로 수가 나열 됨. 

- Auto meoization 으로 구현 
"""

#%% Auto Memoization technique 
from functools import lru_cache

""" 함수의 리턴결과를 캐시해 주는(=캐시 메모리에 저장하는) 데코레이터
    (ref) https://wikidocs.net/109299
    (ref) https://planbs.tistory.com/entry/Python-memoize
    (ref) https://docs.python.org/ko/3/library/functools.html
"""


# ================================================================= #
#                       1. Create a function                        #
# ================================================================= #
# %% 01. 피보나치 수열 공식 정의 
""" * n = 0, 1 일 때 => fibo(0) = 0, fibo(1) = 1 
    * n >=2 일 때 => fibo(n) = fibo(n-1) + fibo(n-2)
"""
@ lru_cache(maxsize=None)
def fibo(n: int) -> int: 
    return fibo(n-1) + fibo(n-2) if n >= 2 else n  # same definition as 02.Fibonacci-sequence.py


""" 캐시 메모리에 함수 리턴 결과가 저장되기 때문에 
    memoization 효과를 누를 수 있음 
"""


# ================================================================= #
#                            2. Main                                #
# ================================================================= #
# %% 02. Main
if __name__ == '__main__':
    print(f"n=5 번째 피보나치 수열: {fibo(4)}")
    print(f"n=8 번째 피보나치 수열: {fibo(50)}") # time complexity is reduced
# %%
