# Test project for google cloud functions in python
#
# Euler 9 project: main.py
Uses a few functions from my number_theory library. 
Euler 9 is described here in more detail https://projecteuler.net/problem=9.
The algorithm uses the equation a=n^2-m^2, b=2*n*m, c=n^2+m^2.
It generates all primitive triples if n and m are coprime and one of the even the other odd.
From this equation and a+b+c=k follows k=2*n*(n+m). This means that there are three conditions for a solution
(1) 2 divides k
(2) n divides k
(3) n+m divides k
In addition to this there are two limits n<sqrt(k) and m<n. The program tests all n,m in this limits
for the three criteria (1), (2), (3). 
