
def calculate(stack):
	if stack.endswith('-'):
		return stack.count('-+') + stack.count('+-') + 1
	else:
		return stack.count('-+') + stack.count('+-')

# import time
if __name__ == '__main__':
	begin = time.time()
	for T in range(1, int(input()) + 1):
		print ("Case #{0}: {1}".format(T, calculate(input())))
	# print ("Time:", time.time() - begin)