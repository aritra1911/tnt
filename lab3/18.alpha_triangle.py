def main():
	n = int(input("Enter no. of rows: "))
	for i in range(n):
		for j in range(i, -1, -1):
			print(chr(65 + j) + " ", end='')
		print()

if __name__ == '__main__':
	main()
