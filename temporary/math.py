"""
some documentations

more detailed descriptions here
"""

# imports go here


def mean(num_lst):
    """
	Calculate the mean of a list of numbers
	
	Parameters
	----------
	num_lst : list
		The list to take the average of
	
	Returns
	-------
	ret: float
		The mean of a list
	
	Examples
	--------
	>>> mean([1,2,3,4,5])
	3.0	
	"""

    return sum(num_lst) / len(num_lst)

