# Uses python3
import sys

def get_optimal_value(n,W):
	value = 0
	if(W==0):
		return value
	list = []
	for _ in range(n):
		v,w = [int(i) for i in input().split()]
		if(v==0):
			continue
		list.append((v,w))
	list.sort(key = lambda x: x[0]/x[1], reverse = True)
    
	for v,w in list:
		if W==0:
			return value
		a = min(w, W)
		value += a*v/w
		W -= a
	return value
    

if __name__ == "__main__":
    
    n, W = [int(i) for i in input().split()]
    opt_value = get_optimal_value(n,W)
    print(opt_value)
