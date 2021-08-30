# find catalan number
#  first solution: recursive solution

#input:
#    n: nth catalan number
def catalan_sarching(n):
    #initial case
    if n<=1:
        return 1
    num=0
    for i in range(n):
        num += catalan_sarching(i)*catalan_sarching(n-i-1)

    return num




#dynamic programming solution
def catalan_dynamic_programming(n):
    #base case
    if n<=1:
         return 1
    # we want to search for n catalan numbers
    #  build table to store results of subproblem
    catalan_number=[0]*(n+1)
    #first two catalan numbers
    catalan_number[0],catalan_number[1]=1,1
    #start dynamic searching
    for i in range(2,n+1):
        for j in range(i):
            catalan_number[i]+=catalan_number[j]*catalan_number[i-j-1]
    return catalan_number[n]


#driver code

if __name__ == '__main__':
    n=10
    for i in range(n):
        print(catalan_sarching(i))
        print(catalan_dynamic_programming(i))