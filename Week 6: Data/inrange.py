def in_range(n, low, high):
  """
  Returns True if n is between low and high, inclusive. 
  high is guaranteed to be greater than low.
  """
  if n >= low and n <= high:
        return True

    # we could have also included an else statement, but since we are returning, it's fine without!
  return False

def main():
	n = input("n: ")
	low = input("low: ")
	high = input("high: ")
	if in_range(n, low, high):
		print("n is in range!")
	else:
		print("n is not in range...")

if __name__ == '__main__':
    main()
