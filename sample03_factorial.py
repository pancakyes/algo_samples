#sample with realization factorial function
def fact(n):
    if n == 1:
        return 1
    else:
       result = n * fact(n-1)
    return result

#tests
print(fact(5))
print(fact(100))
