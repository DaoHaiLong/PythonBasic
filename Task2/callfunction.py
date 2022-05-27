#  0 1 1 2 3 5 8 13 21 34 55
def fibonaci(n):
    if n < 0:
        print("ereor")
    elif n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonaci(n-1) + fibonaci(n-2)
    print("tong day so fibonaci:",fibonaci(9))


def PrintFibonacci(n):
    first = 0
    second = 1 
    #Loop until the length becomes 0.
    print(first)
    print(second)
    while n-2 > 0:
        temp = second
        second = first + second
        first = temp
        # that states the Fibonacci numbers
        n -= 1
        print(second)

if __name__ == "__main__":
    print("Fibonacci Series: ")
    PrintFibonacci(10)
    print("Tong day:",fibonaci(10) )
    pass