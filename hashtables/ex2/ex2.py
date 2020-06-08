#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
	def __init__(self, source, destination):
		self.source = source
		self.destination = destination


def reconstruct_trip(tickets, length):
	"""
	YOUR CODE HERE
	"""
	# Your code here

	route = []
	cache = {}
	key = 'head'

	for ticket in tickets:
		if ticket.source == "NONE":
			cache[ 'head'] = ticket.destination
#			print( cache[ 'head'])
		else:
			cache[ ticket.source] = ticket.destination
#			print( cache[ ticket.source])

	while cache[ key] != "NONE":
#		print( cache[ key])
		route.append( cache[ key])
		key = cache[ key]

	route.append( "NONE")
	

	print( route)
	return route
