# function to match a stirng with a certain pattern, return matching result false or true
#input
     #s: input string
     #p: matched pattern

def pattern_match(s,p):
    #calculate length of matched pattern and input string
    m,n=len(s),len(p)

    #define a helper function to perform recursive searching
    def helper_func(s,p,m,n):
        # if input string is same as given pattern string
        if p==s:
            return True
        #if both stirngs are nulls
        if m==0 and n==0:
            return True
        #if matched string is empty
        if n==0 and m!=0:
            return False
            if (p[n - 1] == '*'):
                 return helper_func(s, p, m, n - 2)
            return False
        if (s[m - 1] == p[n - 1] or p[n - 1] == '.'):
            return helper_func(s, p, m - 1, n - 1)
        elif (p[n - 1] == '*'):
            if (helper_func(s, p, m, n - 2)):
                return True
            if (s[m - 1] == p[n - 2]):
                return helper_func(s, p, m - 1, n)
            if ((s[m - 1] != p[n - 2]) and p[n - 2] == '.'):
                return helper_func(s, p, m - 1, n)
            return False
        return False

    return helper_func(s, p, m, n)

#driver code
s='aaaabjas'
p='aaa*b.as'
print(pattern_match(s,p))