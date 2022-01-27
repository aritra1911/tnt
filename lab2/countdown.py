def main():
	x = int(input("Enter starting value: "))
	if x >= 0:
		while x >= 0:
			print("Countdown : " + str(x))
			x -= 1
	else:
		print("Can't countdown to zero from a negative number.")

if __name__ == '__main__':
	main()
