"""
    Problem: We want to see if a list has a corresponding negative number in a list. 
    
    This means that if we have a list containing [1, -1], we should get back a result of [1] because that's a number which has a corresponding negative in the list.
    
    Solution: We can populate a hash table with all of the positive values from the list. We can then check all values < 0 to see if their absolute value exists in the hash table. If it does, we can append the result to a list.

"""


def has_negatives(a):
    """
    YOUR CODE HERE
    """

    # Instantiate the table
    table = {}

    # Create a list for the result.
    result = []
    negatives = []

    # For every item, we want to populate a table with that item in it.
    for item in a:
        if item > 0:
            table[item] = 1
        else:
            negatives.append(item)

    for item in negatives:
        absolute_value = abs(item)
        if absolute_value in table:
            result.append(absolute_value)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
