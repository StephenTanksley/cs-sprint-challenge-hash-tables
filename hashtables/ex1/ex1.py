"""
    Problem: We need a function which, given an arbitrary container of items of different weights, will return a tuple of the integers which denote the indices of where the weights are located in the container. We're comparing two weights at a time.
    
    Solution: We could create a lookup table which creates a table of all the different possible weights for the items in the container. Then when we call the function, we're only looking it up from a pre-existing table rather than trying to compute it in real time.
    
        Sub-Problem: What do we store in the table? 
        
        Sub-Solution: I think it would make sense to store the weight itself as the index. If we store the weight itself as the index, we can take the limit minus the weight of the first index to find the second index, then return both indexes as a tuple. When ordering the tuple, the larger weight needs to be in [0] position, the lighter index in [1] position.
        
        Because the function needs to run in linear time, I get to use a single for loop to solve this problem. No nested loops.

"""
weights_2 = [4, 4]


def get_indices_of_item_weights(weights, length, limit):

    table = {value: key for (key, value) in enumerate(weights)}

    print(table)

    for i in weights:
        # If I subtract item 1 from the limit and manage to find another item in the table, the reverse would be true. Item 1 plus item 2 would equal the limit. I can return item 1 and 2 in a tuple.
        item1 = i
        item2 = limit - i

        # if item1 == item2:

        if item1 and item2 in table:
            pre_format = (table[item2], table[item1])
            formatted = tuple(sorted(pre_format, reverse=True))
            return formatted

    return None


print(get_indices_of_item_weights(weights_2, 2, 8))
