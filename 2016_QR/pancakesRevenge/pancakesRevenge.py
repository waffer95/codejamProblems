"""
Qualification Round 2016 Problem B: Revenge of the Pancakes
by DelkysWelffer
"""

import time

def flip(pancake):
	if pancake == '-':
		return '+'
	return '-'

def flip_n(n, stack):
	if not n: 
		return 
	for i in range(n):
		stack[i] = flip(stack[i])

def serve(stack):
	stack = list(stack)
	len_stack = len(stack)
	count = 0

	while '-' in stack:
		# print (stack) # debug
		end = 0

		if len_stack == 1:
			end = 1
		else:
			for pancake in range(len_stack):	
				if stack[pancake] != stack[0]:
					if pancake == len_stack - 1 and stack[pancake] == '-':
						end = len_stack
					else:
						end = pancake
					break
			if end == 0:
				end = len_stack

		flip_n(end, stack)
		count += 1
		# time.sleep(1) # debug
	return count


if __name__ == '__main__':
	for T in range(1, int(input()) + 1):
		print ("Case #{0}: {1}".format(T, serve(input())))
