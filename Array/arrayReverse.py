'''
using four types we can reverse the array :
    first --> reverse by recursive function.
    second --> reverse by itteration .
    third --> using list slicing 
    fourth --> by pyhton built in method .

'''

def reverseArrayRecursive(arr,start,end):
    ''' This is the recursive function which require start of an array and end of an array 
        its O(n) with grater space than other function. space complaxity increse with increase of size of array.
    '''

    if start >= end:
        return
    else:
        arr[start], arr[end] = arr[end], arr[start]
        reverseList(arr, start+1, end-1)


def reverseArray(arr,start,end):
    ''' This is the function to reverse the array in itterative ways 
        its time complaxity is O(n/2). better than recursive as space complexity.
    '''
    if len(arr) < 2:
        return arr
    else :
        while start < end:
            arr[start],arr[end] = arr[end],arr[start]
            start += 1 
            end -= 1 
        return arr
    
def reverseArraySlice(arr):
    ''' this is the function to reverse the array using list slicing .
    '''
    arr = arr[::-1] 
    return arr
        

def reverseArrayBuitInFunction(arr):
    ''' this the function to reverse the array using premitive method .
    '''
    arr.reverse()
    return arr

# i.e # Driver function to test above function 
if __name__ == "__main__":
    array = [1, 5, 6, 2, 4, 7]
    start = 0
    end = len(array) - 1 
    print(f'Array --> {array}')
    print(f'Reverse array --> {reverseArraySlice(array)}')
    