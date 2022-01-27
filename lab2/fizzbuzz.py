def main():
	stop = int(input("Enter a number: "))
	for x in range(1, stop + 1):
		if x % 3 == 0 or x % 5 == 0:
			if x % 3 == 0 and x % 5 == 0:
				print("FizzBuzz")
			elif x % 3 == 0:
				print("Fizz")
			elif x % 5 == 0:
				print("Buzz")
		else:
			print(x)

if __name__ == '__main__':
	main()
