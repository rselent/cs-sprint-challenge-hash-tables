def intersection(arrays):
	"""
	YOUR CODE HERE
	"""
	# Your code here
	cache = {}
	result = []

	for array in arrays:

		for n in array:

			if n in cache:
				cache[n] += 1
#				print( cache[n])
			else:
				cache[n] = 1
	
#	print( cache)
	for i in cache:
		if cache[i] == len( arrays):
			result.append( i)
	
	print( result)
	return result


if __name__ == "__main__":
	arrays = []

	arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
	arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
	arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

	print(intersection(arrays))
