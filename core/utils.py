

"""Compute Average values from list"""
def Average(lst):
    average =  sum(lst) / len(lst)
    return round(average, 1)



"""Compute Median values from list"""
def Median(lst):
    n = len(lst)
    index = n // 2
    # Sample with an odd number of observations
    if n % 2:
        return sorted(lst)[index]
    # Sample with an even number of observations
    return sum(sorted(lst)[index - 1:index + 1]) / 2
