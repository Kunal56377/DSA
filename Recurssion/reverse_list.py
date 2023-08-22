def reverse(index,arr,ds):

    if index == len(arr)-1:
        print(arr[index])
        ds.append(arr[index])
        return
        
    reverse(index+1,arr,ds)
    ds.append(arr[index])
    return ds


def reverseby_swap(index,arr,n):

    
    if index == int(n/2):
        return arr
    arr[index], arr[n-index-1] = arr[n-index-1], arr[index]
    return reverseby_swap(index+1,arr,n)
   
   

if __name__=="__main__":
    arr = [1,2,3,4,5]
    #ds = reverse(0,arr,[])
    arr = reverseby_swap(0,arr,5)
    print(arr)