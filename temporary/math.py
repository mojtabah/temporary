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
    # check that user apsses list
    if not isinstance(num_lst, list):
        raise TypeError('Input must be type list')
    
    # Check that list has length
    if len(num_lst) == 0:
        raise ZeroDivisionError('Cannot calculate mean of empty list')
        
    try:
        ret = sum(num_lst) / len(num_lst)
    except TypeError:
        raise TypeError('Values of list must be type int or float')
        
    return ret

