#-*- coding: utf-8 -*-
"""
(ref) 알고리즘 이해: https://shoark7.github.io/programming/algorithm/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%84-%ED%95%B4%EA%B2%B0%ED%95%98%EB%8A%94-5%EA%B0%80%EC%A7%80-%EB%B0%A9%EB%B2%95
(ref) 코드 참고: https://github.com/davecom/ClassicComputerScienceProblemsInPython/blob/master/Chapter1/fib2.py
"""

"""
피보나치 수열 구하기 

- 특징: 0, 1, 1, 2, 3, 5, 8, 13, 21 ...  규칙으로 수가 나열 됨. 

- Recursive function 을 활용해서 구현할 것. 
  * 주의할 점: infinite recursion 은 발생시키지 말 것
  * 즉, break point는 있어야 함 
"""


# ================================================================= #
#                       1. Create a function                        #
# ================================================================= #
# %% 01. 피보나치 수열 공식 정의 
""" (ref) https://shoark7.github.io/programming/algorithm/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%84-%ED%95%B4%EA%B2%B0%ED%95%98%EB%8A%94-5%EA%B0%80%EC%A7%80-%EB%B0%A9%EB%B2%95

    * n = 0, 1 일 때 => fibo(0) = 0, fibo(1) = 1 
    * n >=2 일 때 => fibo(n) = fibo(n-1) + fibo(n-2)

    재귀 함수로 구현 됨. 
"""
def fibo(n: int) -> int: 
    return fibo(n-1) + fibo(n-2) if n >= 2 else n



# ================================================================= #
#                            2. Main                                #
# ================================================================= #
# %% 02. Main
if __name__ == '__main__':
    print(f"n=5 번째 피보나치 수열: {fibo(4)}")
    print(f"n=8 번째 피보나치 수열: {fibo(50)}") # the call tree will explode!
# %%
