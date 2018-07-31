"""
string utilities

more docs
"""
def title_string(s):
    """
    Converts a string to title case
    
    Title case meant that the first charactter of every words is capitalized, 
    otherwise lowercase 
    
    Parameters
    ----------
    s : str
        The string to convert to title case
        
    Returns
    -------
    str
        The input string in ttitle case
        
    Examples
    --------
    >>> title_string("this is a StrING to be ConverTeD")
    'This Is A String To Be Converted'
    """
    # Check type string
    if not isinstance(s, str):
        raise TypeError('The input must be type str')
    
    # check empty string
    if len(s) == 0:
        raise Exception('The input cannot be lenth 0')
        
    l = s.split(' ')
    for i in range(len(l)):
        word = l[i].lower()
        word = word[0].upper() + word[1:]
        l[i] = word

    return ' '.join(l)
