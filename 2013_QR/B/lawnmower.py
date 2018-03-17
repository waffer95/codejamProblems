"""
Google Codejam 2013 Qualification Round; Problem B; The Lawnmower
by DelkysWelffer
"""

def print_sq(sq):
	for row in sq:
		print (row)
	print ()

def solve(pattern, N, M):
	if N == 1 or M == 1:
		return "YES"

	lawn = [ [100 for _ in range(M)] for _ in range(N) ]

	for i in range(N):
		maxInRow = 0
		for j in range(M):
			if pattern[i][j] > maxInRow:
				maxInRow = pattern[i][j]
		for j in range(M):
			if maxInRow < lawn[i][j]:
				lawn[i][j] = maxInRow
	
	for j in range(M):
		maxInCol = 0
		for i in range(N):
			if pattern[i][j] > maxInCol:
				maxInCol = pattern[i][j]
		for i in range(N):
			if maxInCol < lawn[i][j]:
				lawn[i][j] = maxInCol

	if lawn == pattern:
		return "YES"

	return "NO"


if __name__ == '__main__':
	for T in range(1, int(input()) + 1):
		N, M = ( int(n) for n in input().split(' ') )
		pattern = [ [ int(n) for n in input().split(' ') ] for _ in range(N) ]
		print ("Case #{}: {}".format(T, solve(pattern, N, M)))