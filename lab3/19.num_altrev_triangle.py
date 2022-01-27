def main():
	n = int(input("Enter no. of rows: "))
	for i in range(n):
		if i % 2 == 0:
			for j in range(1, i + 2):
				print(str(j) + " ", end='')
		else:
			for j in range(i + 1, 0, -1):
				print(str(j) + " ", end='')
		print()

if __name__ == '__main__':
	main()
