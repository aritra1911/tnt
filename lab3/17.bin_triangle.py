def main():
	n = int(input("Enter no. of rows: "))
	for i in range(n):
		for j in range(i+1):
			print(str((i + j + 1) % 2) + " ", end='')
		print()

if __name__ == '__main__':
	main()
