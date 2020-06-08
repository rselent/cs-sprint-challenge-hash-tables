# Your code here
import re


def finder(files, queries):
	"""
	YOUR CODE HERE
	"""
	# Your code here
	result = []
	testQuery = queries[-4:]

	for a, searchTerm in enumerate( queries):
		if searchTerm[:4] == 'file':
			x = searchTerm[3:]
			y = len( x)
			for b, dirStruc in enumerate( files):
#				print( b, dirStruc)
#				xx = re.sub( '[^0-9]+', '', dirStruc).split( sep= '/', maxsplit= 1)
				if dirStruc[-y:] == x:
					result.append( dirStruc)
#					print( dirStruc)
#					print( dirStruc[-y:], x, y, b)
		elif (len( searchTerm) < 4) and (files[a][-3:] == queries[a][-3:]):
			result.append( files[a])

	print( result)
	return result


if __name__ == "__main__":
	files = [
		'/bin/foo',
		'/bin/bar',
		'/usr/bin/baz'
	]
	queries = [
		"foo",
		"qux",
		"baz"
	]
	print(finder(files, queries))
