
class Equation:

	equation_string = ""
	result = None

	def __init__(self, equation_string, result):
		self.equation_string = equation_string
		self.result = result



def makePairs(l):
	allPairs = []
	curr_list = list(l)

	while len(curr_list) > 1:
		i = 1
		while i < len(curr_list):
			allPairs.append((curr_list[0], curr_list[i],))
			i += 1

		del curr_list[0]

	return allPairs


def getAllEquationResults(pair):
	results = []
	results.append(Equation("({}) + ({})".format(pair[0].equation_string, pair[1].equation_string), pair[0].result + pair[1].result))
	results.append(Equation("({}) * ({})".format(pair[0].equation_string, pair[1].equation_string), pair[0].result * pair[1].result))
	results.append(Equation("({}) - ({})".format(pair[0].equation_string, pair[1].equation_string), pair[0].result - pair[1].result))
	results.append(Equation("({}) - ({})".format(pair[1].equation_string, pair[0].equation_string), pair[1].result - pair[0].result))
	try:
		results.append(Equation("({}) / ({})".format(pair[0].equation_string, pair[1].equation_string), pair[0].result / pair[1].result))
		results.append(Equation("({}) / ({})".format(pair[1].equation_string, pair[0].equation_string), pair[1].result / pair[0].result))
	except ZeroDivisionError:
		pass

	return results


def getEquation(l, n):

	#Turn numbers into equation objects
	equations = []
	for num in l:
		equations.append(Equation(str(num), num))


	#Make list of number lists, initially containing only the numbers of l
	all_lists = [equations]

	#loop through the lists until they all have a length of 1
	while len(all_lists[0]) != 1:
		new_lists = []
		#loop through every list
		for resulting_list in all_lists:
			#get all pairs of list
			pairs = makePairs(resulting_list)
			for pair in pairs:
				#get list of results of each operation
				allResults = getAllEquationResults(pair)
				#make list, with the equation objects included in current pair removed
				removedPair_list = [eq for eq in resulting_list if eq not in pair]
				#extend new_lists with lists including each of the results for the given pair
				for result in allResults:
					new_lists.append(removedPair_list + [result])

		#check if result matches n
		for resulting_list in new_lists:
			for eq in resulting_list:
				if eq.result == n:
					return eq.equation_string

		all_lists = list(new_lists)



	#if this point is reached, a valid equation wasn't found
	return None

