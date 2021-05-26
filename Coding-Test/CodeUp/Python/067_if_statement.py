"""
[ref] https://codeup.kr/problem.php?id=1067

Question:
    1. take one integer; x 
    2. print its sign('minus', 'plus') and even/odd 
"""
x = int(input())


sign = "plus" if x > 0 else "minus"
category = "even" if x %2 ==0 else "odd"


print("%s" %sign)
print("%s" %category)