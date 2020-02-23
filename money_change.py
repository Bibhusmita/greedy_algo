# Uses python3
import sys

def get_change(m):
	c=0
	for i in [10,5,1]:
		if(m>=i):
			n=m//i
			c+=n
			m=m%i
			if(m==0):
				return c

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
