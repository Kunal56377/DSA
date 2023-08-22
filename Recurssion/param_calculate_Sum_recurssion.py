

def addition(n,sum):
    if n < 1:
        print(sum)
        return 
    
    addition(n-1,sum+n)


if __name__=="__main__":
    n = input("Enter the number")
    addition(int(n),0)