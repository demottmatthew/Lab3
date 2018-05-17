def power(n, p):
    if p == 0:
        return 1
    else:
        return n * power(n, p -1)

def main():
    print(power(2, 3))

main()