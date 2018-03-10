"""
Google Codejam Qualification Round 2016; Problem A; Counting Sheep
by DelkysWelffer
"""

digits = {'0': 0,'1': 0,'2': 0,'3': 0,'4': 0,'5': 0,'6': 0,'7': 0,'8': 0,'9': 0}

def count_sheeps(N, i, digits):
	
	if N == 0: return "INSOMNIA"

	elif not(0 in digits.values()):
		return N * (i - 1)
	
	else:
		for d in str(N * i): digits[d] += 1
		return count_sheeps(N, i + 1, digits)


if __name__ == "__main__":

	for T in range(1, int(input()) + 1):
		N = int(input())
		print ("Case #{0}: {1}".format(T, count_sheeps(N, 1, digits.copy())))