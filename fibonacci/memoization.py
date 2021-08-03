def fib(n):
    if memarr[n] == -1:
        memarr[n] = fib(n-2) + fib(n-1)
    return memarr[n]

n = 5
memarr = [-1]*(n+1)
memarr[1] = 0
memarr[2] = 1

# both will print the same value. 
print(fib(n))
print (memarr[n])
