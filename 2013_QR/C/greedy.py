"""
Google Codejam 2013 Qualification Round; Problem C; Fair and Square
by DelkysWelffer
"""

from math import sqrt


def reverseString(st):
	return st[::-1]

def isPalindrome(number):
	number_str = str(number)
	return number_str == reverseString(number_str)

def isFairAndSquare(number):
	if not (number % sqrt(number) == 0): 
		return False
	return isPalindrome(number) and isPalindrome(int(sqrt(number)))

def findFairsSquares(A, B):
	count = 0
	for x in range(A, B):
		if isFairAndSquare(x):
			count += 1
	return count


if __name__ == "__main__":
	for T in range(1, int(input()) + 1):
		A, B = ( int(n) for n in input().split(' ') )
		print ("Case {}: {}".format(T, findFairsSquares(A, B)))

	