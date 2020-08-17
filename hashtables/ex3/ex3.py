"""
    Problem: We need to calculate intersection of items in arrays. An intersection is when an item is present in multiple arrays.

    Solution: We can find the values which intersect between all of the arrays by populating a table with the results of each of them. 
    
    If a value exists in more than one table, we can increment a counter on that item. 
    
    Then we can filter our results by only including those items which have a count equal to the number of arrays that we've passed into the function.

"""

# Instantiate the table.
table = {}


def intersection(arrays):

    for arr in arrays:
        for item in arr:
            # if that item doesn't exist yet, we want it to exist and have a count of 1.
            if item not in table:
                table[item] = 1

            # Otherwise, if we've already seen that item before, we want to increase the count by 1.
            else:
                table[item] += 1

    # We can use the number of arrays to check for intersections.
    # If item's value value is equal num_of_arrays, that item is an intersection. It exists in every array.
    result = []

    for number, count in table.items():
        if count == len(arrays):
            result.append(number)

    print(result)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
