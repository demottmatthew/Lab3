def factorial(n): #define our function with parameter n which is our integer that we want to multiply
    if n == 0: #if we get n equal to 0 then we return 1 because 0! is equal to 1
        return 1
    else: #if not 0 then we want to multiply our current number times our next n
            #for example if n = 4 then we are doing 4 * 3
        return n * factorial(n-1)

def main():
    print(factorial(4))

main()