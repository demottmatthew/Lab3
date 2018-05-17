def power(n, p):
    if p == 0: #once we get to power 0 we know that everything to the power of 0 is 1
                #you always look for your base case first and go from there
        return 1
    else:
        return n * power(n, p -1) #if the power is greater than 0 then we simply multiply the number by the next call

def fib(n):
    if n == 0: #the fibonacci sequence has two base cases because we are always adding two number together
        return 0 #so we make the two base cases the first two numbers
    elif n == 1:
        return 1
    else:
        return fib(n -1) + fib(n-2) #if not a base case, we add the previous two numbers together by calling fib(n-1) and fib(n-2)

def main():
    #print(power(2, 3))
    print(fib(0))
    print(fib(1))
    print(fib(2))
    print(fib(3))
    print(fib(4))
    print(fib(5))
    print(fib(6))
    print(fib(7))

main()