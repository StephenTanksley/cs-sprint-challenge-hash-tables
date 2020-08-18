"""
    Problem: I'm given a list of filepaths and I need to look for the possible paths to get to certain files.
    
    Solution: I can use a hash table to keep a collection of filepaths that end in the filename I want.
    
    table = {
        "foo.txt": ["/home/davidlightman/foo.txt", "/usr/local/share/foo.txt"],
        "ls": ["/usr/bin/ls"]
    }
    
    I should then be able to return the result of table["foo.txt"] to get all of those filepaths.

"""


def finder(files, queries):

    # instantiate a table
    table = {}

    # Instantiate a list.
    results = []

    # We have to break up the filepath to get what we need from the end.
    for path in files:
        path_pieces = path.split("/")

        # "/home/davidlightman/foo.txt" ===> "foo.txt"
        single_name = path_pieces[-1]

        """
        
        Problem: We need to have a faster way of implementing table matching.
        
        Solution(?): Populate the table itself with the queries and then use the queries table to check against each file in the files argument.
        
        """

        # We can populate a table with all of the
        table[single_name] = []

        # if we successfully have a match between the filename and the query, we want to populate that into our table.
        if single_name in queries:
            table[single_name].append(path)

        # Cleanup line. We only want to return items with a value greater than 0. If there are no filepaths which match what we're looking for, we don't care.
        if len(table[single_name]) == 0:
            del table[single_name]

    # We want to grab all the items from our table which have filepaths in them and then throw those into a list for viewing. We have to unpack those items so they don't show up as nested lists. We unpack things using the *table[key] syntax.
    for key, _ in table.items():
        results.append(*table[key])

    return results


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
