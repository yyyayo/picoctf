def func1(x):
	i = 0
	while x != 0:
		if x & 1 != 0:
		# if x % 2 != 0:
			print(x)
			i = func2(i)
		x = x >> 1
		# x //= 2
	return i

def func2(i):
	return i + 3


if __name__ == "__main__":
	print(hex(func1(469937816)))