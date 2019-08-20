from math import sqrt

def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.

    Trying to do a bit more. 

    """
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        value=request.args.get('message')
        return f"value was = {value}"
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Hello World! -- Hello. -- Hellohello!'
#
# euklids algorithm to find the greatest common divisor of two integers
# non recursive for a change
# no optimization like for example handling situation where one factor is 
# much bigger than the other
#
def euklid(i,j):
    if (i<1 or j<1):
        return 0
    while (i!=j):
        if (i>j):
            i=i-j
        else:
            j=j-i
        return j
    
def coprime(i,j):
    return euklid(i,j)==1

def congruent(i,j,m):
    return ((i%m)==(j%m))

def divisible(i,j):
    return ((i%j)==0)

def odd(n):
    return not divisible(n,2)

def even(n):
    return divisible(n,2)
 
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
#
# 
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
    s=f"Solution of the Euler problem to find an pythagorean triplet a,b,c with a+b+c={k}:<br>"
    if odd(k):
        s=s+f"There is no solution for odd k.<br>"
    ns=len(result)
    if ns==0:
        s=s+f"There is no solution for {k}"
    elif ns==1:
        r=result[0]
        s=s+f"There is a unique solution {r}"
    else:
        s=s+f"There are {ns} different solutions {result}"
    s=s+"Call the function with the url ?message= to calculate a different value.<br>"
    s=s+"Example: <br>"
    s=s+'<A HREF="https://europe-west2-staging-area-249707.cloudfunctions.net/function-1?message=1008">https://europe-west2-staging-area-249707.cloudfunctions.net/function-1?message=1008</A>'
    return s  
