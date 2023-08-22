def addition(n):
    if n==0:
        return 0
    return n + addition(n-1)


if __name__=="__main__":
    n = input("Enter the number")
    print(addition(int(n)))