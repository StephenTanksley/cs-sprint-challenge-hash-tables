"""
    Problem: Our tickets are all out of order.
    
    Solution: We can start by populating a table and using the sources as our keys, our destinations as values. Once we have those in a table, we can look up the next destination by providing the source.
    
    As we find each source and its corresponding destination, we can add those items to a list and return the final list.
"""


#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


# Create a dictionary for the tickets.
table = {}


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    for ticket in tickets:
        table[ticket.source] = ticket.destination

    # We can populate a list to become our new route as we re-order the tickets.
    stops = []

    # First step is to find the first ticket. This will be the one with a source of "None", because we aren't coming FROM another airport.

    start = table["NONE"]
    stops.append(start)

    # The ticket itself should tell you which location is next in your list.

    # For each item in the length of our trip
    for _ in range(1, length):

        # We'll look up the ticket at the end of our stops list.
        next_stop = table[stops[-1]]

        # When we look up table[stops[-1]], it returns the destination. We can then use that next destination to restart the process of getting our tickets in order.
        stops.append(next_stop)
    return stops
