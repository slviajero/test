from math import sqrt

# some of the functions from my number theory library not imported but copied
# primitive euklid algorithm to find the greatest common divisor of two integers
def euklid(i,j):
    if (i<1 or j<1):
        return 0
    while (i!=j):
        if (i>j):
            i=i-j
        else:
            j=j-i
    return j

# coprimes means no common divisor >1
def coprime(i,j):
    return euklid(i,j)==1

# congruences
def congruent(i,j,m):
    return ((i%m)==(j%m))

# divisibility, odd and even
def divisible(i,j):
    return ((i%j)==0)
def odd(n):
    return not divisible(n,2)
def even(n):
    return divisible(n,2)
 
# the main function
def eulerf(k):
# condition (0) k must be even, for odd numbers there is no solution
    if odd(k):
        return []
    u=k//2
# condition (1) maximum n is sqrt(k/2) 
    nmax=int(sqrt(u))
# condition (3)
# walk through the range on possible n's 
# and check first if n divides u, create a list of these candidates
    nlist=[]
    for n in range(1,nmax+1):
        if divisible(u,n):
            nlist.append(n)
# check condition (2) and (4) now 
# all possible m must be <n and (n+m) must dived u
    sol=[]
    for n in nlist:
        for m in range(1,n):
            if divisible(u,n+m):
                sol.append((n,m))
# reduce the list further by asserting that n,m are coprime
# and one of them is even
# this yields only primitive solutions
    sol2=[]
    for t in sol:
        if coprime(t[0], t[1]):
            if even(t[0]) or even(t[1]):
                sol2.append(t)
# sol2 contains now all solutions that satisfy the congruences, 
# and that a>0, and that a,b,c are primitive
#
# now we construct the actual solutions and make sure that 
# they are scaled to the right k
    sol3=[]
    for s in sol2:
        n=s[0]
        m=s[1]
        a=n**2-m**2
        b=2*n*m
        c=n**2+m**2
        circ=a+b+c
        if (a>b):
            ap=a
            a=b
            b=ap
        f=int(k/circ)
        sol3.append((a*f, b*f, c*f))
    return sol3

# the called function, processing the web request, accepts a json or http request 
# copied from the hello world main function of google
def eulers_dream(request):
    
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        value=request.args.get('message')
    elif request_json and 'message' in request_json:
        value=request_json['message']
    else:
        value=1000
     
    k=int(value)
    result=eulerf(k)
    s="Solution of the Euler problem number 9 to find an pythagorean triplet a,b,c with a+b+c=k.<br><br>"
    if odd(k):
        s=s+f"There is no solution for odd k.<br>"
    ns=len(result)
    if ns==0:
        s=s+f"There is no solution for {k}.<br>"
    elif ns==1:
        r=result[0]
        s=s+f"There is one solution {r} for k={k}.<br>"
    else:
        s=s+f"There are {ns} different solutions {result} for k={k}.<br>"
    s=s+"<br>Call the function with the url argument ?message=k for a different value of k.<br>"
    s=s+"<br>Example for the value 1008: <br>"
    s=s+'<A HREF="https://europe-west2-staging-area-249707.cloudfunctions.net/function-1?message=1008">https://europe-west2-staging-area-249707.cloudfunctions.net/function-1?message=1008</A><br>'
    s=s+'Source and documentation <A HREF="https://github.com/slviajero/test">https://github.com/slviajero/test</A><br>'
    s=s+'The original problem <A HREF="https://projecteuler.net/problem=9">https://projecteuler.net/problem=9</A><br>'
    return s  

