def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)


if __name__=="__main__":
    n = input("Enter the number")
    print(fact(int(n)))