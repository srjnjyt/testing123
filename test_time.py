from time import time

def test_time(loop1,loop2):
	st = time()
	for i in range(loop1):
		for j in range(loop2):
			a = 1000**2
	time_taken = time() - st
	print('time taken: {} secs'.format(time_taken))
	
test_time(10000,10000)