"""
Write a fibonacci function
Write a function reverse to reverse a list. Can you do this without using list slicing?
Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...]. Write a function cumulative_sum to compute cumulative sum of a list. Does your implementation work for a list of strings?
Write a function cumulative_product to compute cumulative product of a list of numbers.
Write a function unique to find all the unique elements of a list. (int & strings)
Write a function dups to find all duplicates in the list. (int & strings)
Write a function group(list, size) that take a list and splits into smaller lists of given size.
"""
"""
	Saul Flores
	web.saul.flores@gmail.com
"""




def fibonacci(num):
	""" regresa una lista con la suceccion fibonacci hasta la posicion indicada """

	def calcular_fibonacci(number):
		""" calcula el fibonacci de 'number' de forma recursiva y regresa dicho numero """

		toReturn = 0;
		if(number == 1):
			toReturn = 1
		elif(number > 1):
			toReturn = calcular_fibonacci(number - 1) + calcular_fibonacci(number - 2)		

		return toReturn
	
	i = 0	
	fibonacciList = []
	while(i < num):
		fibonacciList.append(calcular_fibonacci(i))
		i += 1
	return fibonacciList;
	



def reverse(list_a):
	""" toma una lista y regresa la misma lista pero en orden inverso """

	list_reverse = []
	sizeList = len(list_a) - 1

	for index in range(sizeList + 1):
		list_reverse.append(list_a[sizeList - index])

	return list_reverse



def cumulative_sum(list_a):
	""" 
		recive una lista de (enteros / string) y acumula (suma / concatena) sus elementos 
		input [a, b, c, d]
		output [a, a+b, a+b+c, a+b+c+d]
	"""
	temp_sum = list_a[0]
	list_sum = []

	for element in list_a:
		if(type(temp_sum) == str or type(element) == str):
			temp_sum = str(temp_sum) + str(element)
		else:
			temp_sum += element		

		list_sum.append(temp_sum)

	return list_sum



def cumulative_product(list_a):
	""" 
		recive una lista de enteros y multiplica sus elementos 
		input [a, b, c, d]
		output [a, a*b, a*b*c, a*b*c*d]
	"""
	temp_product = list_a[0]
	list_product = []

	for element in list_a:
		temp_product *= element		
		list_product.append(temp_product)
	return list_sum



def unique(list_a):
	"""
		find all the unique elements of a list. (int & strings)
	"""
	dictionary = {}	
	list_unique = []

	for element in list_a:
		try:
		   dictionary[element] += 1
		except KeyError:
			dictionary[element] = 0
	
	for key in dictionary:
		if(dictionary[key] == 0):
			list_unique.append(key)
	return list_unique
		   	



def dups(list_a):
	"""
		find all duplicates in the list. (int & strings)
	"""
	dictionary = {}	
	list_duplicate = []

	for element in list_a:
		try:
		   dictionary[element] += 1
		except KeyError:
			dictionary[element] = 0
	for key in dictionary:
		if(dictionary[key] >= 1):
			list_duplicate.append(key)

	return list_duplicate



def group(list_a, size):
	"""
		that take a list and splits into smaller lists of given size.
	"""
	list_groub = []
	list_temp = []
	for i in range(len(list_a)):		
		list_temp.append(list_a[i])
		if((i + 1) % size == 0):
			list_groub.append(list_temp)
			list_temp = []
	if(len(list_a) % size != 0):
		list_groub.append(list_temp)
		
	return list_groub


#print(fibonacci(20))
#reverse([1,2,3,4,5,6,7])
#cumulative_sum(['a', 'b', 'c', 'd', 1, 2, 3])
#cumulative_product([1,2,3,4,5,6,7])
#unique([1,2,3,4,1,2,3,4,5, 'a', 'b', 'a'])
#dups([1,2,3,4,5,1,2,3,8,1,2,3,7])
#group([1,2,3,4,5,6,7,8,9,0, 'a'], 11)

