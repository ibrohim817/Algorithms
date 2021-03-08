# method 1  Time Complexity: O(2^n)
def fib_rec(n: int) -> int:
	if n < 3:
		return 1
	return fib_rec(n - 1) + fib_rec(n - 2)


# method 2 Time Complexity: O(n)
def fib_in_array(n: int) -> int:
	fibs = [1, 1]
	for i in range(1, n - 1):
		fibs.append(fibs[i] + fibs[i - 1])
	return fibs[n - 1]


# method 3 Time Complexity: O(log(n))
def fib_in_matrix(n: int) -> int:
	n -= 1
	if n < 2: return 1


	def multi_matrix(a: list, b: list) -> list:
		r = [[0, 0], [0, 0]]
		for i in range(2):
			for j in range(2):
				for k in range(2):
					r[i][j] += a[j][k] * b[k][i]
		return r


	def bin_pow(n: int) -> int:
		result = [[1, 0], [0, 1]]
		a = [[0, 1], [1, 1]]
		while n:
			if n&1:
				result = multi_matrix(result, a)
			a = multi_matrix(a, a)
			n >>= 1
		return result


	return bin_pow(n)[1][1]


# f1 = 1 and f2 = 1
n = 35
# 1 1 2 3 5 8 13 21 34 55

print('Method 1 -> got: {0} | expected: {1}'.format(fib_rec(n), 55))
print('Method 2 -> got: {0} | expected: {1}'.format(fib_in_array(n), 55))
print('Method 3 -> got: {0} | expected: {1}'.format(fib_in_matrix(n), 55))
