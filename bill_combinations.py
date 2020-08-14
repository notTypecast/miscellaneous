

def withdraw(amount):

	function_permutations = allPermutations([get100s, get50s, get20s])

	allArrays = []

	for _ in range(len(function_permutations)):
		allArrays.append([0, 0, 0])

	current_permutation = 0

	for permutation in function_permutations:
		cAmount = amount

		func_returnValues = []

		for func in permutation:
			returnValue = func(cAmount)
			func_returnValues.append(returnValue)
			cAmount -= returnValue[0] * returnValue[1]

		if cAmount == 0:
		
			for returnValue in func_returnValues:
				if returnValue[1] == 100:
					allArrays[current_permutation][0] = returnValue[0]

				elif returnValue[1] == 50:
					allArrays[current_permutation][1] = returnValue[0]

				else:
					allArrays[current_permutation][2] = returnValue[0]

		current_permutation += 1

	allArrays = [arr for arr in allArrays if sum(arr) != 0]

	if len(allArrays) == 0:
		return None

	bestSolution = allArrays[0]

	for arr in allArrays:
		if sum(arr) < sum(bestSolution):
			bestSolution = arr

	return bestSolution


def get100s(amount):
	total_100s = 0

	if amount >= 100:
		total_100s = amount // 100

	return total_100s, 100

def get50s(amount):
	total_50s = 0

	if amount >= 50:
		total_50s = amount // 50

	return total_50s, 50

def get20s(amount):
	total_20s = 0

	if amount >= 20:
		total_20s = amount // 20

	return total_20s, 20

def allPermutations(l):

	permutations = []

	for item1 in l:
		for item2 in l:
			if item2 != item1:
				p = []
				p.extend([item1, item2])
				for item in l:
					if item not in p:
						p.append(item)
						break

				permutations.append(p)


	return permutations
	