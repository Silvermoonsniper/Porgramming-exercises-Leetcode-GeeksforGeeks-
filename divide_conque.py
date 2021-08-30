# find nth ugly number
import numpy as np
## Dynamic programming
def ugly_number_finder(n):
    #each  subsequence is ugly sequence itself multiply with divisor array
    #set initial indexes of divisors
    index_1,index_2,index_3=0,0,0
    #set divisor array
    divisor_1,divisor_2,divisor_3=2,3,5
    initial_divisor_1,initial_divisor_2,initial_divisor_3=divisor_1, divisor_2, divisor_3
    #set up ugly number array
    ugly_array=[0] * n
    #first ugly number
    ugly_array[0]=1
    #start search
    for j in range(1,n):

        ugly_array[j]=min(divisor_1,divisor_2,divisor_3)
        #increase index values by checking if it can be divided by divisors without remainder
        if ugly_array[j] == divisor_1:
            index_1+=1
            divisor_1=ugly_array[index_1]*initial_divisor_1
        if ugly_array[j] == divisor_2:
            index_2+=1
            divisor_2=ugly_array[index_2]*initial_divisor_2
        if ugly_array[j] == divisor_3:
            index_3+=1
            divisor_3=ugly_array[index_3]*initial_divisor_3
    return ugly_array[-1]
#call main function
if __name__ == '__main__':
    n=150
    print(ugly_number_finder(n))
