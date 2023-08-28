def palidrome(index,str,count):
    if index >=len(str)/2:
        if count == index:
            #print("True")
            return True
            
        else:
            return False
    
    if str[index] == str[len(str)-1-index]:
        count= count +1 

    return palidrome(index+1,str,count)


if __name__=="__main__":
    str = input("Enter the String")
    if palidrome(0,str,0) == True:
        print("palidrome")
    else:
        print("not palidrome")
    