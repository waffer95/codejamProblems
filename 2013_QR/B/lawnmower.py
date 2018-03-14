"""
Google Codejam 2013 Qualification Round; Problem B; The Lawnmower
by DelkysWelffer
"""

def solve(lawn, N, M):
	if N == 1 or M == 1:
		return "YES"

	internals = set()
	for i in range(1, N - 1):
		for j in range(1, M - 1):
			internals.add(lawn[i][j])
			
	externals = set()
	for row in lawn:
		externals.add(row[0])
		externals.add(row[-1])
	for chunk in lawn[0]:
		externals.add(chunk)
	for chunk in lawn[-1]:
		externals.add(chunk)
		
	for internal in internals:
		for external in externals:
			if internal < external:
				return "NO"

	return "YES"


if __name__ == '__main__':
	for T in range(1, int(input()) + 1):
		N, M = ( int(n) for n in input().split(' ') )
		lawn = [ [ int(n) for n in input().split(' ') ] for _ in range(N) ]
		print ("Case {}: {}".format(T, solve(lawn, N, M)))