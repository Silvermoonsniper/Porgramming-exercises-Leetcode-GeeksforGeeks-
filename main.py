# maximum subarray searching with divide and conquer
def maximum_subarray_search(array,l,m,h):
    #calculate subarray in left side of middle point
    sum=0
    left_sum=-10000
    for i in range(m,l-1,-1):
        sum=sum+array[i]
        if sum>left_sum:
            left_sum=sum
    #calculate subarray on right hand side of middle point
    right_sum=-10000
    sum=0
    for j in range(m+1,h+1):
        sum=sum+array[j]
        if sum>right_sum:
            right_sum=sum
    #return maximum subarray, as maximum subarray can only have 3 possibilities:
    #   1. on the left side of middle point
    #   2. on the right side of middle point
    #   3. cross the middle point.
    return max(left_sum,right_sum,left_sum+right_sum)
#main function to follow this recursive searching
def maximum_subarray(array,low,high):
    #only one element remain, just return it
    if (low == high):
        return array[low]
    m=(low+high)//2

    return max(maximum_subarray(array,low,m),maximum_subarray(array,m+1,high),maximum_subarray_search(array,low,m,high))
if __name__ == '__main__':
    array=[2,-2,5,7,8,1,2]
    #calculate length of array
    length=len(array)
    max=maximum_subarray(array, 0, length-1)
    print("maximum subarray is", max)