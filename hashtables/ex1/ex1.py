"""
    Problem: We need a function which, given an arbitrary container of items of different weights, will return a tuple of the integers which denote the indices of where the weights are located in the container. We're comparing two weights at a time.
    
    Solution: We could create a lookup table which creates a table of all the different possible weights for the items in the container. Then when we call the function, we're only looking it up from a pre-existing table rather than trying to compute it in real time.
    
        Sub-Problem: What do we store in the table? 
        
        Sub-Solution: I think it would make sense to store the weight itself as the index. If we store the weight itself as the index, we can take the limit minus the weight of the first index to find the second index, then return both indexes as a tuple. When ordering the tuple, the larger weight needs to be in [0] position, the lighter index in [1] position.
        
        Because the function needs to run in linear time, I get to use a single for loop to solve this problem. No nested loops.

"""
weights_3 = [4, 6, 10, 15, 16]


def get_indices_of_item_weights(weights, length, limit):

    table = {value: key for (key, value) in enumerate(weights)}

    for i in weights:

        if (limit - i in table) and i in table:
            pre_format = (table[limit - i], table[i])
            formatted = tuple(sorted(pre_format, reverse=True))
            return formatted

    return None


print(get_indices_of_item_weights(weights_3, 5, 21))
