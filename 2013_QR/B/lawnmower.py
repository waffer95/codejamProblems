"""
Google Codejam 2013 Qualification Round; Problem B; The Lawnmower
by DelkysWelffer
"""

def solve(lawn, N, M):
	if N == 1 or M == 1:
		return "YES"
	# let's check those rows... and columns
	for i in range(1, N - 1):
		for j in range(1, M - 1):
			if lawn[i][j] < lawn[i][0] or lawn[i][j] < lawn[i][N - 1]:
				return "NO"
			if lawn[j][i] < lawn[j][0] or lawn[j][i] < lawn[j][M - 1]:
				return "NO"

	return "YES"


if __name__ == '__main__':
	for T in range(1, int(input()) + 1):
		N, M = ( int(n) for n in input().split(' ') )
		lawn = [ [ int(n) for n in input().split(' ') ] for _ in range(N) ]
		print ("Case {}: {}".format(T, solve(lawn, N, M)))