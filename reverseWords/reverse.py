
def main():
	for T in range(1, int(input()) + 1):
		line = input().split(" ")
		line.reverse()

		print ("Case #%d:" % T, end=" ")

		for word in line:
			print (word, end=" ")

		print()


if __name__ == "__main__":
	main()