def main():
	cols = int(input("Enter no. of columns: "))
	i = 0
	while i < cols:
		j = 1
		while j <= cols - i:
			print(j, end='')
			j += 1
		print()
		i += 1

if __name__ == '__main__':
	main()
