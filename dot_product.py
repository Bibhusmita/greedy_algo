#Uses python3

import sys

def max_dot_product(a, b,n):
    #write your code here
    res = 0
    a.sort()
    b.sort()
    res= sum([a[i]*b[i] for i in range(n)])
    return res

if __name__ == '__main__':
    
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    print(max_dot_product(a, b,n))
    
