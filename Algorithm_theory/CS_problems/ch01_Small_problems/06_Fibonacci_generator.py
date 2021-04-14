#-*- coding: utf-8 -*-
"""
(ref) 알고리즘 이해: https://shoark7.github.io/programming/algorithm/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%84-%ED%95%B4%EA%B2%B0%ED%95%98%EB%8A%94-5%EA%B0%80%EC%A7%80-%EB%B0%A9%EB%B2%95
(ref) 코드 참고: https://github.com/davecom/ClassicComputerScienceProblemsInPython/blob/master/Chapter1/fib6.py
"""

"""
피보나치 수열 구하기 

- 특징: 0, 1, 1, 2, 3, 5, 8, 13, 21 ...  규칙으로 수가 나열 됨. 

- 고전적인 방식으로 iterative approach 활용 (반복적 풀이)
"""

#%% 
from typing import Generator

""" Generator:
    * iterator를 생성해 주는 함수
    * yield 키워드를 사용해서 generator 생성 

    (ref) https://planbs.tistory.com/entry/Python-Generator?category=653588
    (ref) https://wikidocs.net/16069
    (ref) https://bluese05.tistory.com/56
"""

# ================================================================= #
#                       1. Create a function                        #
# ================================================================= #
# %% 01. 피보나치 수열 공식 정의 
""" * n = 0, 1 일 때 => fibo(0) = 0, fibo(1) = 1 
    * n >=2 일 때 => fibo(n) = fibo(n-1) + fibo(n-2)
"""
def fibo(n: int) -> Generator[int, None, None]: 
    yield 0  # special case 
    if n > 0 : yield 1  # special case 

    last: int = 0   # initially set to fibo(0)
    next: int = 1   # initially set to fibo(1)

    for _ in range(1, n):
        last, next = next, last + next 
        yield next  # main generation step 


# ================================================================= #
#                            2. Main                                #
# ================================================================= #
# %% 02. Main
if __name__ == '__main__':
    for i in fibo(50):
        print(i)

# %%
