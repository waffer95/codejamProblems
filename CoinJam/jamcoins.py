"""
Google Codejam Qualification Round 2016; Problem C; Coinjam
by DelkysWelffer
"""

def find_factor(number):
	i = 2
	while i * i < number:
		if number % i == 0:
			return i
		i += 1
	return 0

def convertBinaryToBase(x, base):
    return int(bin(x)[2:], base)
		
def print_coins(N, J):
	n = 2 ** (N - 1) + 1
	while J > 0:
		factors = []
		for base in range(2, 11):
			factor = find_factor(convertBinaryToBase(n, base))
			if factor != 0:
				factors.append(factor)
		
		n += 2
		
		if len(factors) < 9:
			continue
		
		print (convertBinaryToBase(n, 10), end = ' ')
		for factor in factors:
			print (factor, end = ' ')
		print ()
		J -= 1


def main():
	for T in range(1, int(input()) + 1):
		N, J = ( int(n) for n in input().split(' ') )
		print("Case #%d:" % T)
		print_coins(N, J)


if __name__ == "__main__":
	main()